import vcf
import pyensembl

# Load Ensembl database for the human genome (GRCh38)
ensembl = pyensembl.EnsemblRelease(release=100)

IDENTIIED_GENES = {"UMODL1", "KRTAP12-2", "KRTAP10-10", "PCNT", "KRTAP10-7", "LCA5L", "COL18A1", "IFNAR2", "KRTAP10-1", "KRTAP10-3"}

def check_if_in_genes(record):
    chromosome = '21'
    position = record.POS

    # Get the gene(s) that overlap with the chromosomal position
    genes = ensembl.genes_at_locus(chromosome, position)

    # Print the gene names
    for gene in genes:
        if gene.gene_name in IDENTIIED_GENES:
            return gene.gene_name
    
def create_gene_vcf(input_vcf, output_vcf):
    # Open input VCF file
    template_reader = vcf.Reader(open(input_vcf, 'r'))

    # Create output VCF writer
    writer = vcf.Writer(open(output_vcf, 'w'), template_reader)
    vcf_reader = vcf.Reader(open('chrom21.vcf', 'r'))

    # Iterate over variant records
    for record in vcf_reader:
        # Extract desired fields
        chrom = record.CHROM
        pos = record.POS
        variant_id = record.ID

        # Extract gene information (modify this according to your VCF format)
        gene_info = check_if_in_genes(record)
        # gene_info = check_if_in_genes(record)

        if gene_info is not None:
            # Create a new variant record with selected fields
            new_record = vcf.model._Record(
                CHROM=chrom,
                POS=pos,
                ID=variant_id,
                INFO={'GENE': gene_info}, 
                REF = '',
                ALT = '',
                QUAL = '',
                FILTER = '',
                FORMAT = '',
                sample_indexes = ''
                # GENE=gene_info
            )

            # Write the new variant record to the output VCF file
            writer.write_record(new_record)

    # Close the VCF reader and writer
    # reader.close()
    writer.close()

    print(f"New VCF file created. Output saved to '{output_vcf}'.")

# Usage example
create_gene_vcf('template.vcf', 'output.vcf')




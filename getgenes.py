import pyensembl
import vcf
import csv

# Load Ensembl database for the human genome (GRCh38)
ensembl = pyensembl.EnsemblRelease(release=100)

vcf_reader = vcf.Reader(open('chrom21.vcf', 'r'))

genes_snp = {}

# Loop through each record and print the position ID
for record in vcf_reader:
    # Specify the chromosome number and position of interest
    chromosome = '21'
    position = record.POS

    # Get the gene(s) that overlap with the chromosomal position
    genes = ensembl.genes_at_locus(chromosome, position)

    # Print the gene names
    for gene in genes:
        if gene.gene_name in genes_snp:
            genes_snp[gene.gene_name] += 1
        else:
            genes_snp[gene.gene_name] = 1
        # print(gene.gene_name)

    # if len(genes) == 0:
    #     print("NONE")
# sorted_genes_snp = sorted(genes_snp.items(), key=lambda x:x[1])
# print(sorted_genes_snp)

with open('gene_count.csv', 'w') as f:
    for key in genes_snp.keys():
        f.write("%s,%i\n"%(key,genes_snp[key]))
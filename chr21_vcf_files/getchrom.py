import vcf

vcf_reader = vcf.Reader(open('ZSNPs.vcf', 'r'))
for record in vcf_reader.fetch('21'):  
    print(record) 
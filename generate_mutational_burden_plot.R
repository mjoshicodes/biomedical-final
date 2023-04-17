library(ggplot2)
library(dplyr)

genes <- read.csv(file = "/Users/jaiveersingh/Downloads/gene_count.csv", header = F)

genes <- genes %>%
  arrange(desc(V2))
top_genes <- genes[1:10,]

top_genes %>%
  arrange(V2) %>%   
  mutate(name=factor(V1, levels=V1)) %>%
  ggplot(aes(x=name, y=V2)) +
  geom_segment( aes(xend=name, yend=0)) +
  geom_point( size=4, color="orange") +
  geom_text(aes(label=V2), hjust=-.4) +
  coord_flip() +
  theme_bw() +
  ylab("Muational Burden") +
  xlab("Top Genes") + 
  expand_limits(y = 1500) + 
  ggtitle("Top 10 Genes With the Highest Mutational Burden")
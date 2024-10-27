from pathlib import Path

import numpy as np
import pandas as pd

filename = Path("./.data/counts.txt")

data_table = pd.read_csv(filename, index_col=0)
print(data_table.iloc[:5, :5])

samples = list(data_table.columns)

gene_file = Path("./.data/genes.csv")
gene_info = pd.read_csv(gene_file, index_col=0)
print(gene_info.iloc[:5, :])

print(f"Genes in data_table {data_table.shape[0]}")
print(f"Genes in gene_info {gene_info.shape[0]}")

matched_index = pd.Index.intersection(data_table.index, gene_info.index)

counts = np.asarray(data_table.loc[matched_index], dtype=int)

gene_names = np.array(matched_index)

print(f"{counts.shape[0]} genes measured in {counts.shape[1]} individuals.")

gene_lengths = np.asarray(gene_info.loc[matched_index]["GeneLength"], dtype=int)

print(counts.shape)
print(gene_lengths.shape)

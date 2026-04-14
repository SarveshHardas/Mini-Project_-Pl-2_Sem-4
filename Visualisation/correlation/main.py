import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_heatmap():
    data_path = '../../data/cleaned_data.csv'
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    
    df = pd.read_csv(data_path)
    
    
    top_exporters = df.groupby('Exporter')['TIV'].sum().nlargest(10).index
    top_importers = df.groupby('Importer')['TIV'].sum().nlargest(10).index
    
    filtered_df = df[df['Exporter'].isin(top_exporters) & df['Importer'].isin(top_importers)]
    
    
    pivot_table = filtered_df.pivot_table(index='Exporter', columns='Importer', values='TIV', aggfunc='sum', fill_value=0)
    
    plt.figure(figsize=(14, 10))
    sns.heatmap(pivot_table, annot=True, fmt=".1f", cmap='YlGnBu', cbar_kws={'label': 'Total TIV'})
    plt.title('Heatmap of Total TIV: Top 10 Exporters vs Importers')
    plt.xlabel('Importer')
    plt.ylabel('Exporter')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'topo10_tiv_heatmap.png'))
    plt.close()

if __name__ == "__main__":
    generate_heatmap()
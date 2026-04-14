import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_barchart():
    data_path = '../../data/cleaned_data.csv'
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    
    df = pd.read_csv(data_path)
    sns.set_style("whitegrid")
    
    
    top_exporters = df.groupby('Exporter')['Units'].sum().sort_values(ascending=False).head(10)
    
    plt.figure(figsize=(12, 7))
    sns.barplot(x=top_exporters.index, y=top_exporters.values, hue=top_exporters.index, palette='viridis', legend=False)
    plt.title('Top 10 Exporters by Total Units')
    plt.xlabel('Exporter')
    plt.ylabel('Total Units')
    plt.xticks(rotation=45)
    plt.grid(True, axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'top10_units_exporter.png'))
    plt.close()

if __name__ == "__main__":
    generate_barchart()
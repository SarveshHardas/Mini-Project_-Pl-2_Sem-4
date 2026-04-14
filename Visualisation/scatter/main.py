import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_scatter_plot():
    data_path = '../../data/cleaned_data.csv'
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    
    df = pd.read_csv(data_path)
    sns.set_style("whitegrid")
    
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Units', y='TIV_per_unit', alpha=0.6, color='indigo')
    plt.title('Units vs TIV per Unit')
    plt.xlabel('Units')
    plt.ylabel('TIV per Unit')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'units_vs_tiv_per_unit.png'))
    plt.close()

if __name__ == "__main__":
    generate_scatter_plot()
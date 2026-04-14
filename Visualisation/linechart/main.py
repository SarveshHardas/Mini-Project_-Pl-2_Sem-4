import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_linechart():
    data_path = '../../data/cleaned_data.csv'
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    
    df = pd.read_csv(data_path)
    sns.set_style("whitegrid")
    
    
    yearly_units = df.groupby('Year')['Units'].sum().sort_index()
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=yearly_units.index, y=yearly_units.values, marker='o', color='red', linewidth=2)
    plt.title('Total Units per Year')
    plt.xlabel('Year')
    plt.ylabel('Total Units')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'units_per_year.png'))
    plt.close()

if __name__ == "__main__":
    generate_linechart()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_boxplot():
    data_path = '../../data/cleaned_data.csv'
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    
    df = pd.read_csv(data_path)
    sns.set_style("whitegrid")
    
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df['Units'], color='lightgreen')
    plt.title('Boxplot of Units Distribution')
    plt.xlabel('Units')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'box_units.png'))
    plt.close()

if __name__ == "__main__":
    generate_boxplot()
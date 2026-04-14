import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_histogram():
    data_path = '../../data/cleaned_data.csv'
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    
    df = pd.read_csv(data_path)
    sns.set_style("whitegrid")
    
    
    plt.figure(figsize=(10, 6))
    sns.histplot(df['TIV'], bins=30, kde=True, color='skyblue')
    plt.title('Histogram of Total Indicative Value (TIV)')
    plt.xlabel('TIV')
    plt.ylabel('Frequency')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'hist_tiv.png'))
    plt.close()

def generate_kde():
    data_path = '../../data/cleaned_data.csv'
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    
    df = pd.read_csv(data_path)
    sns.set_style("whitegrid")
    
    
    plt.figure(figsize=(10, 6))
    sns.kdeplot(df['Units'], fill=True, color='orange')
    plt.title('KDE Plot of Units Distribution')
    plt.xlabel('Units')
    plt.ylabel('Density')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'kde_units.png'))
    plt.close()

if __name__ == "__main__":
    generate_histogram()
    generate_kde()
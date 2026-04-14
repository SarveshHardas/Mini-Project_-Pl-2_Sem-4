import pandas as pd
import matplotlib.pyplot as plt
import os

# load dataset
df = pd.read_csv(r"D:\py mini pro\Mini-Project_-Pl-2_Sem-4\data\cleaned_data.csv")

# select numeric columns
corr = df[["TIV", "Units", "TIV_per_unit"]].corr()

# create heatmap
plt.figure(figsize=(8,6))
plt.imshow(corr, cmap="coolwarm", interpolation="nearest")
plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heatmap")
plt.tight_layout()

# create output folder
os.makedirs("output", exist_ok=True)

# save graph
plt.savefig("output/correlation_heatmap.png")
plt.show()
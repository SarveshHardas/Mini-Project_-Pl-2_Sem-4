import pandas as pd
import matplotlib.pyplot as plt
import os

# load dataset
df = pd.read_csv(r"D:\py mini pro\Mini-Project_-Pl-2_Sem-4\data\cleaned_data.csv")

# remove missing values
df = df.dropna(subset=["Weapon", "Units"])

# create graph
plt.figure(figsize=(12,6))
df.boxplot(column="Units", by="Weapon")

plt.title("Boxplot of Units by Weapon")
plt.suptitle("")
plt.xlabel("Weapon")
plt.ylabel("Units")
plt.xticks(rotation=45)
plt.tight_layout()

# create output folder
os.makedirs("output", exist_ok=True)

# save graph
plt.savefig("output/units_by_weapon.png")
plt.show()
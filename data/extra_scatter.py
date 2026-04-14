import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("../../data/cleaned_data.csv")

# remove missing values
df = df.dropna(subset=["Weapon", "TIV_per_unit"])

# unique weapons
weapons = df["Weapon"].unique()

# prepare data
data = [df[df["Weapon"] == weapon]["TIV_per_unit"] for weapon in weapons]

# violin plot
plt.figure(figsize=(12,6))
plt.violinplot(data, showmeans=True)

plt.xticks(range(1, len(weapons)+1), weapons, rotation=45)
plt.title("Violin Plot of TIV_per_unit by Weapon")
plt.xlabel("Weapon")
plt.ylabel("TIV_per_unit")
plt.tight_layout()

# save output
plt.savefig("output/violin_tiv_weapon.png")

# show
plt.show()
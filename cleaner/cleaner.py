import pandas as pd

df = pd.read_csv("../data/raw_data.csv")

df = df.dropna(axis=1)
df = df.drop_duplicates()

df["Exporter"] = df["Exporter"].str.replace(r"\[.*?\]", "", regex=True).str.strip()
df["Importer"] = df["Importer"].str.replace(r"\[.*?\]", "", regex=True).str.strip()
df["Weapon"] = df["Weapon"].str.title()

df = df[df["Exporter"] != df["Importer"]]
df = df[df["Units"] > 0]
df = df[df["TIV"] > 0]

df["TIV_per_unit"] = df["TIV"] / df["Units"]
df = df.sort_values(by=["Year","Exporter"])
df.to_csv("../data/cleaned_data.csv", index=False)
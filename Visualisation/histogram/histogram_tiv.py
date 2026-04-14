import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\py mini pro\Mini-Project_-Pl-2_Sem-4\data\cleaned_data.csv")

plt.figure(figsize=(10,5))
plt.hist(df["TIV"], bins=20)

plt.title("Histogram of TIV")
plt.xlabel("TIV")
plt.ylabel("Frequency")
plt.grid(True)

import os
os.makedirs("output", exist_ok=True)

plt.savefig("output/histogram_tiv.png")
plt.show()

import os
os.makedirs("output", exist_ok=True)

plt.savefig("output/histogram_tiv.png")
plt.show()
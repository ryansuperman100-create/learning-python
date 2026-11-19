import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

records = pd.read_csv("openpowerlifting.csv")
print(records.head())
print(records.describe())
records[["Wilks"]].plot(kind="hist", bins=20, figsize=(10, 6))
wilks_mm = MinMaxScaler().fit_transform(records[["Wilks"]])
print(wilks_mm, "\n")
wilks_mm = pd.DataFrame(wilks_mm, columns=["Wilks"])
print(wilks_mm)
print(wilks_mm.describe())
wilks_mm.plot(kind="hist", bins=20, figsize=(10, 6))
plt.show()

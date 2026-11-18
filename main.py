import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

records = pd.read_csv("openpowerlifting.csv")
print(records.head())
print(records.describe())
records[["Wilks"]].plot(kind = "hist")
wilks_mm = MinMaxScaler().fit_transform(records[["Wilks"]])
wilks_mm = pd.DataFrame(wilks_mm, columns="Wilks")
print(wilks_mm)
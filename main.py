import pandas as pd
import matplotlib.pyplot as plt

dates = pd.read_csv("openpowerlifting.csv")
print(dates.head())
pivotData = dates.pivot(columns = "Equipment", values = "BestBenchKg")
print(pivotData)
pivotData.plot(kind = "box", figsize = (10,6))

dates["BenchGroup"] = pd.cut(dates["BestBenchKg"], bins = [0, 60, 100, 140, 180, 250])
dates.groupby("Equipment")["BenchGroup"].value_counts().unstack().plot(kind = "bar", stacked = True, figsize = (10, 6))
plt.show()
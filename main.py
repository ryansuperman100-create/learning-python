import pandas as pd
import matplotlib.pyplot as plt

dates = pd.read_csv("openpowerlifting.csv")
print(dates.head())
missing = dates["BestBenchKg"].isnull()
print(missing)
print(dates[missing])
print(dates.dropna(subset = ["BestSquatKg", "BestDeadliftKg"], how = "all"))
print(dates.dropna(axis=1 , thresh=380000))
print(dates.fillna({"BestDeadliftKg":-1}))
print(dates.fillna({"BestDeadliftKg":dates["BestDeadliftKg"].median()}))
mask = (dates["Name"] == "Angie Belk Terry") & (dates["MeetID"] == 0)
dates.loc[mask, "Wilks"] = 400
print(dates)
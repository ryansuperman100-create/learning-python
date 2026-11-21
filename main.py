import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split

records = pd.read_csv("openpowerlifting.csv")
response = "Wilks"
y = records[[response]]
predictors = list(records.columns)
print(predictors, '\n')
predictors.remove(response)
x = records[predictors]
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=.1, random_state=1234, stratify=x["Equipment"])
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

print(x["Equipment"].value_counts(normalize=True))
print(x_test["Equipment"].value_counts(normalize=True))

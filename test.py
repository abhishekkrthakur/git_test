import pandas as pd

df = pd.read_csv("train.csv", nrows=100)

print(df.head(20))
print(df.sentiment.value_counts())

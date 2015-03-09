import pandas as pd

data = pd.read_csv('train.csv', header=0)

data['Age'].fillna(data['Age'].mean(skipna=True), inplace=True)

data.to_csv("data_train.tst", ",")



import pandas as pd

import numpy as np

import seaborn as sns

import matplotlib.pyplot as plt
housedf=pd.read_csv("USA_Housing (1).csv")
print ("/nFirst 5 Rows of Dataset")
print(housedf.head)

print ("/nlast 5 Rows of Dataset")
print(housedf.tail())

print ("/n Dataset Info")
print(housedf.info())

print ("/nColumns Names")
print(housedf.columns)

print(housedf.describe())

print ("/nMissing values")
print(housedf.isnull().sum())

sns.pairplot(housedf)

plt.figure(figsize=(10,6))
sns.heatmap(housedf.corr(numeric_only=True),annot=True , cmap="coolwarm")

plt.figure()
sns.histplot(housedf["Price"], bins=30)
plt.show()
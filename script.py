#! /usr/bin/env python3

"""
# To filter data by groups, calculate regression between two variables from tabular data and plotting into a PNG"
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

dataframe = pd.read_csv("iris.csv")

versicolor = dataframe[dataframe.species == "Iris_versicolor"]
print(versicolor)

virginica = dataframe[dataframe.species == "Iris_virginica"]
print(virginica)

setosa = dataframe[dataframe.species == "Iris_setosa"]
print(setosa)

x = versicolor.petal_length_cm
y = versicolor.sepal_length_cm
regression = stats.linregress(x, y)
slope = regression.slope
intercept = regression.intercept

plt.scatter(x, y, label = 'Versicolor Data')
plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()

plt.savefig("versicolor_petal_v_sepal_length_regress.png")

x = virginica.petal_length_cm
y = virginica.sepal_length_cm
regression = stats.linregress(x, y)
slope = regression.slope
intercept = regression.intercept

plt.scatter(x, y, label = 'Virginica Data')
plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")

plt.savefig("virginica_petal_v_sepal_length_regress.png")


x = setosa.petal_length_cm
y = setosa.sepal_length_cm
regression = stats.linregress(x, y)
slope = regression.slope
intercept = regression.intercept

plt.scatter(x, y, label = 'Setosa Data')
plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")

plt.savefig("setosa_petal_v_sepal_length_regress.png")


quit()


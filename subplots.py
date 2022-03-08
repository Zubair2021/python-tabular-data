#! usr/bin/python3

# importing library
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

dataframe = pd.read_csv("iris.csv")

versicolor = dataframe[dataframe.species == "Iris_versicolor"]
print(versicolor)

virginica = dataframe[dataframe.species == "Iris_virginica"]
print(virginica)

setosa = dataframe[dataframe.species == "Iris_setosa"]
print(setosa)

ver_x = versicolor.petal_length_cm
ver_y = versicolor.sepal_length_cm
regression = stats.linregress(ver_x, ver_y)
slope = regression.slope
intercept = regression.intercept


plt.scatter(ver_x, ver_y, label = 'Versicolor Data')
plt.plot(ver_x, slope * ver_x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()

plt.savefig("versicolor_petal_v_sepal_length_regress.png")
quit()

vir_x = virginica.petal_length_cm
vir_y = virginica.sepal_length_cm
regression = stats.linregress(x, y)
slope = regression.slope
intercept = regression.intercept

plt.scatter(vir_x, vir_y, label = 'Virginica Data')
plt.plot(vir_x, vir_slope * vir_x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.savefig("virginica_petal_v_sepal_length_regress.png")
quit()

set_x = setosa.petal_length_cm
set_y = setosa.sepal_length_cm
regression = stats.linregress(set_x, set_y)
slope = regression.slope
intercept = regression.intercept

plt.scatter(set_x, set_y, label = 'Setosa Data')
plt.plot(set_x, slope * set_x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")

plt.savefig("setosa_petal_v_sepal_length_regress.png")


quit()



# Creating 6 subplots and unpacking the output array immediately
#fig, ((ax1, ax2, ax3)) = plt.subplots(1, 3)
#ax1.plot(ver_x, ver_y, color="orange")
#ax2.plot(vir_x, vir_y, color="green")
#ax3.plot(set_x, set_y, color="blue")


fig, axs = plt.subplots(3, 1)
axs[0, 0].plot(ver_x, ver_y)
axs[0, 0].set_title("Versicolor")

axs[1, 0].plot(vir_x, vir_y)
axs[1, 0].set_title("Virginica")

axs[2, 0].plot(set_x, set_y)
axs[2, 0].set_title("Setosa")

plt.legend()
plt.savefig("subplots_petal_v_sepal_length_regress.png")

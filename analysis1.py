# Pands project 2023
# script for analysis.py related to Iris flower species data set.

# 1. import the libraries needed to run the script.
import numpy as np
import pandas as pd                                   
from matplotlib import pyplot as plt                

# Load them Iris dataset from the .csv file
iris_df = pd.read_csv('IrisDataset.csv')

# define each species for plotting histograms
setosa = iris_df [iris_df.Species == "Iris-setosa"]
versicolor = iris_df [iris_df.Species == "Iris-versicolor"]
virginica = iris_df [iris_df.Species == "Iris-virginica"]

# histogram for Sepal Length
#def Sepal_Length_hist(): 
plt.hist(setosa['SepalLengthCm'], alpha=0.5, label='Iris Setosa', color="purple")
plt.hist(versicolor['SepalLengthCm'], alpha=0.5, label='Iris Versicolor', color="violet")
plt.hist(virginica['SepalLengthCm'], alpha=0.5, label='Iris Virginica', color="blue")
plt.legend(loc='upper right')
plt.title('Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency', size = 16)
plt.savefig("SepalLength.png")
plt.show()

# Histogram for Sepal Width
#def Sepal_Width_hist():
plt.hist(setosa['SepalWidthCm'], alpha=0.5, label='Iris Setosa', color="purple")
plt.hist(versicolor['SepalWidthCm'], alpha=0.5, label='Iris Versicolor', color="violet")
plt.hist(virginica['SepalWidthCm'], alpha=0.5, label='Iris Virginica', color="blue")
plt.legend(loc='upper right')
plt.title('Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency', size = 16)
plt.savefig("SepalWidth.png")
plt.show()

#Histogram for Petal Length
#def Petal_Length_hist():
plt.hist(setosa['PetalLengthCm'], alpha=0.5, label='Iris Setosa', color="purple")
plt.hist(versicolor['PetalLengthCm'], alpha=0.5, label='Iris Versicolor', color="violet")
plt.hist(virginica['PetalLengthCm'], alpha=0.5, label='Iris Virginica', color="blue")
plt.legend(loc='upper right')
plt.title('Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency', size = 16)
plt.savefig("PetalLength.png")
plt.show()

#Histogram for Petal Width
#def Petal_Width_hist():
plt.hist(setosa['PetalWidthCm'], alpha=0.5, label='Iris Setosa', color="purple")
plt.hist(versicolor['PetalWidthCm'], alpha=0.5, label='Iris Versicolor', color="violet")
plt.hist(virginica['PetalWidthCm'], alpha=0.5, label='Iris Virginica', color="blue")
plt.legend(loc='upper right')
plt.title('Petal Width')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency', size = 16)
plt.savefig("PetalWidth.png")
plt.show()
'''
# Generate .txt file for the Summary
# Write the summary of each variable to the file.
# Summary contains the variable(id), min & max values, the mean and the standard deviation of each variable.

with open('Summary_Iris.txt', 'w') as file:
    file.write('Iris Dataset Variables Summary:\n\n')              
    for column in iris_df.columns:
        file.write('Variable: {}\n'.format(column))
        file.write('Minimum value: {}\n'.format(iris_df[column].min()))
        file.write('Maximum value: {}\n'.format(iris_df[column].max()))
        file.write('Mean value: {}\n'.format(iris_df[column].mean()))
        file.write('Standard deviation: {}\n\n'.format(iris_df[column].std()))







def sepal_width():




def petal_length():



def petal_width():


# Load them Iris dataset from the .csv file
iris_df = pd.read_csv('IrisDataset.csv')


# function for uniting all the functions for creating histograms
def histograms():
    sepal_length()
    sepal_width()
    petal_length()
    petal_width()



# Main project code for analysis





# histo , scatter and pair plots .png
# reference: 
histograms()
scatterplots()
pairplot()
'''

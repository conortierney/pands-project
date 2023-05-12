# pands-project 2023
# Module: Programming & Scripting
# Author: Conor Tierney
# As part of H.Dip in Data Analytics @ ATU
# Author: Conor Tierney
# analysis.py for Iris Fisher's data set.
# Program for analysis of Iris flower species data set.


# 1. Import the libraries needed to run the code.
import numpy as np
import pandas as pd                                   
from matplotlib import pyplot as plt                

# Step 2: Load the Iris flower species dataset from the .csv file
iris_df = pd.read_csv('IrisDataset.csv')         # read data set into data frame df


# Step 3:  define each species of flower for plotting histograms
setosa = iris_df [iris_df.Species == "Iris-setosa"]
versicolor = iris_df [iris_df.Species == "Iris-versicolor"]
virginica = iris_df [iris_df.Species == "Iris-virginica"]

# Step 4: Histogram of each variable.Saved to png files on repository.

#Histogram dispalying Sepal Length.

def hist_SepalLength(): 
    plt.hist(setosa['SepalLengthCm'], alpha=0.5, label='Iris Setosa', color="purple")
    plt.hist(versicolor['SepalLengthCm'], alpha=0.5, label='Iris Versicolor', color="violet")
    plt.hist(virginica['SepalLengthCm'], alpha=0.5, label='Iris Virginica', color="blue")
    plt.legend(loc='upper right')
    plt.title('Sepal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Frequency', size = 16)
    plt.savefig("SepalLength.png")
    plt.show()

# Histogram displaying Sepal Width

def hist_SepalWidth():
    plt.hist(setosa['SepalWidthCm'], alpha=0.5, label='Iris Setosa', color="purple")
    plt.hist(versicolor['SepalWidthCm'], alpha=0.5, label='Iris Versicolor', color="violet")
    plt.hist(virginica['SepalWidthCm'], alpha=0.5, label='Iris Virginica', color="blue")
    plt.legend(loc='upper right')
    plt.title('Sepal Width')
    plt.xlabel('Sepal Width (cm)')
    plt.ylabel('Frequency', size = 16)
    plt.savefig("SepalWidth.png")
    plt.show()

# Histogram displaying Petal Length
def hist_PetalLength():
    plt.hist(setosa['PetalLengthCm'], alpha=0.5, label='Iris Setosa', color="purple")
    plt.hist(versicolor['PetalLengthCm'], alpha=0.5, label='Iris Versicolor', color="violet")
    plt.hist(virginica['PetalLengthCm'], alpha=0.5, label='Iris Virginica', color="blue")
    plt.legend(loc='upper right')
    plt.title('Petal Length')
    plt.xlabel('Petal Length (cm)')
    plt.ylabel('Frequency', size = 16)
    plt.savefig("PetalLength.png")
    plt.show()

# Histogram displaying Petal Width.
def hist_PetalWidth():
    plt.hist(setosa['PetalWidthCm'], alpha=0.5, label='Iris Setosa', color="purple")
    plt.hist(versicolor['PetalWidthCm'], alpha=0.5, label='Iris Versicolor', color="violet")
    plt.hist(virginica['PetalWidthCm'], alpha=0.5, label='Iris Virginica', color="blue")
    plt.legend(loc='upper right')
    plt.title('Petal Width')
    plt.xlabel('Petal Width (cm)')
    plt.ylabel('Frequency', size = 16)
    plt.savefig("PetalWidth.png")
    plt.show()

# Output of all Histogram functions. 
def histograms():
    hist_SepalLength()
    hist_SepalWidth()
    hist_PetalLength()
    hist_PetalWidth()


# Step 5: Scatterplots for each pair of variables.

# That is: Sepal length and Width & Petal Length and Width.

def scatplot_Sepal_length_width():
    plt.scatter(setosa['SepalLengthCm'], setosa['SepalWidthCm'], color='purple', label='Iris Setosa')
    plt.scatter(versicolor['SepalLengthCm'], versicolor['SepalWidthCm'], color='violet', label='Iris Versicolor')
    plt.scatter(virginica['SepalLengthCm'], virginica['SepalWidthCm'], color='blue', label='Iris Virginica')
    plt.legend(loc='upper right')
    plt.title('Scatter Plot of Sepal Length vs. Sepal Width')
    plt.xlabel('Sepal Length', size=16)
    plt.ylabel('Sepal Width',size=16)
    plt.savefig("Scatplot SepalLengthWidth.png")
    plt.show()

# use function for scatterplot
def scatplot_Petal_length_width():
    plt.scatter(setosa['PetalLengthCm'], setosa['PetalWidthCm'], color='purple', label='Iris Setosa')
    plt.scatter(versicolor['PetalLengthCm'], versicolor['PetalWidthCm'], color='violet', label='Iris Versicolor')
    plt.scatter(virginica['PetalLengthCm'], virginica['PetalWidthCm'], color='blue', label='Iris Virginica')
    plt.legend(loc='upper right')
    plt.title('Scatter Plot of Petal Length vs. Petal Width')
    plt.xlabel('Petal Length', size=16)
    plt.ylabel('Petal Width',size=16)
    plt.savefig("Scatplot PetalLengthWidth.png")
    plt.show()


# Output function to generate scatterplots.
def scatterplots():
    scatplot_Sepal_length_width()
    scatplot_Petal_length_width()

# prints Histograms first and Scatterplots second.
histograms()
scatterplots()


# Project code for Summary analysis (.txt file) in repsitory.

# Generate a text file for the summary of each variable in the data set.
# Write ('w') the summary of each variable to the file.
# Summary contains the variable(id), min & max values, the mean and the standard deviation for each.

with open('Summary_Iris.txt', 'w') as file:
    file.write('IRIS DATA SET VARIABLES SUMMARY:\n\n')              
    for column in iris_df.columns:
        file.write('Variable: {}\n'.format(column))
        file.write('Minimum value: {}\n'.format(iris_df[column].min()))
        file.write('Maximum value: {}\n'.format(iris_df[column].max()))
        file.write('Mean value: {}\n'.format(iris_df[column].mean()))
        file.write('Standard deviation: {}\n\n'.format(iris_df[column].std()))
  
# Ends.





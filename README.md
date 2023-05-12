# Programming and Scripting Project 2023

### Author: Conor Tierney

This is the repository for the final project of the Programming and Scripting module in the Higher Diploma in Science in Computing in Data Analytics 
at ATU. The projects focus is on investigating the well-known Fisher’s Iris data set. The dataset contains information about different types of Iris flowers.

## Table of Contents

* [Steps to complete project](#steps-to-complete-project)   
* [Fisher's Iris Dataset](#fisher's-iris-dataset)    
* [Iris dataset .csv file](#Iris-dataset-.csv-file)  
* [Iris Dataset Analysis and Code ](#Iris-Dataset-Analysis-and-Code)  

* [Plots](#plots)   
  *[Histograms](#histogram)    
  *[Histogram code](#histogram-code)   
  
* [Scatterplots](#scatter-plots)  
  *[Scatter plots code](#scatter-plots-code)  
  
* [Resources/ Libraries / Learnings](#resources-libraries-learnings)      
* [References](#references)      
  
-----------------------------------------------------------------------------------------

## Steps to complete project  

My approach to the project was to break down it down into smaller parts to write code, review the output of the files and generate a program analysisng the Iris data set.  

1. Import Python libraries needed to run the code.  
2. Import the Iris data set from a downloaded .csv file.  
3. Read in the data frame to summaries the species variables to a .txt file fo analysis.  
4. Define each species of flower before plotting the Histograms.  
5. Generate Histograms (png files) for each of the 4 variables.   
6. Gnerate Scatterplots (png files) for each pair of variables.   

-------------------------------------------------------------------------------------------

# Fisher's Iris Dataset  

The Fisher's Iris dataset is a widely used dataset in data analysis and statistics. It contains measurements of the various physical features of 3 types of Iris flowers, namely Setosa, Versicolor, and Virginica. It consists of 50 records for each of the 3 species.  
The dataset was created by Ronald Fisher in 1936 to show how discriminant analysis can tell different types of plants apart. It's a well-known dataset for exploratory data analysis, classification, clustering, and visualization purposes.
The data set contains 5 columns such as Petal Length, Petal Width, Sepal Length, Sepal Width and Species type [1], [2].


Image of the Iris flower species [3]

![image](https://user-images.githubusercontent.com/123323783/235207350-570be5ba-c0cf-48ab-8533-68786c7bf087.png)

------------------------------------------------------------------------------------------

## Iris dataset .csv file  

The [.csv file](https://github.com/conortierney/pands-project/blob/main/IrisDataset.csv) in this repository contains the Iris data set which comprises of 150 records, where each species has 50 samples [1].

The data set was originally accessed here: [Link](https://archive.ics.uci.edu/ml/datasets/iris)  

The dataset columns are : 

* __Id__  
* __SepalLengthCm__   
* __SepalWidthCm__     
* __PetalLengthCm__  
* __PetalWidthCm__ 
* __Species__    

![image](https://user-images.githubusercontent.com/123323783/235209194-c6e72f62-ce96-4415-93b0-c50d9f1eb1cb.png)

-------------------------------------------------------------------------------------------


# Iris Dataset Analysis and Code  

The data set is analysed with a python program called ***analysis.py*** (link) that is saved in the ***pands-project*** repository.  

*The first task of writing the program was to import the libraries needed to run the code.* 

***numpy*** is a python library that helps with statistical analysis and maths operations. It is a tool for working with arrays and matrices.  
It is widely used in data science [7].  

***pandas*** is a Python library that helps in data analysis and manipulation . it is a toll for working with tables called DataFrames. It reads data from warious sources auch as CSV files where users can manipulate and transform data with its built-in functions [8]. 

*In my **analysis.py** program pandas is used to create a summary of the data set in a .txt file from the .csv file*.  

***matplotlib*** is a library that helps create different types of graphs, like histograms, scatter plots, and bar charts. It can be used with Python and NumPy to make these graphs [9]. In this program it is used to generate the histograms and scatter plots that are saved in the repository.  




## Importing the Dataset

The code reads in the Iris flower species dataset from the .csv file to a DataFrame for analysis [6].


```python
iris_df = pd.read_csv('IrisDataset.csv')
```  

## Dataset Summary

The dataset analysis summary is saved in the repository as [Summary_Iris.txt](https://github.com/conortierney/pands-project/blob/main/Summary_Iris.txt)  

The following code generates the .txt file for analysis of each variable in the dataset. The summary file contains the variable(id), min & max values, the mean and the standard deviation
for each if the variables in the dataset. 

```python  
with open('Summary_Iris.txt', 'w') as file:
    file.write('IRIS DATA SET VARIABLES SUMMARY:\n\n')              
    for column in iris_df.columns:
        file.write('Variable: {}\n'.format(column))
        file.write('Minimum value: {}\n'.format(iris_df[column].min()))
        file.write('Maximum value: {}\n'.format(iris_df[column].max()))
        file.write('Mean value: {}\n'.format(iris_df[column].mean()))
        file.write('Standard deviation: {}\n\n'.format(iris_df[column].std()))
```
**Output Sample of the summary in the .txt file**  

`IRIS DATA SET VARIABLES SUMMARY:`  
  
`Variable: Id`  
`Minimum value: 1`    
`Maximum value: 150`    
`Mean value: 75.5`    
`Standard deviation: 43.445367992456916`    
  
`Variable: SepalLengthCm`   
`Minimum value: 4.3`   
`Maximum value: 7.9`   
`Mean value: 5.843333333333334`    
`Standard deviation: 0.8280661279778629`  


***The program outputs the following:*** 

1.  A summary of each variable to a single text file.  
2.  Histograms of each variable to png files.  
3.  Scatter plots of each pair of variables.  


------------------------------------------------------------------------------------------

## Plots

### Histogram

Histograms displaying each of the 4 variable: Sepal Length, Sepal Width, Petal Length and Petal Width are generated via the functions *'histograms():'* [4],[10].

***Each of the 3 species were defined for plotting the histograms***
```python  
setosa = iris_df [iris_df.Species == "Iris-setosa"]
versicolor = iris_df [iris_df.Species == "Iris-versicolor"]
virginica = iris_df [iris_df.Species == "Iris-virginica"]
```  


### Histogram code

**Example:**

```python
# Histogram dispalying Sepal Length.  
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
   ```  
   
  ```python  
# Output of all Histogram functions. 
def histograms():
    hist_SepalLength()
    hist_SepalWidth()
    hist_PetalLength()
    hist_PetalWidth()
```   

<img src = "https://github.com/sandraelekes/pands-project-2020/blob/master/Petal-lenght.png" alt ="Petal Length" width ="400" heigth="400"> <img src = "https://github.com/sandraelekes/pands-project-2020/blob/master/Petal-width.png" alt ="Petal Width" width ="400" heigth="400">  

<img src = "https://github.com/sandraelekes/pands-project-2020/blob/master/Sepal-lenght.png" alt ="Sepal Length" width ="400" heigth="400"> <img src = "https://github.com/sandraelekes/pands-project-2020/blob/master/Sepal-width.png" alt ="Sepal Width" width ="400" heigth="400">  


## Scatter Plots

<img src = "https://github.com/conortierney/pands-project/blob/main/Scatplot%20SepalLengthWidth.png" alt ="SepalLengthWidth" width ="400" heigth="400"> <img src = "https://github.com/conortierney/pands-project/blob/main/Scatplot%20PetalLengthWidth.png" alt ="PetalLengthWidth" width ="400" heigth="400">  


When comparing sepal lengths and widths we can see from the Scatter Plot analysis that the Setosa species has smaller sepal lengths and larger sepal widths. The Virginica species has larger sepal length but smaller sepal widths and Versicolor sits in the middle in terms of length and width.

Scatter plot analysis also shows us that the Setosa species also has the smallest petal length and widths. Again, Virginica has the largest petal lengths and widths. Versicolor sits in the middle of the two.

### Scatter plots code

**Example:**  

```python
# Scatter plots for each pair of variables.
# That is: Sepal Length and Width & Petal Length and Width.
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
```
```python
# Output function to generate scatterplots.
def scatterplots():
    scatplot_Sepal_length_width()
    scatplot_Petal_length_width()
```  
   
-----------------------------------------------------------------------------------
# Technology:  

* Visual Studio Code
* cmder
* GIT
* GITHUB
* Python v2023.5.20
* Anaconda3


-------------------------------------------------------------------------------------

# Resources/ Libraries / Learnings

* Moodle: Programming and Scripting Module (Notes,Lecture and Tasks)  
* [Markdown Guide](https://www.markdownguide.org/basic-syntax#headings)  
* [How to add images to README file](https://medium.com/@justynagolawska/how-to-easily-add-screenshots-into-your-readme-file-on-github-d806a01d6ffd#:~:text=Take%20a%20screenshot%20of%20whatever,need%20to%20submit%20new%20issue.&text=That's%20it!)  
* [Writing on GitHub](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks)  
* [GitHub with VSCODE](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks)  
* [Python.org](https://www.python.org/)  
* [W3 schools](https://www.w3schools.com/python/)  
* matplotlib
* pandas
* numpy

------------------------------------------------------------------------------------



### References
[1] https://archive.ics.uci.edu/ml/datasets/iris  
[2] https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/   
[3] https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5    
[4] https://www.statology.org/pandas-histogram-size/  
[6] https://www.angela1c.com/projects/iris/   
[7] https://numpy.org/  
[8] https://www.activestate.com/resources/quick-reads/what-is-pandas-in-python-everything-you-need-to-know/    
[9] https://www.activestate.com/resources/quick-reads/what-is-matplotlib-in-python-how-to-use-it-for-plotting/  
[10] https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/  




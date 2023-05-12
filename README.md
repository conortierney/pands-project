# Programming and Scripting Project 2023

### Author: Conor Tierney

This is the repository for the final project of the Programming and Scripting module in the Higher Diploma in Science in Computing in Data Analytics 
at ATU. The projects focus is on investigating the well-known Fisher’s Iris data set. The dataset contains information about different types of Iris flowers.

## Table of Contents

* [Steps to complete project](#steps-to-complete-project)   
* Fisher's Iris Dataset    
* Iris dataset .csv file  
* Dataset summary  
* Dataset code and analysis description  
  * Resources to code  
  
* Plot generation    
  *Histograms  
  *Scatterplots  
 
*Summary  
*Resources / Learnings    
*References    
  
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
The data set contains 5 columns such as Petal Length, Petal Width, Sepal Length, Sepal Width and Species type. [1], [2]


Image of the Iris flower species [2]

![image](https://user-images.githubusercontent.com/123323783/235207350-570be5ba-c0cf-48ab-8533-68786c7bf087.png)

------------------------------------------------------------------------------------------

## Iris dataset .csv file  

The [.csv file](https://github.com/conortierney/pands-project/blob/main/IrisDataset.csv) in this repository contains the Iris data set which comprises of 150 records, where each species has 50 samples.

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

The code reads in the Iris flower species dataset from the .csv file to a DataFrame for analysis.


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

***Project code resources***
* Programming and Scripting 
* numpy
* pandas
* geeks
* matplotlib  

------------------------------------------------------------------------------------------

## Plots

### Histogram
ref : https://www.statology.org/pandas-histogram-size/

Histograms displaying each of the 4 variable: Sepal Length, Sepal Width, Petal Length and Petal Width are generated via the functions 'histograms():' [4], [11].

***Each of the 3 species were defined for plotting the histograms***
```python  
setosa = iris_df [iris_df.Species == "Iris-setosa"]
versicolor = iris_df [iris_df.Species == "Iris-versicolor"]
virginica = iris_df [iris_df.Species == "Iris-virginica"]
```  





### Histogram code

```python



## Scatter Plots

### Scatter plots code

----------------------------------------------------------------------------------
# Summary 


-----------------------------------------------------------------------------------
# Technology: 
VSCODE 
CMDER
GIT
GITHUB
MOODLE
ANACONDA/python


-------------------------------------------------------------------------------------
# References: 

https://www.markdownguide.org/basic-syntax#headings


review and download iris data set .csv file 
copy the file contents to vscode 
step 1: download and import dataset as a .csv file
step 2: use pandas to summaries the data set as a .txt file .


# Resources / Learnings


screenshot image to README file
https://medium.com/@justynagolawska/how-to-easily-add-screenshots-into-your-readme-file-on-github-d806a01d6ffd#:~:text=Take%20a%20screenshot%20of%20whatever,need%20to%20submit%20new%20issue.&text=That's%20it!  
MODDLE VLE course links . 

https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks

vscode 
https://gitprotect.io/blog/github-with-visual-studio-code-guide/#:~:text=VS%20Code%20allows%20you%20to,which%20you%20want%20to%20pull.  


Libraries cheat sheets
List of usefull cheat sheets for libraries used in this project:


references here for libraries used.


### References
[1] https://archive.ics.uci.edu/ml/datasets/iris  
[2] https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/ 
[2] https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5  
[3] https://archive.ics.uci.edu/ml/datasets/iris  
[4] https://www.statology.org/pandas-histogram-size/  
[5] https://www.angela1c.com/projects/iris_project/downloading-iris/#:~:text=The%20Iris%20Data%20Set%20is,described%20above%20in%20section%202.  
[6] https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/  SUMMARY / EXPLAINATION OF DATA SET
[7] https://numpy.org/
[8] https://www.activestate.com/resources/quick-reads/what-is-pandas-in-python-everything-you-need-to-know/
[9] https://www.activestate.com/resources/quick-reads/what-is-matplotlib-in-python-how-to-use-it-for-plotting/
[10] https://www.statology.org/pandas-histogram-size/
[11] https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/


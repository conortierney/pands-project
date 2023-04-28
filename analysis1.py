


import numpy as np
import pandas as pd                                 # Pandas, which is a great library for managing relational (i.e. table-format) datasets: 
from matplotlib import pyplot as plt                #import Matplotlib, which will help customize plots further.
#import seaborn as sns
#import sys


# step 1 - import pandas
import pandas as pd

# Load the dataset from the .csv file
iris_df = pd.read_csv('IrisDataset.csv')

# Open the text file to write the summary
with open('Summary_Iris.txt', 'w') as file:
    file.write('Iris Dataset Variables Summary:\n\n')              # Write the summary of each variable to the file
    for column in iris_df.columns:
        file.write('Variable: {}\n'.format(column))
        file.write('Minimum value: {}\n'.format(iris_df[column].min()))
        file.write('Maximum value: {}\n'.format(iris_df[column].max()))
        file.write('Mean value: {}\n'.format(iris_df[column].mean()))
        file.write('Standard deviation: {}\n\n'.format(iris_df[column].std()))

# the summary includes the min , max , mean value and the standard deviation of each variable.

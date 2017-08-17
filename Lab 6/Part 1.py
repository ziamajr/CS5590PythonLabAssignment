# David Ziama
# Class ID 3
# Lab Assignment 6
# Part 1
# Pick any dataset from the dataset sheet in class sheet and make one prediction model using your imagination
#  – Linear regression.
#  – Logistic regression


import numpy as np
import pandas as pd
import scipy.stats as stats
import sklearn
from sklearn import datasets
from sklearn import linear_model
import matplotlib.pyplot as plt


print("This is a program to predict the prices of homes and compare them to the actual vaules of homes in the Boston area:\n")
linear = linear_model.LinearRegression()
boston = datasets.load_boston()
boston.keys()
#Since the object boston is a dictionary, this is to look at keys within the dictionary
boston.data.shape
#This is indicating the data set information, this will eessneital have 506 rows and 13 colums
print (boston.feature_names)
#This is one of the keys within the dictionary boston, it is to print out this key for the user to see

y = boston.target
#This is to indicate what will be on our y axis
bos = pd.DataFrame(boston.data)
#This is to take the boston dataset and fit it to a pandad data fram to display the information linked with the feature names
bos.head()
#This is to indicate the columns and rows of the datasheet of information
bos.columns = boston.feature_names
#This is to input the columns with feature names
bos.head()
#This is to implement this heading into the boston dataFrame
boston.target[:5]
#This is to add the price target to the boston datafram
bos['PRICE'] = boston.target
#This is to include the price vaule within the datasheet information
print(bos)
#This is to print this information so we are able to see all the data that is going to be input

plt.scatter(bos.RM, bos.PRICE)
#This is to have our plot identified
plt.xlabel ("Average number of rooms per house (RM)")
#This is to indicate the x axis as the number of rooms per house
plt.ylabel ("Prices")
#This is to indicate the x axis as the number of rooms per house
plt.title("Relationship between RM and Price")
#This is to indicate the title of the plot
plt.show()
#This is to plot the graph

X = bos.drop('PRICE', axis = 1)
#This is to indicate the X vaule that will be predicted
plt.scatter(bos.PRICE, linear.predict(X))
#This will be the prediction called to predict the vaule of x
plt.xlabel ("Actual Prices:")
#This is to show the xlabel
plt.ylabel("Predicited prices:")
#This is to show the y label
plt.title("Actual Prices vs Predicted Prices:")
#This is to show the title of the graph
plt.show()
#This is to plot the graph
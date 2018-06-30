# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:51:50 2018

@author: Vishwesh Ravi Shrimali
"""

# Build a linear regression model using Python

import matplotlib.pyplot as plt

# The project can be divided into the following parts

# Take inputs from CSV file
# Calculate mean
# Calculate variance
# Calculate covariance
# Estimate coefficients
# Make predictions
# Plot data

xlabel = []
ylabel = []
y_train = []
x_train = []
x_test = []
y_test = []
y_train_predict=[]

def takeTrainInputs(csvFile):
    try:
        with open(csvFile,"r") as f:
            # Header
            label_x,label_y = f.readline().strip().split(',')
            xlabel.append(label_x)
            ylabel.append(label_y)
            # Read data
            for i in f.readlines():
                try:
                    x_train_data,y_train_data = list(map(float,i.split(',')))
                    x_train.append(x_train_data)
                    y_train.append(y_train_data)
                except ValueError:
                    print("Invalid input detected. Skipping the row.")
        return 0
    except FileNotFoundError:
        print("File not found")
        return -1

def takeTestInputs(csvFile):
    try:
        with open(csvFile,"r") as f:
            # Skip Header
            f.readline()
            # Read data
            for i in f.readlines():
                try:
                    x_test_data = float(i.strip())
                    x_test.append(x_test_data)
                except ValueError:
                    print("Invalid input detected. Skipping the row.")
        return 0
    except FileNotFoundError:
        print("File not found")
        return -1

def mean(values):
    return sum(values)/len(values)

def variance(values,mean):
    return sum([(i-mean)**2 for i in values])

def covariance(x_values, x_mean, y_values, y_mean):
    covar = 0
    for i in range(len(x_values)):
        covar += (x_values[i]-x_mean)*(y_values[i] - y_mean)
    return covar

def trainLinearRegressionModel():
    x_mean,y_mean = mean(x_train),mean(y_train)
    b1 = covariance(x_train,x_mean,y_train,y_mean)/variance(x_train,x_mean)
    b0 = y_mean - b1*x_mean
    return (b0,b1)

def predict():
    b0,b1 = trainLinearRegressionModel()
    for i in x_test:
        y_test.append(b0+b1*i)
    for i in x_train:
        y_train_predict.append(b0+b1*i)

def plotData():
    plt.plot(x_train,y_train,'o',markersize=8,color='r')
    plt.plot(x_test, y_test, 'x', markersize=8, color='k')
    x_merged = x_train+x_test
    y_merged = y_train_predict+y_test
    plt.plot(x_merged,y_merged,'-',color='b')
    plt.xlabel(xlabel[0])
    plt.ylabel(ylabel[0])
    
def linearRegressionModel():
    print("Training model")
    trainLinearRegressionModel()
    print("Training complete. Predicting data")
    predict()
    print("Prediction complete. Plotting result")
    plotData()
    
def main():
    fileName = input("Enter training data csv filename: ")
    if takeTrainInputs(fileName) == -1:
        print("Encountered an error. Program will quit now.")
        return 1
    fileName = input("Enter test data csv filename: ")
    if takeTestInputs(fileName) == -1:
        print("Encountered an error. Program will quit now.")
        return 1
    print("Running the linear regression model")
    linearRegressionModel()
    plt.show()
    print("Model finished running.")

if __name__ == "__main__":
    main()
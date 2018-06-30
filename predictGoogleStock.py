#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Predict Google's stocks after 15 days

Created on Fri Jun 22 18:45:55 2018

@author: hp
"""

# Import modules
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import numpy as np
import quandl
import datetime
import matplotlib.pyplot as plt

# API Config key
quandl.ApiConfig.api_key = 'HAZiMM4Jt5hjaqA-PHub'

# Read dataframe
df = quandl.get('WIKI/GOOGL')

# Define new features to be used
# Voltaility percentages
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low'])/df['Adj. Low']
# Percentage change
df['PCT_CHANGE'] = (df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']

# Keep features that are useful only
df = df[['Adj. Close','HL_PCT','PCT_CHANGE','Adj. Volume']]

# Column to forecast
# Other columns are features
forecast_col = 'Adj. Close'

# Forecast 15 days
forecast_out = 15

# Shift forecast column 15 units back to use
# as training label
df['label'] = df[forecast_col].shift(-forecast_out)

# Last 15 days data will now have NAN

# Define training dataset
X = np.array(df.drop(['label'],1))
# Preprocess the data (scale it)
X = preprocessing.scale(X)

# Data to forecast
X_forecast = X[-forecast_out:]
# Remove these last 15 columns from X
X = X[:-forecast_out]

# Define labels
y = np.array(df['label'])
# Remove last 15 days labels as they are NANs
y = y[:-forecast_out]

# Train test split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.20)

# Prepare classifier
clf = LinearRegression()
# Train dataset
clf.fit(X_train,y_train)

# Calculate accuracy
accuracy = clf.score(X_test,y_test)
print("Accuracy of the classifier = {:.2f}".format(accuracy))

# Get the predictions
predictions = clf.predict(X_forecast)

# Drop NAs
df.dropna(inplace=True)
# Put forecast as NAN
df['forecast'] = np.nan
# Get last date
last_date = df.iloc[-1].name
# Get date in unix format
last_date_unix = last_date.timestamp()
# Number of seconds in one day
one_day = 60*60*24
# Next day in unix format
next_date_unix = last_date_unix+one_day

# Plot data
for i in predictions:
    next_date = datetime.datetime.fromtimestamp(next_date_unix)
    next_date_unix += one_day
    df.loc[next_date] = [np.nan for j in range(len(df.columns)-1)] + [i]

df['Adj. Close'].plot(figsize=(15,6),c='blue')
df['forecast'].plot(figsize=(15,6),c='red')
plt.legend(loc=2)
plt.xlabel("Dates")
plt.ylabel("Adjusted closing price")
plt.title("Google stock predictions")
plt.savefig("Prediction1.png")
plt.show()

# To zoom in to predictions
df['Adj. Close'].plot(figsize=(15,6),c='blue')
df['forecast'].plot(figsize=(15,6),c='red')
plt.xlim(xmin=datetime.date(2015,12,10))
plt.ylim(ymin=400)
plt.legend(loc=2)
plt.xlabel("Dates")
plt.ylabel("Adjusted closing price")
plt.title("Zoomed in view")
plt.savefig("Prediction2.png")
plt.show()

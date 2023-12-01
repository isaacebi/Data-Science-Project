# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:32:24 2023

@author: isaac
"""

# %% libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# %%
folder = os.getcwd()
data = os.path.join(folder, 'data')

# %% Data Loading
for root, files, files in os.walk(data):
    csv_files = {}
    for file in files:
        if "csv" in file:
            file_path = os.path.join(root, file)
            read_file = pd.read_csv(file_path)
            csv_files[file] = read_file

# print(csv_files.keys())
# ------------------------------------------------- #
# 'carInsurance_test.csv', 'carInsurance_train.csv' #
# ------------------------------------------------- #

X_train = csv_files['carInsurance_train.csv']
X_test = csv_files['carInsurance_test.csv']

# %% Data Inspection

# it seems to have several missing data
print("\n# ----- Inspecting DataFrame overall information ----- #")
print(X_train.info())

# Findings:
# 1. There are several data type object -> need to do some data convert
# 2. There are several missing data. 
#    *'Outcome' are very severe

# ----------------------------- #
# checking on 'Outcome' columns #
# ----------------------------- #
print("\n# ----- Inspecting 'Outcome' ----- #")
print(X_train['Outcome'].unique())

# after reading the data explaination, outcome is the of previous marketing.
# which consists of [nan 'failure' 'other' 'success'].


# ----------------------------------- #
# checking on 'Communication' columns #
# ----------------------------------- #
print("\n# ----- Inspecting 'Communication' ----- #")
print(X_train['Communication'].unique())

# only indicate either person can be contacted or not
# might need more statistical analysis with the target


# ----------------------------------- #
# checking on 'Communication' columns #
# ----------------------------------- #
print("\n# ----- Inspecting 'Education' ----- #")
print(X_train['Education'].unique())

# based on my experiences, the educations do affect the tendency going for
# insurance, but lets try to prove it later


# ----------------------------------- #
# checking on 'Communication' columns #
# ----------------------------------- #
print("\n# ----- Inspecting 'Job' ----- #")
print(X_train['Job'].unique())

# this is a very challenging to replace the missing data, but for now lets
# drop all the missing values


# ----------------------------------- #
# checking on 'CarInsurance' columns #
# ----------------------------------- #
print("\n# ----- Inspecting 'CarInsurance' ----- #")
print(X_train['CarInsurance'].value_counts())

# slightly imbalance


# ----------------------------------- #
# checking on 'Call' columns #
# ----------------------------------- #
print("\n# ----- Inspecting 'Call' ----- #")
print(X_train[['CallStart', 'CallEnd']])

# i think its better to create a new column CallDuration

# creating 'Call Duration'
# Convert 'CallStart' and 'CallEnd' columns to datetime objects
X_train['CallStart'] = pd.to_datetime(X_train['CallStart'], format='%H:%M:%S')
X_train['CallEnd'] = pd.to_datetime(X_train['CallEnd'], format='%H:%M:%S')

# Calculate call duration and create a new column 'CallDuration'
X_train['CallDuration'] = X_train['CallEnd'] - X_train['CallStart']
X_train['CallDuration'] = X_train['CallDuration'].dt.total_seconds()


# %% Data Visualization
# get all column name
columns = list(X_train.columns)

# continous
conti = []
for col in X_train:
    if X_train[col].nunique() > 100:
        conti.append(col)


# categorical
categ = [x for x in columns if x not in conti]


# plot
sns.histplot(data=X_train, x='CallDuration', hue='CarInsurance')
plt.show()

















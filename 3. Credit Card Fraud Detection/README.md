# Card Credit Fraud Detection
Welcome to the Credit Card Fraud Detection project! This repo contains the ongoing code as well as resources for building a system to detect the fraudulent transaction in credit card. Leveraging Machine Learning techniques, this projects aims to contribute to ongoing efforts as well as learning purposes in securing financial transactions and protecting users from unauthorized activities.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Packages](#packages)
- [Usage](#usage)
- [Results](#results)

## Introduction
Credit card fraud occurs when unauthorized and fraudulent transactions are made using someone else's credit card information. This can happen through various means, including:

- **Stolen Cards:** Physical theft of credit cards or card information.
- **Skimming:** Illegitimate card readers capture and store card information during a legitimate transaction.
- **Phishing:** Fraudsters use deceptive emails or websites to trick individuals into providing their credit card details.
- **Data Breaches:** Hackers gain unauthorized access to databases containing credit card information.
- **Carding:** Testing stolen credit card information by making small transactions to verify if the card is still active.

Detecting and preventing credit card fraud is crucial to protecting individuals and financial institutions from financial losses and maintaining trust in electronic payment systems. Machine learning models are often employed to analyze transaction patterns and identify anomalies that may indicate fraudulent activity.

## Dataset
Incase if you needed the data, access [Card-Credit-Fraud-Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data). The author mentioned that:
> The **dataset** comprises transactions made by credit cards in September 2013 by European cardholders. This dataset presents transactions that occurred in two days, where we have 492 **frauds** out of 284,807 transactions. The dataset is highly **unbalanced**, with the positive class (frauds) accounting for 0.172% of all transactions.

> It contains only **numerical input variables** which are the result of a **PCA transformation**. Unfortunately, due to **confidentiality issues**, we cannot provide the original features and more background information about the data. Features **V1, V2, … V28** are the principal components obtained with PCA; the only features which have not been transformed with PCA are '**Time**' and '**Amount**'. Feature '**Time**' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature '**Amount**' is the transaction **Amount**, and this feature can be used for **example-dependant cost-sensitive learning**. Feature '**Class**' is the response variable and takes value 1 in case of **fraud** and 0 otherwise.

> Given the class imbalance ratio, we recommend measuring the accuracy using the **Area Under the Precision-Recall Curve (AUPRC)**. **Confusion matrix accuracy** is not meaningful for unbalanced classification.

## Packages
This project is developed using Python version 3.8.13 and relies on several essential libraries for data analysis and machine learning. Below is a list of key packages along with their versions used in this project:

- **Python:** 3.8.13
- **Pandas:** 1.4.2
- **NumPy:** 1.22.3
- **Matplotlib:** 3.5.2
- **Seaborn:** 0.11.2
- **Scikit-learn:** 1.0.2

To ensure compatibility and replicate the development environment, it is recommended to install these packages with the specified versions. You can install them using the provided [requirements.txt](link_to_requirements_file_here) file. If you encounter any issues or have specific requirements, feel free to modify the versions as needed.

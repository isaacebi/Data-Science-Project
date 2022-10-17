from random import random
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class data:
    def __init__(self, application, credit):
        self.df = application
        self.df2 = credit

    def caseOne(self):
        df_pivot = pd.pivot(
            self.df2,
            index='ID',
            values='STATUS',
            columns='MONTHS_BALANCE'
        )
        df_pivot.reset_index(inplace=True)
        df_pivot['window'] = df_pivot.isna().sum(axis=1)
        df_pivot = df_pivot[df_pivot.window > 20]
        df_pivot['due_count'] = np.where((df_pivot.iloc[:, 1:-1]=='0') | (df_pivot.iloc[:, 1:-1]=='1') | (df_pivot.iloc[:, 1:-1]=='2') | (df_pivot.iloc[:, 1:-1]=='3') | (df_pivot.iloc[:, 1:-1]=='4') | (df_pivot.iloc[:, 1:-1]=='5'), 1, 0).sum(axis=1)
        df_clean = pd.merge(self.df, df_pivot[['ID', 'window', 'due_count']], on='ID', how='inner')
        df_clean['bad_cus'] = np.where(df_clean.due_count > df_clean.due_count.median(), 1, 0)
        df_validation, df_train = train_test_split(df_clean, test_size=0.3, random_state=0)
        df_train, df_test = train_test_split(df_train, test_size=0.3, random_state=0)

        return [df_validation, df_test, df_train]
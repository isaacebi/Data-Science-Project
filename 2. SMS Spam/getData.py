# %%
from sklearn.model_selection import train_test_split
import requests, zipfile, io
import pandas as pd
import os

# %%
URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip"
RANDOM = 123
DATA_PATH = os.path.join(os.getcwd(), 'data')
DATA_SMS = os.path.join(os.getcwd(), 'data', 'SMSSpamCollection')
VALIDATE_CSV = os.path.join(os.getcwd(), 'data', 'validate.csv')
TRAIN_CSV = os.path.join(os.getcwd(), 'data', 'train.csv')
TEST_CSV = os.path.join(os.getcwd(), 'data', 'test.csv')

# %%
def createData(data_path):
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    
# %%
createData(DATA_PATH)

# get data from UCI datasets
r = requests.get(URL)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall(DATA_PATH)

# %%
df = pd.read_csv(DATA_SMS, sep='\t', names=['label', 'message'])
isValidate, isTrain = train_test_split(df, test_size=0.3, random_state=RANDOM)
forTrain, forTest = train_test_split(isTrain, test_size=0.3, random_state=RANDOM)

# %%
isValidate.to_csv(VALIDATE_CSV, index=False)
forTrain.to_csv(TRAIN_CSV, index=False)
forTest.to_csv(TEST_CSV, index=False)

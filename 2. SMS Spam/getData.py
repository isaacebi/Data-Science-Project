# %%
import requests, zipfile, io
import os    

#%%
URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip"

DATA_PATH = os.path.join(os.getcwd(), 'data')

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

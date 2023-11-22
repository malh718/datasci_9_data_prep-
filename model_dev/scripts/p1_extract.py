import pandas as pd 

## get data 

# original link: lake county cancer rates 
# data download link: 
datalink = 'https://data-lakecountyil.opendata.arcgis.com/datasets/lakecountyil::cancer-rates.csv?where=1=1&outSR=%7B%22latestWkid%22%3A3435%2C%22wkid%22%3A102671%7D'

df = pd.read_csv(datalink)
df.size
df.sample(5)
df.shape

missing_values = df.isnull().sum()
missing_values 

df_clean=df.dropna()
df_clean


## save as csv to WK9/code/model_dev/data/raw
df.to_csv('model_dev/data/processed/raw/cancer_data.csv', index=False)

## save as pickle to WK9/code/model_dev/data/raw
df.to_pickle('model_dev/data/processed/raw/cancer_data.pkl')


# Lake county cancer rates  
## original link: https://catalog.data.gov/dataset/cancer-rates-5cf0c
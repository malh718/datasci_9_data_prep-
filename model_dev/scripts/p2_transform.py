import pandas as pd 
from sklearn.preprocessing import OrdinalEncoder

## get data raw
df = pd.read_pickle('model_dev/processed/raw/cancer_data.pkl')

## get birth statisitcs (kept the name the same but it is about birth statistics)
df_rpt_dist = pd.read_csv('model_dev/processed/raw/Birth_Statistics.csv')
## get column names
df_rpt_dist.columns
df_rpt_dist.shape

missing_values2 = df_rpt_dist.isnull().sum()
missing_values2 

dfother_clean=df_rpt_dist.dropna()
dfother_clean
dfother_clean.shape

## do some data cleaning of colun names, 
## make them all lower case, replmove white spaces and rpelace with _ 
df.columns = df.columns.str.lower().str.replace(' ', '_')
df.columns

df_rpt_dist.columns = df_rpt_dist.columns.str.lower().str.replace(' ', '_')
df_rpt_dist.columns

## get data types
df.dtypes # nice combination of numbers and strings/objects 
len(df)

df.sample(5)

## drop columns
to_drop = [
    'FID',
    'shape_area',
    'shape_length'
]

df.drop(to_drop, axis=1, inplace=True, errors='ignore')

to_drop = [
    'FID',
    'shape_area',
    'shape_length'
]

df_rpt_dist.drop(to_drop, axis=1, inplace=True, errors='ignore')

df.sample(5)

df.columns

# keep columns 
to_keep = [
    'rd',
    'name'
]


df_rpt_dist = df_rpt_dist[to_keep]
df_rpt_dist['rd'] = pd.to_numeric(df_rpt_dist['rd'], errors='coerce')
df_rpt_dist.dropna(inplace=True)
df_rpt_dist['rd'] = df_rpt_dist['rd'].astype('int64')





## perform ordinal encoding on date_occ
enc = OrdinalEncoder()
enc.fit(df[['all_cancer']])
df['all_cancer_ordinal'] = enc.transform(df[['all_cancer']])

## create dataframe with mapping
df_mapping_date = pd.DataFrame(enc.categories_[0], columns=[zip])
df_mapping_date['all_cancer_ordinal'] = df_mapping_date.index
df_mapping_date

## save mapping to csv
df_mapping_date.to_csv('model_dev/PROCESSEDDATA/mapping_date.csv', index=False)

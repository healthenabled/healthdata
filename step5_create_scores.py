import pandas as pd


dfcats = pd.read_csv('2016_category_mappings.csv')
catcounts = dfcats['Indicator'].value_counts()

df = pd.read_csv('2016dataset_clean.csv')
print(df.columns)



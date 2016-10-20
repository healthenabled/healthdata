import pandas as pd
import numpy as np


df = pd.read_csv('2016dataset_clean.csv', index_col=0)

dfcats = pd.read_csv('2016_category_mappings.csv', index_col=0)

# Ignore any columns that don't contribute to scores
# Ignore these: meta, note
dfscores = df.copy()
dropcols = dfcats[dfcats['Indicator'].isin(['meta', 'note'])].index
dfscores.drop(dropcols.values, axis=1, inplace=True)
dfcats.drop(dropcols.values, axis=0, inplace=True)
catcounts = dfcats['Indicator'].value_counts()

# Convert values into point scores
# Types: date, list, number, yn, qtr, gislevel, maturity
qtrmap = pd.Series({'': 0, '0': 0, '25': 0.25, '25-50': 0.5,
                    '50-75': 0.75, '75': 1})
for col in dfcats.itertuples():  # ugly code, but gets job done for now
    if col[1] == 'yn':
        dfscores[col[0]] = np.where(df[col[0]] == 'Yes', 1, 0)
        continue
    if col[1] == 'qtr':
        dfscores[col[0]] = df[col[0]].map(qtrmap)
    if col[1] == 'gislevel':  # FIXIT: give points for having anything!
        dfscores[col[0]] = np.where(df[col[0]].str.len() > 0, 1, 0)
        continue
    if col[1] == 'maturity':  # FIXIT: give points for having anything!
        dfscores[col[0]] = np.where(df[col[0]].str.len() > 0, 1, 0)
        continue
    if col[1] == 'date':  # FIXIT: give points for having anything!
        dfscores[col[0]] = np.where(df[col[0]].str.len() > 0, 1, 0)
        continue
    if col[1] == 'number':  # FIXIT: need to define "good" here
        dfscores[col[0]] = 0
        continue
    if col[1] == 'list':
        continue

dfscores.to_csv('2016dataset_scores.csv')

# Add up all those scores, to create summary scores




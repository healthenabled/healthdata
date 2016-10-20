import pandas as pd


df = pd.read_csv('2016dataset_raw.csv')
statuscols = ['teleradiology', 'teledermatology', 'telepathology',
              'telepsychiatry', 'remotemonitoring', 'mhealth_tollfree',
              'mhealth_callcentre', 'mhealth_appointments',
              'mhealth_telehealth', 'mhealth_disaster', 'mhealth_adherence',
              'mhealth_community', 'mhealth_infoaccess', 'mhealth_records',
              'mhealth_mlearning', 'mhealth_dss', 'mhealth_monitoring',
              'mhealth_survey', 'mhealth_surveillance']

allcolvals = pd.Series([])
for col in statuscols:
    colvals = df[col].value_counts()
    allcolvals = allcolvals.append(colvals)

dfvals = pd.DataFrame({'text': allcolvals.index, 'count': allcolvals.values})
valcounts = pd.pivot_table(dfvals, index=['text'], aggfunc='sum')
valcounts.to_csv('2016dataset_statuscols.csv')

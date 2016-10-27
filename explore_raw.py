import pandas as pd


def explore_raw(rawfile='2016dataset_raw.csv'):
    df = pd.read_csv(rawfile)
    statuscols = ['teleradiology', 'teledermatology', 'telepathology',
                  'telepsychiatry', 'remotemonitoring', 'mhealth_tollfree',
                  'mhealth_callcentre', 'mhealth_appointments',
                  'mhealth_telehealth', 'mhealth_disaster',
                  'mhealth_adherence', 'mhealth_community',
                  'mhealth_infoaccess', 'mhealth_records',
                  'mhealth_mlearning', 'mhealth_dss', 'mhealth_monitoring',
                  'mhealth_survey', 'mhealth_surveillance']

    allcolvals = pd.Series([])
    for col in statuscols:
        colvals = df[col].value_counts()
        allcolvals = allcolvals.append(colvals)

    dfvals = pd.DataFrame({'text': allcolvals.index,
                           'count': allcolvals.values})
    valcounts = pd.pivot_table(dfvals, index=['text'], aggfunc='sum')
    valcounts.to_csv('2016dataset_statuscols.csv')
    return


def get_missing_countries():
    df1 = pd.read_csv('2016ghocountries.csv', header=None,
                      names=['code', 'name'])
    df2 = pd.read_csv('UNSTATS list of countries.csv')
    v1 = df1['code'].str.lower().values
    v2 = df2['*ISO ALPHA-3* *code*'].str.lower().values
    missingcodes = set(v2) - set(v1)
    missingcountries = df2[df2['*ISO ALPHA-3* *code*'].str.lower().isin(missingcodes)]
    missingcountries.to_csv('2016dataset_missingcountries.csv')
    print(missingcountries[['*   Country or area name*', '*ISO ALPHA-3* *code*']])
    return missingcountries

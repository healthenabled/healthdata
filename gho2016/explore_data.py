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


def get_missing_countries(uselist=0):
    masterlists = [('../supporting_data/UNSTATS list of countries.csv',
                    '*ISO ALPHA-3* *code*'),
                   ('../supporting_data/UN member countries 2016.csv',
                    'ISO3166')]
    master = masterlists[uselist]
    df1 = pd.read_csv('2016ghocountries.csv', header=None,
                      names=['code', 'name'])
    df2 = pd.read_csv(master[0])
    v1 = df1['code'].str.lower().values
    v2 = df2[master[1]].str.lower().values
    missingcodes = set(v2) - set(v1)
    missingcountries = df2[df2[master[1]].str.lower().isin(missingcodes)]
    missingcountries.to_csv('2016dataset_missingcountries.csv')
    return missingcountries


def get_missing_values():
    df = pd.read_csv('2016dataset_clean.csv')
    nullcount = []
    for col in df.columns:
        nullcount.append([col, df[col].isnull().sum()])
        # print('{}: {}'.format(col, df[col].isnull().sum()))
    dfnulls = pd.DataFrame(nullcount, columns=['column', 'nulls'])
    dfnulls.to_csv('2016dataset_columnnulls.csv')
    
    rownulls = pd.DataFrame(df.isnull().sum(axis=1), columns=['nulls'])
    rownulls['country'] = df['meta_country']
    rownulls.to_csv('2016dataset_rownulls.csv', columns=['country', 'nulls'])
    return


import pandas as pd


rawcolumns = [  # ['meta_country', '1', ''],
              ['policy_health', '3', '75'],
              ['policy_ehealth', '3', '58'],
              ['policy_his', '3', '66'],
              ['policy_telehealth', '3', '22'],
              ['funding_public', '3', '77'],
              ['funding_private', '3', '40'],
              ['funding_donor', '3', '63'],
              ['funding_publicprivate', '3', '42'],
              ['policy_multilingual', '3', '28'],
              ['sites_multilingual', '2', '48'],
              ['training_preservice', '3', '74'],
              ['training_inservice', '3', '77'],
              ['population_1000s', 'number', ''],
              ['lifeexpectancy_years', 'number', ''],
              ['GNI_percapita', 'number', ''],
              ['healthspend_percentgdp', 'number', ''],
              ['physician_per10000', 'number', ''],
              ['ICTdevindex_rank', 'number', ''],
              ['nurse_per10000', 'number', ''],
              ['mobilephone_percent', 'number', ''],
              ['hospitalbed_per10000', 'number', ''],
              ['internetusers_percent', 'number', ''],
              ['legal_ehealth', '2', '31'],
              ['legal_safety', '2', '46'],
              ['legal_privacyanyformat', '2', '78'],
              ['legal_privacydigital', '2', '54'],
              ['sharing_national', '2', '34'],
              ['sharing_international', '2', '22'],
              ['sharing_research', '2', '39'],
              ['owndata_access', '2', '29'],
              ['owndata_correction', '2', '32'],
              ['owndata_deletion', '2', '18'],
              ['owndata_sharingcontrol', '2', '28'],
              ['legal_registration', '2', '76'],
              ['legal_idmanagement', '2', '65'],
              ['teleradiology', 'list', ''],
              ['teledermatology', 'list', ''],
              ['telepathology', 'list', ''],
              ['telepsychiatry', 'list', ''],
              ['remotemonitoring', 'list', ''],
              ['elearning_students_medicine', '2', '58'],
              ['elearning_students_dentistry', '2', '39'],
              ['elearning_students_publichealth', '2', '50'],
              ['elearning_students_nursing', '2', '47'],
              ['elearning_students_pharmacy', '2', '38'],
              ['elearning_students_biomedical', '2', '42'],
              ['elearning_prof_medical', '2', '58'],
              ['elearning_prof_dentistry', '2', '30'],
              ['elearning_prof_publichealth', '2', '47'],
              ['elearning_prof_nursing', '2', '46'],
              ['elearning_prof_pharmacy', '2', '31'],
              ['elearning_prof_biomedical', '2', '34'],
              ['ehr_national', 'yndate', ''],
              ['ehr_legislation', '1', ''],
              ['ehr_primary', 'yndate', ''],
              ['ehr_secondary', 'yndate', ''],
              ['ehr_tertiary', 'yndate', ''],
              ['ehr_laboratory', '2', '35'],
              ['ehr_pathology', '2', '18'],
              ['ehr_pharmacy', '2', '33'],
              ['ehr_pacs', '2', '26'],
              ['ehr_vaccinationalerts', '2', '10'],
              ['ehr_billing', '2', '58'],
              ['ehr_supplychain', '2', '58'],
              ['ehr_hr', '3', '69'],  # NB text issue
              ['meta_region', '1', ''],
              ['sm_policy', '3', '18'],
              ['sm_policyhealth', '2', '5'],
              ['sm_org_healthpromotion', '2', '78'],
              ['sm_org_appointment', '2', '24'],
              ['sm_org_feedback', '2', '56'],
              ['sm_org_announcements', '2', '72'],
              ['sm_org_emergency', '2', '59'],
              ['sm_ind_learn', '2', '79'],
              ['sm_ind_decide', '2', '56'],
              ['sm_ind_feedback', '2', '62'],
              ['sm_ind_campaign', '2', '62'],
              ['sm_ind_forum', '2', '59'],
              ['policy_bigdata_health', '3', '17'],
              ['policy_bigdata_private', '3', '8'],  # NB text issue
              ['junk_country', '1', ''],  # junk, but affects neighbouring col
              ['mhealth_tollfree', 'list', ''],
              ['mhealth_callcentre', 'list', ''],
              ['mhealth_appointments', 'list', ''],
              ['mhealth_telehealth', 'list', ''],
              ['mhealth_disaster', 'list', ''],
              ['mhealth_adherence', 'list', ''],
              ['mhealth_community', 'list', ''],
              ['mhealth_infoaccess', 'list', ''],
              ['mhealth_records', 'list', ''],
              ['mhealth_mlearning', 'list', ''],
              ['mhealth_dss', 'list', ''],
              ['mhealth_monitoring', 'list', ''],
              ['mhealth_survey', 'list', ''],
              ['mhealth_surveillance', 'list', ''],
              ['junk_footer', 'junk', '']]

# Check which column types / misspellings we have here
# coltypes = set()
# for col in rawcolumns:
#     coltypes.add(col[1])
# print('{}'.format(coltypes))

df = pd.read_csv('2016dataset_raw.csv', index_col=0)
template = '(?P<{}>.*){}(?P<{}>.*)'
outcols = []

for col in rawcolumns:
    if col[1] == 'junk':
        df.drop(col[0], axis=1, inplace=True)
        continue
    if col[1] == 'number' and df[col[0]].dtype == object:
        df[col[0]] = df[col[0]].str.replace('[^0-9.]', '')
        outcols += [col[0]]
        continue
    if col[1] == 'number' and df[col[0]].dtype != object:
        outcols += [col[0]]
        continue
    if col[1] == '1':
        df[col[0]] = df[col[0]].str.strip()
        outcols += [col[0]]
        continue
    if col[1] == '2':
        newcol1 = col[0]
        newcol2 = 'junk'
        coltemplate = template.format(newcol1, col[2], newcol2)
        df[[newcol1, newcol2]] = df[col[0]].str.extract(coltemplate)
        outcols += [newcol1]
        continue
    if col[1] == '3':
        newcol1 = col[0]
        newcol2 = col[0] + '_note'
        coltemplate = template.format(newcol1, col[2], newcol2)
        df[[newcol1, newcol2]] = df[col[0]].str.extract(coltemplate)
        outcols += [newcol1, newcol2]
        continue
    if col[1] == 'yndate':
        newcol1 = col[0]
        newcol2 = col[0] + '_note'
        df[[newcol1, newcol2]] = df[col[0]].str.split(' ', expand=True, n=1)
        outcols += [newcol1, newcol2]
        continue
    if col[1] == 'list':
        newcol1 = col[0]
        newcol2 = col[0] + '_note'
        df[[newcol1, newcol2]] = df[col[0]].str.rsplit(' ', expand=True, n=1)
        outcols += [newcol1, newcol2]
        continue

# Remove the junk column that we've been putting column junk into
df['junk'] = ''
df.drop('junk', axis=1, inplace=True)

# Clean up the problem column: meta_region
df['meta_region'] = df['ehr_hr_note'] + ' ' + df['meta_region']
df.drop('ehr_hr_note', axis=1, inplace=True)
outcols.remove('ehr_hr_note')

# Clean up the problem column: meta_country
df['policy_bigdata_private_note'] = df['policy_bigdata_private_note'] + \
    ' ' + df['junk_country']
df['policy_bigdata_private_note'] = \
    [a.replace(b, '') for a, b in
     zip(df['policy_bigdata_private_note'].astype('str'),
     df.index.astype('str'))]
df.drop('junk_country', axis=1, inplace=True)
outcols.remove('junk_country')

# Strip out any remaining junk in string columns
for col in outcols:
    if df[col].dtype == object:
        df[col] = df[col].str.strip()
        df[col].replace('N/A', '', inplace=True)

# Clean up known problem cells.  FIXIT: find a better way to do this
# Syria "Yes 75 19" in policy_health because two "75"s in cell
df.loc['Syrian Arab Republic', 'policy_health'] = 'Yes'
df.loc['Syrian Arab Republic', 'policy_health_note'] = '1975'
# Costa Rica "Yes 8 198" in policy_bigdata_private because two 8s in cell
df.loc['Costa Rica', 'policy_bigdata_private'] = 'Yes'
df.loc['Costa Rica', 'policy_bigdata_private_note'] = '1988'
# Iran "NaN" in policy_bigdata_private_note
df.loc['Iran  Islamic Republic of ', 'policy_bigdata_private_note'] = ''


df[outcols].to_csv('2016dataset_clean.csv')

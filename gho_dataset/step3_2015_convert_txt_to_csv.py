import os
import glob
import re
import csv


headers = ['meta_country', 'policy_health', 'policy_ehealth', 'policy_his',
           'policy_telehealth', 'funding_public', 'funding_private',
           'funding_donor', 'funding_publicprivate', 'policy_multilingual',
           'sites_multilingual', 'training_preservice', 'training_inservice',
           'population_1000s', 'lifeexpectancy_years', 'GNI_percapita',
           'healthspend_percentgdp', 'physician_per10000', 'ICTdevindex_rank',
           'nurse_per10000', 'mobilephone_percent', 'hospitalbed_per10000',
           'internetusers_percent', 'legal_ehealth', 'legal_safety',
           'legal_privacyanyformat', 'legal_privacydigital',
           'sharing_national', 'sharing_international', 'sharing_research',
           'owndata_access', 'owndata_correction', 'owndata_deletion',
           'owndata_sharingcontrol', 'legal_registration',
           'legal_idmanagement', 'teleradiology', 'teledermatology',
           'telepathology', 'telepsychiatry', 'remotemonitoring',
           'elearning_students_medicine', 'elearning_students_dentistry',
           'elearning_students_publichealth', 'elearning_students_nursing',
           'elearning_students_pharmacy', 'elearning_students_biomedical',
           'elearning_prof_medical', 'elearning_prof_dentistry',
           'elearning_prof_publichealth', 'elearning_prof_nursing',
           'elearning_prof_pharmacy', 'elearning_prof_biomedical',
           'ehr_national', 'ehr_legislation', 'ehr_primary', 'ehr_secondary',
           'ehr_tertiary', 'ehr_laboratory', 'ehr_pathology', 'ehr_pharmacy',
           'ehr_pacs', 'ehr_vaccinationalerts', 'ehr_billing',
           'ehr_supplychain', 'ehr_hr', 'meta_region', 'sm_policy',
           'sm_policyhealth', 'sm_org_healthpromotion', 'sm_org_appointment',
           'sm_org_feedback', 'sm_org_announcements', 'sm_org_emergency',
           'sm_ind_learn', 'sm_ind_decide', 'sm_ind_feedback',
           'sm_ind_campaign', 'sm_ind_forum', 'policy_bigdata_health',
           'policy_bigdata_private', 'junk_country', 'mhealth_tollfree',
           'mhealth_callcentre', 'mhealth_appointments', 'mhealth_telehealth',
           'mhealth_disaster', 'mhealth_adherence', 'mhealth_community',
           'mhealth_infoaccess', 'mhealth_records', 'mhealth_mlearning',
           'mhealth_dss', 'mhealth_monitoring', 'mhealth_survey',
           'mhealth_surveillance', 'junk_footer']

keepset = '[^a-zA-Z0-9\.{}=\-/]'

datadir = '2015ghodata'
txtfiles = glob.glob(os.path.join(datadir, '*.txt'))
fin = open('2015_gho_pdfboxtemplate.txt', 'r')
ftemplate = fin.read()
fin.close()
#ftemplate = re.sub('\n', '=', ftemplate)
ftemplate = re.sub(keepset, ' ', ftemplate)
ftemplate = ftemplate.replace('{}', '(.*)')

fout = open('2015dataset_raw.csv', 'w')
cout = csv.writer(fout, quoting=csv.QUOTE_ALL)
cout.writerow(headers)

for filepath in txtfiles:
    fileroot = filepath[len(datadir) + 1:-4]
    print('Converting {}'.format(fileroot))

    fin = open(filepath, 'r')
    filetext = fin.read()
    fin.close()
    #filetext = re.sub('\n', '=', filetext)
    filetext = re.sub('Zero', '0', filetext)
    filetext = re.sub(keepset, ' ', filetext)
    dataset = re.findall(ftemplate, filetext)
    # print("found {}".format(dataset))
    if len(dataset) == 0:
        dataset = [[]]
    cout.writerow(dataset[0])

fout.close()

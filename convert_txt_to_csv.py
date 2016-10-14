import os
import glob
import re
import csv

keepchars = '[^a-zA-Z0-9\.{} ,%=]'
datadir = '2016ghodata'
txtfiles = glob.glob(os.path.join(datadir, '*.txt'))
fin = open('PDFconversionTests/pdfbox_afg_template.txt', 'r')
ftemplate = fin.read()
fin.close()
ftemplate = re.sub('\n', '=', ftemplate)
ftemplate = re.sub(keepchars, ' ', ftemplate)
ftemplate = ftemplate.replace('{}', '(.*)')

fout = open('2016dataset_raw.csv', 'w')
cout = csv.writer(fout, quoting=csv.QUOTE_ALL)

headings = ['countryname', 'policy_universalhealth',
            'policy_ehealth', 'policy_his', 'policy_telehealth',
            'funding_public', 'funding_private', 'funding_donor',
            'funding_publicprivate', 'policy_mumltilingualism',
            'multilanguagesites', 'training_preservice', 'training_inservice',
            'population_thousands', 'lifeexpectancy_years', 'gni_percapita',
            'healthexpenditure_percentgdp', 'per10000_physician',
            'ICTdevindex_rank', 'per10000_nurse', 'mobilephone_percent',
            'per10000_hospitalbed', 'internetuser_percent',
            'legal_telehealth', 'legal_safety', 'legal_privacyanyformat',
            'legal_privacydigital', 'legal_sharingnational',
            'legal_sharinginternational', 'legal_sharingresearch',
            'legal_individualaccess', 'legal_individualcorrection',
            'legal_individualdeletion', 'legal_individualsharingchoice',
            'legal_registration', 'legal_idmanagement',
            'teleradiology', 'teledermatology', 'telepathology',
            'telepsychiatry', 'remotemonitoring', 'elearning_medicine',
            'elearning_dentistry', 'elearning_publichealth',
            'elearning_nursing', 'elearning_pharmacy', 'elearning_biomed',
            'ehr_national', 'ehr_legislation', 'ehr_primary',
            'ehr_secondary', 'ehr_tertiary', 'ehr_laboratory',
            'ehr_pathology', 'ehr_pharmacy', 'ehr_pacs',
            'ehr_vaccinationalerts', 'ehr_billing', 'ehr_supplychain',
            'ehr_hr', 'region', 'policy_socialmedia',
            'policy_socialmediahealth', 'socialmedia_healthpromotion',
            'socialmedia_appointments', 'socialmedia_feedback',
            'socialmedia_generalannounce', 'socialmedia_emergencyannounce',
            'smindividual_learn', 'smindividual_decide',
            'smindividual_feedback', 'smindividual_communitycampaign',
            'smindividual_communityforum',
            'policy_bigdatahealth', 'policy_bigdataprivate',
            'junk1', 'mhealth_emergencyline', 'mhealth_callcentre',
            'mhealth_reminder', 'mhealth_telehealth', 'mhealth_disasters',
            'mhealth_adherence', 'mhealth_mobilization', 'mhealth_information',
            'mhealth_records', 'mhealth_mlearning', 'mhealth_dss',
            'mhealth_monitoring', 'mhealth_surveys', 'mhealth_surveillance',
            'junk2']

cout.writerow(headings)

for filepath in txtfiles:
    fileroot = filepath[len(datadir) + 1:-4]
    print('Converting {}'.format(fileroot))

    fin = open(filepath, 'r')
    filetext = fin.read()
    fin.close()
    filetext = re.sub(' N/A', ' ', filetext)
    filetext = re.sub(' Zero', ' 0', filetext)
    filetext = re.sub('\n', '=', filetext)
    filetext = re.sub(keepchars, ' ', filetext)
    dataset = re.findall(ftemplate, filetext)
    if len(dataset) == 0:
        dataset = [[]]
    cout.writerow(dataset[0])

fout.close()

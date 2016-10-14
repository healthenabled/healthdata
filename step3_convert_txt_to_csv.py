import os
import glob
import re
import csv


datadir = '2016ghodata'
txtfiles = glob.glob(os.path.join(datadir, '*.txt'))
fin = open('PDFconversionTests/pdfbox_afg_template.txt', 'r')
ftemplate = fin.read()
fin.close()
ftemplate = re.sub('[^a-zA-Z0-9\.{}]', ' ', ftemplate)
ftemplate = ftemplate.replace('{}', '(.*)')

fout = open('2016dataset_raw.csv', 'w')
cout = csv.writer(fout, quoting=csv.QUOTE_ALL)

for filepath in txtfiles:
    fileroot = filepath[len(datadir) + 1:-4]
    print('Converting {}'.format(fileroot))

    fin = open(filepath, 'r')
    filetext = fin.read()
    fin.close()
    filetext = re.sub('[^a-zA-Z0-9\.{}]', ' ', filetext)
    dataset = re.findall(ftemplate, filetext)
    print("found {}".format(dataset))
    if len(dataset) == 0:
        dataset = [[]]
    cout.writerow(dataset[0])

fout.close()

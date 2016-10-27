import subprocess
import os
import glob


datadir = '2016ghodata'
pdffiles = glob.glob(os.path.join(datadir, '*.pdf'))
extractstr = 'java -jar PDFconversionTests/pdfbox-app-2.0.3.jar ExtractText {} {}/{}.txt'

for filepath in pdffiles:
    fileroot = filepath[len(datadir) + 1:-4]
    print('Converting {}'.format(fileroot))
    command = extractstr.format(filepath, datadir, fileroot)
    subprocess.check_output(command, shell=True)

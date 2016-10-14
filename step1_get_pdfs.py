'''
Pull set of PDFs from WHO country listing page
'''

import requests
from bs4 import BeautifulSoup

countrylisturl = 'http://www.who.int/goe/publications/atlas/2015/en/'
html = requests.get(countrylisturl)

soup = BeautifulSoup(html.text)
countryblocks = soup.find_all('ul', 'a_z')
countrylis = sum([countryblocks[i].find_all('li')
                  for i in range(0, len(countryblocks))], [])

# Print out country codes list
fout = open('countrylist.csv', 'w')
for li in countrylis:
    ccode = li.a['href'][-7:-4]
    cname = li.text.encode('utf-8')
    fout.write('{},{}\n'.format(ccode, cname))
fout.close()

# grab all the pdf files
for li in countrylis:
    url = 'http://www.who.int' + li.a['href']
    fout = open('countrydata/' + url.split('/')[-1], 'w')
    print('Getting pdf from {}'.format(url))
    a = requests.get(url, stream=True)
    # Write out pdf in blocks
    for block in a.iter_content(512):
        if not block:
            break
        fout.write(block)

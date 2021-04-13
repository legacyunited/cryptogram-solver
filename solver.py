import requests
from bs4 import BeautifulSoup

# address for the cryptogram solver website
url = "http://rumkin.com/tools/cipher/cryptogram-solver.php"

# posting data to website
r = requests.post(url, data = {
    'dict': 'american-english-huge',
    'text': 'DL KBZ PVVM ZBDE LKBL EVXFROBRT DZ LKV CFOZL QFOZL QFOX FQ WFNVOMXVML VJRVGL BUU LKV FLKVOZ LKBL KBNV PVVM LODVE.'
}).text

# using bs4 to parse reponses

soup = BeautifulSoup(r, 'html.parser')
i = 0
for each in soup.findAll('div'):
    if i == 6:
        print(each.text)
    i += 1
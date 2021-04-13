import requests
from bs4 import BeautifulSoup

url = "http://rumkin.com/tools/cipher/cryptogram-solver.php"

r = requests.post(url, data = {
    'dict': 'american-english-huge',
    'text': 'DL KBZ PVVM ZBDE LKBL EVXFROBRT DZ LKV CFOZL QFOZL QFOX FQ WFNVOMXVML VJRVGL BUU LKV FLKVOZ LKBL KBNV PVVM LODVE.'
}).text

soup = BeautifulSoup(r, 'html.parser')
i = 0
for each in soup.findAll('div'):
    if i == 6:
        print(each.text)
    i += 1
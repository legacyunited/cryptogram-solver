import requests
from bs4 import BeautifulSoup

sample = 'DL KBZ PVVM ZBDE LKBL EVXFROBRT DZ LKV CFOZL QFOZL QFOX FQ WFNVOMXVML VJRVGL BUU LKV FLKVOZ LKBL KBNV PVVM LODVE.'

class solve_cryptogram:
    def solve(self, cryptogram):

        # address for the cryptogram solver website
        url = "http://rumkin.com/tools/cipher/cryptogram-solver.php"

        # posting data to website
        r = requests.post(url, data = {
            'dict': 'american-english-huge',
            'text': cryptogram
        }).text

        # using bs4 (beautifulsoup) to parse reponses

        soup = BeautifulSoup(r, 'html.parser')
        i = 0
        for each in soup.findAll('div'):
            if i == 6:
                return each.text
            i += 1

if __name__ == "__main__":
    test = solve_cryptogram()
    test.solve(sample)

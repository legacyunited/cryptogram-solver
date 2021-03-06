import requests
from bs4 import BeautifulSoup

sample = 'DL KBZ PVVM ZBDE LKBL EVXFROBRT DZ LKV CFOZL QFOZL QFOX FQ WFNVOMXVML VJRVGL BUU LKV FLKVOZ LKBL KBNV PVVM LODVE.'

class solve_cryptogram:
    def solve(self, cryptogram):

        if len(cryptogram) == 0 or not len(''.join(cryptogram.replace(' ',''))):
            return 'There is no text to decrypt.'

        # address for the cryptogram solver website
        url = "http://rumkin.com/tools/cipher/cryptogram-solver.php"

        # posting data to website
        try:
            r = requests.post(url, data = {
                'dict': 'american-english-huge',
                'text': cryptogram
            }).text
        except:
            return 'Sorry, do me again.'

        # using bs4 (beautifulsoup) to parse reponses
        soup = BeautifulSoup(r, 'html.parser')
        i = 0
        for each in soup.findAll('div'):
            if i == 6:

                res = each.text.splitlines()[1]

                if res == 'Sorry, no quotes found':
                    #print(res)
                    return 'You got bubub! Maybe, challenge us with a shorter cryptogram?'
                
                print(res)
                return res

            i += 1

if __name__ == "__main__":
    test = solve_cryptogram()
    test.solve(sample)
    test.solve('')
    test.solve(' ')

from requests_html import HTMLSession
from urllib.parse import quote
from random import randint
from time import sleep
import re


session = HTMLSession()
res = input()
a = 0
while res:
    try:
        url = 'https://scholar.google.com/scholar?start=' + str(a) + '&num=100&q=' + quote(res)
        print(a, quote(res))
        a += 20
        response = session.get(url)
        print(url)

        response.html.render()
        for result in response.html.find('.gs_ri'):
            title = result.find('.gs_rt', first=True).text
            print(title)
            print(next(iter(result.absolute_links)))
            f = result.find('.gs_a', first=True).text
            print(f)
            try:
                print((re.search("\d{4}", f)).group(0))
            except:
                print('?')
    except:
        url = 'https://scholar.google.com/scholar?start=' + str(a) + '&num=100&q=' + quote(res)
        print(a, quote(res))
        print(url)
        break
    sleep(randint(1, 10))

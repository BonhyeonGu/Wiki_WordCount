import pickle as pic

import requests
from bs4 import BeautifulSoup
import time
from random import uniform

def urlToSoup(url):
    while(True):
        try:
            req = requests.get(url)
            break
        except Exception as e:
            print("urlToSoup fail : %s"%(url))
            time.sleep(uniform(0.5, 1.5))
    soup = BeautifulSoup(req.text, 'lxml')
    return soup

def getPR0den(u):
    url = "https://en.wikipedia.org/w/index.php?title=Special:Search&limit=20&offset=0&ns0=1&search=" + u
    soup = urlToSoup(url)
    tag = soup.select_one('#mw-search-top-table > div.results-info > strong:nth-child(2)')
    if tag == None:
        return 0
    return int(tag.text.replace(',', ''))

if __name__ == "__main__":
    file_locale = './keyOnly0.pkl'
    start_point = 0
    
    with open(file_locale, 'rb') as f:
        keyOnly:list = pic.load(f)
    #with open(file_locale[:-4] + '_ret.pkl', 'rb') as f:
    #    ret:list = pic.load(f)
    #    start_point = len(ret) - 1
    ret = dict()

    for i in range(start_point, len(keyOnly)):
        ret[keyOnly[i]] = getPR0den(keyOnly[i])
        if i % 1000 == 0:
            print(i)
            with open(file_locale[:-4] + 'ret.pkl','wb') as f:
                pic.dump(ret, f)
    with open(file_locale[:-4] + 'ret.pkl','wb') as f:
        pic.dump(ret, f)

    print("end")
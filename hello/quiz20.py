import random
import urllib.request

from bs4 import BeautifulSoup
from urllib.request import urlopen


class Quiz20:

    def quiz20list(self) -> str: return None

    def quiz21tuple(self) -> str: return None

    def quiz22dict(self) -> str: return None

    def quiz23listcom(self) -> str:
        print('----------------legacy----------')
        a = []
        for i in range(5):
            a.append(i)
        print('----------------comprehension----------')
        a2 = [i for i in range(5)]
        print(a2)
        return None


    def quiz24zip(self) -> str:
        i = []
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc.read(), 'lxml') #html.parser vs lxml
        '''
        #print(soup.prettify())
        artists = soup.find_all('p', {"class": "artist"})
        # print(type(artists)) # <class 'b24.element.ResultSet'>
        artists = ([i.get_text() for i in artists])
        #print(type(artists))
        #print(''.join(i for i in artists))
        title = soup.find_all('p', {"class": "title"})
        title = ([j.get_text() for j in title])
        print(''.join(j for j in title))'''
        for i, j in enumerate(['artist', 'title']):
            print('\n\n\n'.join([i for i in self.abc(soup, j)]))
            print('*'*100)

        '''a = [i for i in self.abc(soup, 'p', 'class', 'artist')]
        a = [i for i in self.abc(soup, 'p', 'class', 'title')]
        a = self.abc(soup, 'p', 'class', 'artist')
        b = self.abc(soup, 'p', 'class', 'title')
        print(a, b)'''

        return None

    @staticmethod
    def abc(soup, d) -> str:
        a = soup.find_all('p', {'class': d})
        a = ([j.get_text() for j in a])
        #print(''.join(j for j in a))
        return a

    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        music = soup.find_all('div', {"class": "ellipsis rank01"})
        music = ([i.get_text() for i in music])
        print(''.join(i for i in music))

        return None

    def quiz28(self) -> str:
        return None

    def quiz29(self) -> str: return None



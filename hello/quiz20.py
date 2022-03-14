import random
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from hello.domains import my100, myRandom, members
from quiz00 import Quiz00


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

    def quiz24zip(self) -> {}:
        '''a = [i for i in self.abc(soup, 'p', 'class', 'artist')]
        a = [i for i in self.abc(soup, 'p', 'class', 'title')]
        a = self.abc(soup, 'p', 'class', 'artist')
        b = self.abc(soup, 'p', 'class', 'title')
        print(a, b)'''

        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc.read(), 'lxml')  # html.parser vs lxml
        ls1 = self.find_music(soup, 'title')
        ls2 = self.find_music(soup, 'artist')
        a = [i if i == 0 or i == 0 else i for i in range(1)]
        b = [i if i == 0 or i == 0 else i for i in []]
        c = [(i, j) for i, j in enumerate([])]
        d = {i: j for i, j in zip(ls1, ls2)}
        l = [i + j for i, j in zip(ls1, ls2)]
        # self.dict1(ls1, ls2)
        # self.dict2(ls1, ls2)
        # dt = {i: j for i, j in zip(ls1, ls2)}
        l = [i + j for i, j in zip(ls1, ls2)]
        l2 = dict(zip(ls1, ls2))
        d1 = dict(zip(ls1, ls2))
        print(d1)
        return d1
        # self.dict1(ls1, ls2)
        # self.dict2(ls1, ls2)
        # self.dict3(ls1, ls2)

    @staticmethod
    def dict3(ls1, ls2)-> None:
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)

    @staticmethod
    def dict2(ls1, ls2) -> None:
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)

    @staticmethod
    def dict1(ls1, ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            dict[ls1[i]] = ls2[i]
        print(dict)

    def find_rang(self, soup) -> None:
        for i, j in enumerate(['artist', 'title']):
            for i, j in self.find_music(soup, j):
                print(f'{i}위 : {j}')
            print('*'*100)

    @staticmethod
    def print_music_list(soup)-> None:
        # print(soup.prettify())
        artists = soup.find_all('p', {"class": "artist"})
        # print(type(artists)) # <class 'b24.element.ResultSet'>
        artists = ([i.get_text() for i in artists])
        # print(type(artists))
        # print(''.join(i for i in artists))
        title = soup.find_all('p', {"class": "title"})
        title = ([j.get_text() for j in title])
        print(''.join(j for j in title))

    @staticmethod
    def find_music(soup, cls_name) -> []:
        ls = soup.find_all('p', {'class': cls_name})
        return [j.get_text() for j in ls]
        #print(''.join(j for j in a))

    @staticmethod
    def quiz25dictcom() -> {}:
        a = Quiz00
        students = set([a.quiz06member_Choice() for i in range(5)])
        scores = [myRandom(0, 100) for i in range(5)]
        while len(students) < 5:
            students.add(a.quiz06member_Choice())
        student = list(students)
        res = dict(zip(student, scores))
        print({i : j for i, j in zip(student, scores)})

        return {i : j for i, j in zip(student, scores)}

    def quiz26map(self) -> None: return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        ls1 = self.find(soup, 'ellipsis rank01')
        ls2 = self.find(soup, 'ellipsis rank02')
        a = dict(zip(ls1, ls2))
        print(a)
        return a


    @staticmethod
    def find(soup, cls_name) -> []:

        ls = soup.find_all('div', {"class": cls_name})
        return [i.get_text() for i in ls]

    def quiz28dataframe(self) -> None:
        dict = self.quiz24zip()
        df = pd.DataFrame.from_dict(dict, orient='index')
        print(df)
        df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')

    '''
    다음 결과 출력
        a   b   c
    1   1   3   5
    2   2   4   6
    '''

    def quiz29_pandas(self) -> object:
        d1 = {'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}
        df1 = pd.DataFrame(d1, index =[1, 2])
        print(df1)
        '''
        a  b  c
    1  1  3  5
    2  2  4  6
        '''
        d2 = {"1":[1, 3, 6], "2": [2, 4, 6]}
        df2 = pd.DataFrame.from_dict(d2)
        print(df2)
        '''
           1  2
        0  1  2
        1  3  4
        2  6  6        
        '''
        df3 = pd.DataFrame.from_dict(d2, orient='index', columns=['a', 'b', 'c'])
        print(df3)

        odds = []
        evens = []
        columns = [chr(i) for i in range(97,100)]       # c =  ['a', 'b', 'c']
        [odds.append(i) if i%2 ==0 else evens.append(i) for i in range(1, 7)]
        dict = {'1': evens,'2': odds}
        df4 = pd.DataFrame.from_dict(dict, orient= 'index', columns=columns)
        '''
           a  b  c
        1  1  3  5
        2  2  4  6
        '''
        print(df4)
        return None

    def quiz29dataframe(self) -> None:
        dict = self.quiz27melon()
        df = pd.DataFrame.from_dict(dict, orient='index')
        print(df)
        df.to_csv('./save/melon.csv', sep=',', na_rep='NaN')



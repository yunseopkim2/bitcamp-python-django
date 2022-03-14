import random
import string

import numpy as np
import pandas as pd
from icecream import ic

from hello.domains import myRandom


class Quiz30:
    '''
           데이터프레임 문제 Q02
       ic| df:     A   B   C
               1   1   2   3
               2   4   5   6
               3   7   8   9
               4  10  11  12
       '''

    ''' aa=[]

            [aa.append(i) if i==3 or i==6 or i ==9 else aa.append(i)  for i in range(1,12)]
            dict = [aa]
            df = pd.DataFrame.(dict, index=range(1, 5), columns=['A', 'B', 'C'])

            # 위 식을 리스트결합 형태로 분해해서 조립하시오
            ic(df)
            return None
        '''

    def quiz30_df_4_by_3(self) -> object:
        '''l1 = [range(1, 4)]
        l2 = [range(4, 7)]
        l3 = [range(7, 10)]
        l4 = [range(10, 13)]'''
        d ={'1' : range(1, 4),
            '2': range(4, 7),
            '3': range(7, 10),
            '4': range(10, 13)}
        df2 = pd.DataFrame.from_dict(d, orient='index', columns=['A', 'B', 'C'])
        ic(df2)


        return None


    '''
        데이터프레임 문제 Q03.
        두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
        ic| df:     0   1   2
                0  97  57  52
                1  56  83  80
    '''

    def quiz31_rand_2_by_3(self) -> object:
        a=  [[myRandom(10 ,100) for i in range(3)] for i in range(2)]
        a1=  pd.DataFrame(np.random.randint(10, 100 , size=(2,3))) # 넘파일을 사용한 매체
        '''l1 = [i for i in range(2)]
        columns = [i for i in range(3)]
        df = pd.DataFrame(a, index=l1, columns=columns)'''
        # df = pd.DataFrame({})
        # df = pd.DataFrame({}, columns={})
        # df = pd.DataFrame({}, index={}, columns={})
        df = pd.DataFrame(a1)
        print(df)
        return None

    '''
                데이터프레임 문제 Q04.
                국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성.
                 단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기

                  ic| df4:        국어  영어  수학  사회
                            lDZid  57  90  55  24
                            Rnvtg  12  66  43  11
                            ljfJt  80  33  89  10
                            ZJaje  31  28  37  34
                            OnhcI  15  28  89  19
                            claDN  69  41  66  74
                            LYawb  65  16  13  20
                            QDBCw  44  32   8  29
                            PZOTP  94  78  79  96
                            GOJKU  62  17  75  49
    '''
    @staticmethod
    def id(chr_size) -> str:
        return ''.join([random.choice(string.ascii_letters) for i in range(chr_size)])

    @staticmethod
    def grade(scores) -> []:
        return [myRandom(0, 100) for i in range(scores)]

    def quiz32_df_grade(self) -> object:
        col = ['국어', '영어', '수학', '사회']
        grade = [self.grade(scores=4) for i in range(10)]
        id = [self.id(chr_size=5) for i in range(10)]
        grade1 = np.random.randint(0,100 ,(10,4))
        dict1 = dict(zip(id, grade1))
        df1 = pd.DataFrame.from_dict(dict1, orient='index', columns=col)
        df2 = pd.DataFrame(grade1, index=id, columns=col)
        ic(df1)
        ic(df2)

        return None

    def quiz33(self) -> str: return None

    def quiz34(self) -> str: return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None
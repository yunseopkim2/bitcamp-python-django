import random

from hello import Member
from hello.domains import my100, myRandom, members


class Quiz00:
    def quiz00calculator(self) -> float:

        a = my100()
        b = my100()
        o = ['+', '-', '*', '/', '%']
        # lise : indexing
        res = o[myRandom(0, 5)]

        if res == '+':
            result = self.add(a, b)
        elif res == '-':
            result = self.sub(a, b)
        elif res == '*':
            result = self.mul(a, b)
        elif res == '/':
            result = self.div(a, b)
        elif res == '%':
            result = self.mod(a, b)

        return print(f'{a} {res} {b} = {result}')

    def add(self, a, b) -> float:
        return a + b

    def sub(self, a, b) -> float:
        return a - b

    def mul(self, a, b) -> float:
        return a * b

    def div(self, a, b) -> float:
        return a / b

    def mod(self, a, b) -> float:
        return a % b

    def quiz01bmi(member):
        this = Member()
        this.name = members()[myRandom(0, 23)]
        this.height = myRandom(150, 190)
        this.weight = myRandom(40, 100)
        bmi = this.weight / (this.height * this.height) * 10000
        if bmi >= 30:
            res = '고도비만'
        elif bmi > 25:
            res = '비만'
        elif bmi > 23:
            res = '과체중'
        elif bmi > 18.5:
            res = '정상'
        else:
            res = '저체중'
        print(f'{this.name} 키:{this.height}cm 몸무게:{this.weight}kg BMI결과:{res}')
        return None
    def quiz02dice(self):
        print(myRandom(1, 6))
        return None

    def quiz03rps(self):
        c = myRandom(1, 3)
        p = myRandom(1, 3)
        # 1 가위 2  바위 3 보
        rps = ['가위', '바위', '보']
        print(' ----------- 1 ------------')
        if p == 1:
            if c == 1:
                res = f'플레이어:{rps[0]}, 컴퓨터:{rps[0]}, 결과: 무승부'
            elif c == 2:
                res = f'플레이어:{rps[0]}, 컴퓨터:{rps[1]}, 결과: 패배'
            elif c == 3:
                res = f'플레이어:{rps[0]}, 컴퓨터:{rps[2]}, 결과: 승리'
        elif p == 2:
            if c == 1:
                res = f'플레이어:{rps[1]}, 컴퓨터:{rps[0]}, 결과: 승리'
            elif c == 2:
                res = f'플레이어:{rps[1]}, 컴퓨터:{rps[1]}, 결과: 무승부'
            elif c == 3:
                res = f'플레이어:{rps[1]}, 컴퓨터:{rps[2]}, 결과: 패배'
        elif p == 3:
            if c == 1:
                res = f'플레이어:{rps[2]}, 컴퓨터:{rps[0]}, 결과: 패배'
            elif c == 2:
                res = f'플레이어:{rps[2]}, 컴퓨터:{rps[1]}, 결과: 승리'
            elif c == 3:
                res = f'플레이어:{rps[2]}, 컴퓨터:{rps[2]}, 결과: 무승부'
        print(f'플레이어는 {rps[p - 1]} 컴퓨터는 {rps[c - 1]} 결과는 {res}')
        print(' ----------- 2 ------------')
        if p == c:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:무승부'
        elif p - c == 1 or p - c == -2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:승리'
        elif p - c == -1 or p - c == 2:
            res = f'플레이어:{rps[p - 1]}, 컴퓨터:{rps[c - 1]}, 결과:패배'
        else:
            res = '1~3 입력'
        print(res)

    def quiz04leap(self):
        y = myRandom(2000, 2022)
        '''
        s1 = '윤년' if y % 4 == 0 and y %100 != 0 else '평년'
        s2 = '윤년' if y % 400 == 0 else '평년'
        Java = 
        String s;
        (if y % 4 == 0 && y % 100 != 0 ) ? "윤년" : (y % 400 == 0) ? "윤년" : "평년" ;
        '''
        s = '윤년' if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 else "평년"
        print(f'{y}년은 {s}니다.')
        pass

    def quiz05grade(self):
        name = members()[myRandom(0, 23)]
        kor = myRandom(0, 100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        sum = self.sum(kor, eng, math)
        avg = self.avg(kor, eng, math)
        grade = self.grade(kor, eng, math)
        passChk = self.passChk(kor, eng, math)
        print(f'이름:{name} \n'
              f'국어:{kor}점 영어:{eng}점 수학:{math}점 \n'
              f'총점:{sum}점 \n'
              f'평균:{avg}점 \n'
              f'등급:{grade} \n'
              f'합/불:{passChk}')
        return None

    def sum(self, kor, eng, math):
        return kor + eng + math

    def avg(self, kor, eng, math):
        return (kor + eng + math) / 3

    def grade(self, kor, eng, math):
        if (self.avg(kor, eng, math)) >= 90:
            return 'A등급'
        elif (self.avg(kor, eng, math)) >=80:
            return 'B등급'
        elif (self.avg(kor, eng, math)) >=70:
            return 'C등급'
        elif (self.avg(kor, eng, math)) >=60:
            return 'D등급'
        else:
            return 'F등급'

    def passChk(self,kor,eng,math):  # 60점이상이면 합격
        if (self.avg(kor,eng,math)) >= 60:
            return '합격'
        else:
            return '불합격'

    @staticmethod
    def quiz06member_Choice():
        print(members()[myRandom(0, 23)])
        return members()[myRandom(0, 23)]

    def quiz07lotto(self):

        numbers = ','.join(str(random.randint(1, 45)) for i in range(6))
        print(numbers)
        pass

    def quiz08bank(self):  # 이름, 입금, 출금만 구현

        #의존관계 형성 (메소드 안에서)a = Account()

        Account.main()


    def quiz09gugudan(self):  # 책받침구구단

        pass


'''
은행이름은 비트은행
입급자 이름(name), 계좌번호(account_number), 금액(money) 속성값으로 계좌를 생성한다.
계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성된다.
금액은 100 - 999 사이로 랜덤하게 입금된다. (단위는 만단위로 암묵적으로 판단한다) 
'''


class Account(object):
    def __init__(self, name, account_number, money):
        self.BANK_NAME = '비트은행'
        self.name = members()[myRandom(0, 23)] if name == None else name
        #self.account_number = f'{myRandom(0, 999):0>3}-{myRandom(0, 99):0>2}-{myRandom(0, 999999):0>6}'
        self.account_number = self.creat_account_number() if account_number == None else account_number
        self.money = myRandom(100, 999) if money == None else money

    def to_string(self):
        return f'은행: {self.BANK_NAME} ' \
               f'입금자: {self.name} ' \
               f'계좌번호: {self.account_number} ' \
               f'금액: {int(self.money)}만원'

    @staticmethod
    def creat_account_number():
        '''
        ls = [str(myRandom(0, 9)) for i in range(3)]
        ls.append('-')
        ls += [str(myRandom(0, 9)) for i in range(2)]
        ls.append('-')
        ls += [str(myRandom(0, 9)) for i in range(6)]
        return ''.join(ls) '''

        #return ''.join([str(myRandom(0, 9)) if i != 3 and i != 6 else '-' for i in range(13)])

        return  ''.join(['-' if i == 3 or i == 6 else str(myRandom(0, 9)) for i in range(13)])

    @staticmethod
    def find_account(ls, account_number):

       # return ''.join([ j.to_string() if j.account_number == account_number else '찾는 계좌 아님' for i, j in enumerate(ls)])

       ''' for i, j in enumerate(ls):
            if j.account_number == account_number:
                 print(j.to_string()) '''

       for i, j in enumerate(ls):
           if j.account_number == account_number:
               a = ls[i]

       return a

    @staticmethod
    def del_account(ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]

    @staticmethod
    def add_account(ls, account_number, add):

        for i, j in enumerate(ls):
            if j.account_number == account_number:
                ls[i].money += int(add)
                return ls[i]

    @staticmethod
    def withdraw_account(ls, account_number, withdraw):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                ls[i].money -= int(withdraw)
                return ls[i]

    @staticmethod
    def main():

        ls = []
        while 1 :
            menu = input('0.exit 1.계좌개설 2. 계좌목록 3.입급 4.출금 5.계좌해지 6.계좌조회')
            if menu == '0':
                break
            if menu == '1':
                acc = Account(None, None, None)
                print(f'{acc.to_string()}... 개설되었습니다.')
                ls.append(acc)

            elif menu == '2':

                a = '\n'.join(i.to_string() for i in ls)
                print(a)

            elif menu == '3':
                a = Account.add_account(ls, input('입금할 계좌번호 입력'), input('입금액'))
                print(a.to_string())

                '''account_number = input('입금할 계좌번호')
                deposit = input('입급액')
                for i, j in enumerate(ls):
                    if j.account_number == account_number:
                        pass'''
            elif menu == '4':

                a = Account.withdraw_account(ls, input('출금할 계좌번호'), input('출금액'))
                print(a.to_string())

            elif menu == '5':
                Account.del_account(ls, input('탈퇴할 계좌번호'))

            elif menu == '6':
                print(Account.find_account(ls, input('조회할 계좌번호')))

            else:
                print('Wrong Number.. Try Again')
                continue



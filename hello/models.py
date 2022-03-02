import random
import statistics


def main():
    while 1:
        menu = input('0.Exit 1.계산기(+,-,*,/) 2.BMI 3.성적표 4.오토성적표 5.주사위' )
        if menu == '0':
            print('종료')
            break
        elif menu == '1': #계산기
            # 객체생성
            q1 = Quiz01Calculator(int(input('첫번째 수')),input('연산자'), int(input('두번째 수')))
            print('*'*30)
            print(f'{q1.num1} {q1.opcode} {q1.num2} = {q1.calc()}')
        elif menu == '2': #BMI
            q2 = Quiz02Bmi(input('이름 입력'), int(input('키 입력(cm)')), int(input('몸무게 입력(kg)')))
            print('*'*30)
            print(f'{q2.name}님의 BMI 결과는 {q2.bmi()}입니다')
        elif menu == '3': #Grade
            q3 = Quiz03Grade(input('이름 입력'), int(input('국어 점수')), int(input('영어 점수')), int(input('수학 점수')))
            print('*'*15 + '성적표' + '*'*15 + '\n' +
                f' 이름: {q3.name}\n' +
                f'> 국어: {q3.kor}점 \n' +
                f'> 영어: {q3.eng}점 \n' +
                f'> 수학: {q3.math}점\n' +
                f' 총점: {q3.total()}점 \n' +
                f' 평균: {q3.avg()}점\n' +
                f' 합격여부: {q3.chkPass()}\n' +
                '*'*35)
        elif menu == '4':
            name = input('이름 입력')
            kor = int(input('국어 점수'))
            eng = int(input('영어 점수'))
            math = int(input('수학 점수'))
            q4 = Quiz04AutoGrade(name, kor, eng, math)
            print('*' * 15 + '성적표' + '*' * 15 + '\n' +
                  f' 이름: {q4.name}\n' +
                  f'> 국어: {q4.kor}점 \n' +
                  f'> 영어: {q4.eng}점 \n' +
                  f'> 수학: {q4.math}점\n' +
                  f' 총점: {q4.total()}점 \n' +
                  f' 평균: {q4.avg()}점\n' +
                  f' 합격여부: {q4.chkPass()}\n' +
                  '*' * 35)
        elif menu == '5':
            print(f'{Quiz05Dice.cast()}')
        elif menu == '6':
            q6 = Quiz06RandomGenerator()
            print(f'{q6.random()}')
        elif menu == '7':
            q7 = Quiz07RandomChoice()
            q7.chooseMember()
        elif menu == '8':
            q8 = Quiz08Rps(1) # 1 가위 2 바위 3 보
            print(q8.game())
        elif menu == '9':
            q9 = Quiz09GetPrime()
        elif menu == '7':
            q10 = Quiz10LeapYear()
        elif menu == '7':
            q11 = Quiz11NumberGolf()
        elif menu == '7':
            q12 = Quiz12Lotto()
        elif menu == '7':
            q13 = Quiz13Bank()
        elif menu == '7':
            q14 = Quiz14Gugudan()
        else:
            print('0~14 입력')


class Quiz01Calculator:

    def __init__(self, num1, opcode, num2):
        self.num1 = num1
        self.opcode = opcode
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

    def calc(self):
        if self.opcode == '+':
            return self.add()
        elif self.opcode == '-':
            return self.sub()
        elif self.opcode == '*':
            return self.mul()
        elif self.opcode == '/':
            return self.div()


class Quiz02Bmi:

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        bmiResult = self.weight / (self.height*self.height) * 10000
        if bmiResult >= 35:
            return f'고도 비만'
        elif bmiResult >= 30:
            return f'중(重)도 비만 (2단계 비만)'
        elif bmiResult >= 25:
            return f'경도 비만 (1단계 비만)'
        elif bmiResult >= 23:
            return f'과체중'
        elif bmiResult >= 18.5:
            return f'정상'
        else:
            return f'저체중'


class Quiz03Grade:

    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def total(self):
        return (self.kor + self.eng + self.math)

    def avg(self):
        return (self.kor + self.eng + self.math) / 3

    def chkPass(self):
        if (self.avg()) >= 60:
            return f'합격'
        else:
            return f'불합격'


class Quiz04AutoGrade:

    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def total(self):
        return (self.kor + self.eng + self.math)

    def avg(self):
        return (self.kor + self.eng + self.math) / 3

    def chkPass(self):
        if self.avg() >= 60:
            return f'합격'
        else:
            return f'불합격'


def myRandom(start, end):
    return random.randint(start, end)


class Quiz05Dice(object):
    @staticmethod
    def cast():
        return random.randint(1,6)


class Quiz06RandomGenerator(object): # 원하는 범위의 정수에서 랜덤값 1개 추출
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def random(self):
        return myRandom(self.start, self.end)


class Quiz07RandomChoice(object):

    def __init__(self): # 803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜' , '권솔이', '김지혜' , '하진희' , '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종"]

    def chooseMember(self):
        return self.members[myRandom(0, 23)]


class Quiz08Rps(object):

    def __init__(self, player):
        self.player = player
        self.computer = myRandom(1, 3)

    def game(self):
        #1 가위 2 바위 3 보
        c = self.computer
        p = self.player
        rps = ['가위', '바위', '보']
        if p == 1:
            if c == 1: res = f'플레이어:{rps[0]}, 컴퓨터:{rps[0]}, 결과: 무승부'
            elif c == 2: res = f'플레이어:{rps[0]}, 컴퓨터:{rps[1]}, 결과: 패배'
            elif c == 3: res = f'플레이어:{rps[0]}, 컴퓨터:{rps[2]}, 결과: 승리'
        elif p == 2:
            if c == 1: res = f'플레이어:{rps[1]}, 컴퓨터:{rps[0]}, 결과: 승리'
            elif c == 2: res = f'플레이어:{rps[1]}, 컴퓨터:{rps[1]}, 결과: 무승부'
            elif c == 3: res = f'플레이어:{rps[1]}, 컴퓨터:{rps[2]}, 결과: 패배'
        elif p == 3:
            if c == 1: res = f'플레이어:{rps[2]}, 컴퓨터:{rps[0]}, 결과: 패배'
            elif c == 2: res = f'플레이어:{rps[2]}, 컴퓨터:{rps[1]}, 결과: 승리'
            elif c == 3: res = f'플레이어:{rps[2]}, 컴퓨터:{rps[2]}, 결과: 무승부'
        else: res = '1~3 입력'
        return res
class Quiz09GetPrime(object):
    def __init__(self):
        pass
class Quiz10LeapYear(object):
    def __init__(self):
        pass
class Quiz11NumberGolf(object):
    def __init__(self):
        pass
class Quiz12Lotto(object):
    def __init__(self):
        pass
class Quiz13Bank(object): # 이름, 입금, 출금만 구현
    def __init__(self):
        pass
class Quiz14Gugudan(object): # 책받침구구단
    def __init__(self):
        pass


if __name__ == '__main__':
    main()
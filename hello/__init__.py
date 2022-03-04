from hello.domains import Member
from models import Quiz01Calculator, Quiz02Bmi, Quiz03Grade, Quiz04GradeAuto, Quiz05Dice, Quiz07RandomChoice, \
    Quiz08Rps, Quiz09GetPrime, Quiz10LeapYear, Quiz11NumberGolf, Quiz12Lotto, Quiz13Bank, Quiz14Gugudan, Quiz04AutoGrade
from hello.domains import Member
from hello.quiz00 import Quiz00
from hello.quiz10 import Quiz10
from hello.quiz20 import Quiz20
from hello.quiz30 import Quiz30
from hello.quiz40 import Quiz40


if __name__ == '__main__':
    q0 = Quiz00()
    q1 = Quiz10()
    q2 = Quiz20()
    q3 = Quiz30()
    q4 = Quiz40()
    while 1:
        menu = input("00계산기 01Bmi 02주사위 03가위바위보 04윤년 05성적표 06멤버선택 07로또 08입출금 09구구단"
                     "10버블 11삽입 12선택 13퀵 14병합 15매직 16지그재그 17직각별 18정삼각별 19예약"
                     "20리스트 21튜플 22딕셔너리 23 24 25 26 27 28 29"
                     "30 31 32 33 34 35 36 37 38 39")
        if menu == '00':
            q0 = Quiz01Calculator(int(input('첫번째 수')), int(input('두번째 수')))
            print(f'{q0.num1} + {q0.num2} = {q0.add()}')
        elif menu == '01':
            member = Member()
            q1 = Quiz02Bmi()
            member.name = input('이름 : ')
            member.height = float(input('키 : '))
            member.weight = float(input('몸무게 : '))
            res = q1.getBmi(member)
            print(f'이름: {member.name}, 키: {member.height}, '
                  f'몸무게: {member.weight}, BMI상태: {res} ')
        elif menu == '02':
            q2 = Quiz05Dice()
            print(q2.cast())
        elif menu == '03':

            q3 = Quiz08Rps(int(input('1. 가위 2. 바위 3. 보')))
            print(q3.game())
        elif menu == '04':
            q0.quiz04leap()
        elif menu == '05':
            q5 = Quiz03Grade(input('이름 입력'), int(input('국어 점수')), int(input('영어 점수')), int(input('수학 점수')))
            print('*' * 15 + '성적표' + '*' * 15 + '\n' +
                  f' 이름: {q5.name}\n' +
                  f'> 국어: {q5.kor}점 \n' +
                  f'> 영어: {q5.eng}점 \n' +
                  f'> 수학: {q5.math}점\n' +
                  f' 총점: {q5.total()}점 \n' +
                  f' 평균: {q5.avg()}점\n' +
                  f' 합격여부: {q5.chkPass()}\n' +
                  '*' * 35)
        elif menu == '06':

            q6 = Quiz07RandomChoice()
            print(q6.chooseMember())
        elif menu == '07':
            q0.quiz07lotto()
        elif menu == '08':
            q0.quiz08bank()
        elif menu == '09':
            q0.quiz09gugudan()
        elif menu == '10':
            q1.quiz10bubble()
        elif menu == '11':
            q1.quiz11insertion()
        elif menu == '12':
            q1.quiz12selection()
        elif menu == '13':
            q1.quiz13quick()
        elif menu == '14':
            q1.quiz14merge()
        elif menu == '15':
            q1.quiz15magic()
        elif menu == '16':
            q1.quiz16zigzag()
        elif menu == '17':
            q1.quiz17star()
        elif menu == '18':
            q1.quiz18triangle()
        elif menu == '19':
            q1.quiz19booking()
        elif menu == '20':
            q2.quiz20list()
        elif menu == '21':
            q2.quiz21tuple()
        elif menu == '22':
            q2.quiz22dict()
        elif menu == '23':
            q2.quiz23listcom()
        elif menu == '24':
            q2.quiz24zip()
        elif menu == '25':
            q2.quiz25dictcom()
        elif menu == '26':
            q2.quiz26map()
        elif menu == '27':
            q2.quiz27()
        elif menu == '28':
            q2.quiz28()
        elif menu == '29':
            q2.quiz29()
        elif menu == '30':
            q2.quiz30()
        elif menu == '31':
            q2.quiz31()
        elif menu == '32':
            q2.quiz32()
        elif menu == '33':
            q2.quiz33()
        elif menu == '34':
            q2.quiz34()
        elif menu == '35':
            q2.quiz35()
        elif menu == '36':
            q2.quiz36()
        elif menu == '37':
            q2.quiz37()
        elif menu == '38':
            q2.quiz38()
        elif menu == '39':
            q2.quiz39()
        elif menu == '40':
            q4.quiz40()
        elif menu == '41':
            q4.quiz41()
        elif menu == '42':
            q4.quiz42()
        elif menu == '43':
            q4.quiz43()
        elif menu == '44':
            q4.quiz44()
        elif menu == '45':
            q4.quiz45()
        elif menu == '46':
            q4.quiz46()
        elif menu == '47':
            q4.quiz47()
        elif menu == '48':
            q4.quiz48()
        elif menu == '49':
            q4.quiz49()
        else:
            break




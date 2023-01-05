'''
import pandas as pd
import numpy as np
'''

# student 딕셔너리 생성(전역변수)
student = dict()

# ----- 성적 입력 -----
def Insert(student):
    num = input('학번 : ')

    if (num.isnumeric()):
        num = int(num)
        # 학번이 일의 자리일 경우
        if (0 < num < 10):

            # 학번이 딕셔너리 내에 없을경우,
            if (num not in student) == True:

                while True:
                    # 성적 입력값이 문자열일 경우와 0~100 아닐 경우 다시 입력 받기
                    kor = input('%d의 국어 점수 : ' % num)
                    if (kor.isnumeric()):
                        kor = int(kor)

                        if (kor < 0) or (kor > 100) :
                            print('--> 정수 0~100을 입력하시오.')
                            continue
                    else:
                        print('--> 정수 0~100을 입력하시오.')
                        continue

                    math = input('%d의 수학 점수 : ' % num)
                    if (math.isnumeric()) :
                        math = int(math)

                        if (math < 0) or (math > 100):
                            print('--> 정수 0~100을 입력하시오.')
                            continue

                    else:
                        print('--> 정수 0~100을 입력하시오.')
                        continue

                    eng = input('%d의 영어 점수 : ' % num)
                    if (eng.isnumeric()):
                        eng = int(eng)

                        if (eng < 0) or (eng > 100):
                            print('--> 정수 0~100을 입력하시오.')
                            continue

                    else:
                        print('--> 정수 0~100을 입력하시오.')
                        continue
                    
                    save = input('%d의 점수를 저장하시겠습니까?(y/n)' % num)

                    if save == 'y':
                        score = kor + eng + math
                        avg = round(score/3,3)
                        print('학생(%d)의 점수 합계는 %d점, 평균은 %d입니다.' % (num, score, avg))

                        if 90 <= avg:
                            grade = 'A'

                        elif 80 <= avg < 90:
                            grade = 'B'

                        elif 70 <= avg < 80:
                            grade = 'C'

                        elif 60 <= avg < 70:
                            grade = 'D'

                        else:
                            grade = 'F'

                        # 딕셔너리 Key = Value
                        student[num] = [kor, eng, math, score, avg, grade]
                        person = student[num]
                        return student

                    elif save == 'n':
                        print('학생(%d)의 정보가 입력되지 않습니다.' % num)
                        return main()

                    else:
                        return main()

            # 학번이 중복일 경우
            else:
                print('%d은(는) 성적이 존재하는 학생입니다' % num)
                return main()

        # 학번이 일의 자리가 아닐 경우
        else:
            print("-->'%d'는 입력할 수 없습니다." % num)
            return main()

    # 학번이 숫자가 아닐 경우
    else:
        print("-->'%s'는 입력할 수 없습니다." % num)
        return main()

# ----- 성적 현황 -----
def View(student):
    print("="*37)
    print('학번 : [국어, 영어, 수학, 총점, 평균, 환산]')

    # 딕셔너리 key, value 출력하기(item)
    for key, value in sorted(student.items(), key = lambda x: x[0]):
        print(key, ':', value)

    #최고 점수
    for key, value in sorted(student.items(), key=lambda x: x[1], reverse=True):
        print('최고 점수', student[0][0], student[0][1], student[0][3])

    #최저 점수
    for key, value in sorted(student.items(), key=lambda x: x[1]):
        print('최저 점수',student[0][0], student[0][1], student[0][3])

    print("="*37)

def main():
    # 전역 변수
    global student

    print('='*37)
    print('='*2, '피식 고등학교 성적처리 프로그램', '='*2)
    print('='*37)
    print('<< 메뉴 >>')
    print('1. 성적입력')
    print('2. 성적현황')
    print('3. 종료')
    print('='*37)

    while True:
        select = int(input(">>"))

        # ----- 성적 입력 -----
        if select == 1:
            print('='*37)
            print('학생 성적 입력')
            print('='*37)
            student = Insert(student)

        # ----- 성적 현황 -----
        elif select == 2:
            print('='*37)
            print('학생 성적 현황')
            print('='*37)
            student = View(student)

        # ----- 프로그램 종료 -----
        elif select == 3:
            print('(프로그램 종료 - 개발자 : 20223175 문정은)')
            break

main()
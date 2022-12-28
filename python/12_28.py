import pandas as pd
import numpy as np
# ----- 성적 입력 -----
def Insert(student):
    num = int(input('학번 : '))

    #학번이 딕셔너리 내에 없을경우,
    if (num not in student) == True:

        #성적 입력
        kor =  int(input('%d의 국어 점수 : '%num))
        math =  int(input('%d의 수학 점수 : '%num))
        eng = int(input('%d의 영어 점수 : '%num))
        save = input('%d의 점수를 저장하시겠습니까?'%num)

        if save == 'y' :
            score = kor+eng+math
            avg = round(score/3, 3)
            print('학생(%d)의 점수 합계는 %d점, 평균은 %d입니다.'%(num,score,avg))
        else :
            return main()

    #학번이 중복일 경우
    else:
        print('%d은(는) 성적이 존재하는 학생입니다')
        return main()
        

    #딕셔너리 Key = Value
    student[num] = [kor, eng, math, score, avg]
    person = student[num]
    return student


# ----- 성적 현황 -----
def View(student):
    print("="*33)
    print('학번 : [국어, 영어, 수학, 총점, 평균]')

    
    # 딕셔너리 key, value 출력하기(item)
    for key, value in student.items():
        print(key,':', value)
    print("="*33)
        
    return student

def main():

    # student 딕셔너리 생성
    student = dict()
    print('='*33)
    print('='*2, '피식 고등학교 성적처리 프로그램', '='*2)
    print('='*33)
    print('<< 메뉴 >>')
    print('1. 성적입력')
    print('2. 성적현황')
    print('3. 종료')
    print('='*33)

    while True:
        select = int(input(">>"))

        # ----- 성적 입력 -----
        if select == 1:
            print('='*33)
            print('학생 성적 입력')
            print('='*33)
            student = Insert(student)

        # ----- 성적 현황 -----
        elif select == 2:
            print('='*33)
            print('학생 성적 현황')
            print('='*33)
            student = View(student)
            
        else:
            print('(프로그램 종료 - 개발자 : 20223175 문정은)')
            break

main()
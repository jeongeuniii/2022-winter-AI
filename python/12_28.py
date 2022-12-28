import pandas as pd

# ----- 성적 입력 -----
def Insert(student):
    num = int(input('학번 : '))

    #학번이 데이터프레임 내에 없을경우,
    if (num not in student) == True:

        #성적 입력
        kor =  int(input('%d의 국어 점수 : '%num))
        math =  int(input('%d의 수학 점수 : '%num))
        eng = int(input('%d의 국어 점수 : '%num))
        print('성적이 입력되었습니다.')

        score = kor+eng+math
        avg = round(score/3, 3)

    #학번이 중복일 경우
    else:
        print('%d은(는) 성적이 존재하는 학생입니다')
        return Insert(student)
        

    #딕셔너리 Key = Value
    student[num] = [kor, eng, math, score, avg]
    person = student[num]
    return student


# ----- 성적 현황 -----
def View(student):
    print("="*33)
    print('점수 : [국, 영, 수, 총점, 평균]')

    
    # 딕셔너리 key, value 출력하기(item)
    for key, value in student.items():
        print(key,':', value)
    print("=======================================================")
        
    return student

def main():

    # student 데이터프레임 생성
    student = pd.DataFrame()
    print('='*33)
    print('='*2, '피식 고등학교 성적처리 프로그램', '='*2)
    print('='*33)
    while True:
        print('<< 메뉴 >>')
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
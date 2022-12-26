print("="*33)
print("="*8, "20223175 문정은", "="*8)
print("="*8, "1주차 과제 결과", "="*8)
print("="*33)

mon = int(input("'월'(1~12)입력 :"))
date = int(input("'일'(1~31)입력 :"))

if 0 < mon <= 12:
    if mon == 1:
        if date == 6:
            print("입력하신", mon,"월", date,"일은","'소한'입니다.")
        elif date == 21:
            print("입력하신", mon,"월", date,"일은","'대한'입니다.")
        elif date > 31:
            print("입력하신", mon,"월", date,"일은 일수를 잘못 입력하셨습니다.")
        else:
            print("입력하신", mon,"월", date,"일의 절기를 알 수 없습니다.")

    elif mon == 2:
        if date == 4:
            print("입력하신", mon,"월", date,"일은","'입춘'입니다.")
        elif date == 19:
            print("입력하신", mon,"월", date,"일은","'우수'입니다.")
        elif date >= 29:
            print("입력하신", mon,"월", date,"일은 일수를 잘못 입력하셨습니다.")
        else:
            print("입력하신", mon,"월", date,"일의 절기를 알 수 없습니다.")

    elif mon == 3:
        if date == 6:
            print("입력하신", mon,"월", date,"일은","'경칩'입니다.")
        elif date == 21:
            print("입력하신", mon,"월", date,"일은","'춘분'입니다.")
        elif date > 31:
            print("입력하신", mon,"월", date,"일은 일수를 잘못 입력하셨습니다.")
        else:
            print("입력하신", mon,"월", date,"일의 절기를 알 수 없습니다.")

    elif mon == 4:
        if date == 5:
            print("입력하신", mon,"월", date,"일은","'청명'입니다.")
        elif date == 20:
            print("입력하신", mon,"월", date,"일은","'곡우'입니다.")
        elif date > 30:
            print("입력하신", mon,"월", date,"일은 일수를 잘못 입력하셨습니다.")
        else:
            print("입력하신", mon,"월", date,"일의 절기를 알 수 없습니다.")

    elif mon == 5:
        if date == 6:
            print("입력하신", mon,"월", date,"일은","'입하'입니다.")
        elif date == 21:
            print("입력하신", mon,"월", date,"일은","'소만'입니다.")
        elif date > 31:
            print("입력하신", mon,"월", date,"일은 일수를 잘못 입력하셨습니다.")
        else:
            print("입력하신", mon,"월", date,"일의 절기를 알 수 없습니다.")

    elif mon == 6:
        if date == 6:
            print("입력하신", mon,"월", date,"일은","'망종'입니다.")
        elif date == 21:
            print("입력하신", mon,"월", date,"일은","'하지'입니다.")
        elif date > 30:
            print("입력하신", mon,"월", date,"일은 일수를 잘못 입력하셨습니다.")
        else:
            print("입력하신", mon,"월", date,"일의 절기를 알 수 없습니다.")

    elif mon == 7:
        if date == 7:
            print("입력하신", mon,"월", date,"일은","'소서'입니다.")
        elif date == 23:
            print("입력하신", mon,"월", date,"일은","'대서'입니다.")
        elif date > 31:
            print("입력하신", mon,"월", date,"일은 일수를 잘못 입력하셨습니다.")
        else:
            print("입력하신", mon,"월", date,"일의 절기를 알 수 없습니다.")

    elif mon == 8:
        if date == 8:
            print("입력하신", mon,"월", date,"일은","'입추'입니다.")
        elif date == 23:
            print("입력하신", mon,"월", date,"일은","'처서'입니다.")
        elif date > 31:
            print("입력하신", mon,"월", date,"일은 일수를 잘못 입력하셨습니다.")
        else:
            print("입력하신", mon,"월", date,"일의 절기를 알 수 없습니다.")

    elif mon == 9:
        if date == 8:
            print("입력하신", mon,"월", date,"일은","'백로'입니다.")
        elif date == 23:
            print("입력하신", mon,"월", date,"일은","'추분'입니다.")
        elif date > 30:
            print("입력하신", mon,"월", date,"일은 일수를 잘못 입력하셨습니다.")
        else:
            print("입력하신", mon,"월", date,"일의 절기를 알 수 없습니다.")

    elif mon == 10:
        if date == 8:
            print("입력하신", mon,"월", date,"일은","'한로'입니다.")
        elif date == 13:
            print("입력하신", mon,"월", date,"일은","'저의 생일'입니다.")
        elif date == 23:
            print("입력하신", mon,"월", date,"일은","'상강'입니다.")
        elif date > 31:
            print("입력하신", mon,"월", date,"일은 일수를 잘못 입력하셨습니다.")
        else:
            print("입력하신", mon,"월", date,"일의 절기를 알 수 없습니다.")

    elif mon == 11:
        if date == 7:
            print("입력하신", mon,"월", date,"일은","'입동'입니다.")
        elif date == 22:
            print("입력하신", mon,"월", date,"일은","'소설'입니다.")
        elif date > 30:
            print("입력하신", mon,"월", date,"일은 일수를 잘못 입력하셨습니다.")
        else:
            print("입력하신", mon,"월", date,"일의 절기를 알 수 없습니다.")
            
    elif mon == 12:
        if date == 7:
            print("입력하신", mon,"월", date,"일은","'대설'입니다.")
        elif date == 22:
            print("입력하신", mon,"월", date,"일은","'동지'입니다.")
        elif date > 31:
            print("입력하신", mon,"월", date,"일은 일수를 잘못 입력하셨습니다.")
        else:
            print("입력하신", mon,"월", date,"일의 절기를 알 수 없습니다.")

else:
    print("아쉽지만 입력하신", mon,"월", date,"일은 양력일자가 아닙니다!!")

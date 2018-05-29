balance=0
esc=True
while esc:
    print("--------------------------------", sep="")
    print("1.예금 | 2.출금 | 3.잔고 | 4.종료", sep="")
    print("--------------------------------", sep="")
    no=int(input("선택>"))
    if no==1:
        balance+=int(input("예금액>"))
    elif no==2:
        balance-=int(input("출금액>"))
    elif no==3:
        print("잔고액>", balance)
    elif no==4:
        esc=False
        print("프로그램 종료")
    else:
        print("다시입력해주세요")

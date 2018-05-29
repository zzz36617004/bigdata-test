num=input("숫자 5개를 , 로 구분하여 입력하세요:")
sum=0
num=num.split(",")
for i in num :
    sum+=int(i)
print("평균은",sum/5,"입니다")
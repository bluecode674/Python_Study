#홀수번째 문자열 #으로 바꾸기 
ss = '파이썬은완전재미있어요'

sslen = len(ss)
for i in range(0, sslen):
    if (i%2 == 0):
        print(ss[i], end='')
    else:
        print("#", end='')


#문자열 특정 문자 제외하고 저장
inStr = "<<<파<<이>>썬>>>"
outStr = ""

for i in range(0, len(inStr)):
    if (inStr[i] != "<" and inStr[i] != ">"):
        outStr += inStr[i] 

print(outStr)

#문자열 조건문으로 타입 파악
a = input('문자열 입력 : ')
if a.isdigit():
    print("숫자입니다")
elif a.isalpha():
    print("글자입니다")
elif a.isalnum():
    print("글자+숫자입니다")
else:
    print("모르겠습니다")


# 문자열 내장 함수 사용
a = int(input("A과목: "))
b = int(input("B과목: "))
c = int(input("C과목: "))

sum = a+b+c
average = int(sum/3)
print(f"평균: {average}")
print(f"총점: {sum}")


# f-string?
a = int(input("구입 음악 개수 : "))
total = 400*a
print(f"총 가격: {total}원")
print(f"할인금액: {int(total*0.3)}원")
print(f"총 구입 가격: {int(total*0.7)}원")


# 인덱스

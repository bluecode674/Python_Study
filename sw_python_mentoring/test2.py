# 문제 1 
# 정수를 입력받아서 양수, 음수, 0 인지 판단하는 코드를 작성하시오

num = int(input('정수 입력: '))
if num > 0:
    print(f"{num}은 양수")
elif num < 0:
    print(f"{num}은 음수")
else:
    print(f"{num}은 0")

# 문제 2
# 자연수를 입력받아서 짝수, 홀수를 판단하는 코드를 작성하시오
num = int(input('정수 입력: '))
if num%2==1:
    print(f"{num}은 홀수")
else:
    print(f"{num}은 짝수")


# 문제3
# 아래 문제의 출력 결과를 답하시오
sum = 0
for i in range(2, 6, 1):
    sum = sum + i
print(sum)


sum = 0
for i in range(7):
    sum = sum + i
print(sum)


sum = 0
for i in range(1, 6, 2):
    sum = sum + i
print(sum)
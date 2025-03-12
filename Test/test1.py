# 문제 1
# 숫자 하나를 입력 받아서 그 숫자의 5를 곱한값 출력하기

num1 =input()
num1 = int(num1)
print(num1+6)

# 문제 2
# 연필과 볼펜을 구매하려고 합니다. 연필은 한 자루에 400원이고 볼펜은 한 자루에 800원이라면 구입한 연필과 볼펜의 가격은 얼마일까요?
# 조건: 구입한 연필과 볼펜의 개수를 사용자로부터 입력 받는다.

pencil = int(input('연필개수:'))
pen = int(input("볼펜 개수:"))
total_price = pencil*400+pen*800
print(total_price)

# 문제3
# 문자열 "hello world"에서 index를 활용해 w 출력하기

str = "hello world"
print(str[6])
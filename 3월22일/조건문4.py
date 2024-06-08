num1 = int(input('첫 번째 수 입력: '))
num2 = int(input('두 번째 수 입력: '))
p = input('원하는 연산 기호 하나 입력: (+ - * /)' )
if p == "+":
    print(f"{num1}+{num2}={num1+num2}")
elif p == "-":
    print(f"{num1}-{num2}={num1-num2}")
elif p == "*":
    print(f"{num1}*{num2}={num1*num2}")
elif p == "/":
    print(f"{num1}/{num2}={num1/num2}")
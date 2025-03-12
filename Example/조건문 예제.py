# 기본 조건문
num = int(input('정수 입력: '))
if num > 0:
    print(f"{num}은 양수")
elif num < 0:
    print(f"{num}은 음수")
else:
    print(f"{num}은 0")


# 가장 많이 쓰인는 홀짝 조건문
num = int(input('정수 입력: '))
if num%2==1:
    print(f"{num}은 홀수")
else:
    print(f"{num}은 짝수")

# 로그인 로직 조건문
id = input('아이디 입력: ')
pwd = input('비밀번호 입력: ')
if id == "admin" and pwd == "pw1234":
    print('로그인 성공')
else:
    print('아이디나 비밀번호가 틀려 로그인 실패')

# 합격 로직 조건문
num1 = int(input('1차 점수 입력: '))
num2 = int(input('2차 점수 입력: '))
if (num1+num2)/2 >= 70 and num1>=50 and num2>50:
    print("합격")
else:
    print("불합격") 


# 계산기 로직 조건문
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


# 학점 부여 로직 조건문
num1 = int(input('점수 입력: '))
if num1>=90:
    print(f"{num1}점은 A학점")
elif num1>=80:
    print(f"{num1}점은 B학점")
elif num1>=70:
    print(f"{num1}점은 C학점")
elif num1>=60:
    print(f"{num1}점은 D학점")
else:
    print(f"{num1}점은 F학점")


# 배송료 계산 로직 조건문
p1 = input("국가를 입력하시오: ")
if p1 == "한국":
    p2 = input("도를 입력하시오: ")
    if p2 == "제주도":
        print("배송료는 10000원입니다")
    else:
        print("배송료는 5000원입니다")
else:
    print("배송료는 20000원입니다")
 
# 논리회로
a = 1
b = 1
a and b 

a = 1
b = 0
a or b

a = 1
not a

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)

# 비교연산자
print('Python' == 'python')
print('python' == 'python')
print('Python' != 'world')

age = int(input("나이를 입력하세요: "))
print(age <= 34)
print(age >= 19)


# 조건문
width = int(input("너비를 입력하세요: "))
height = int(input("높이를 입력하세요: "))
figure = input("삼각형 또는 사각형을 입력하세요: ")

if (figure == "삼각형"):
  area = width * height / 2
elif (figure == "사각형"):
  area = width * height
else:
  area = 0

print(area)

if area != 0:
  print(f"{figure}의 면적은 {area} 입니다.")
else:
  print("다시 입력하세요.")

# 배수 판단 예제!!!!!  진짜 중요
x = 9
print(x % 3 == 0)

#  100종류의 숫자가 있는데 그중에서 3의 배수만 얻고싶어
#  X = [5, 16, 18, 7, 11, 9]

# x % 2 == 0 -> 짝수 판단
# x % 2 == 1 -> 홀수 판단




"""
if (조건식):
    조건식이 참일 때 실행할 문장
"""


"""
if (조건식):
    조건식이 참일 때 실행할 문장
else:
    조건식이 거짓일 때 실행할 문장
"""


"""
if (조건식1):
    조건식1이 참일 때 실행할 문장
elif (조건식2):
    조건식2가 참일 때 실행할 문장
elif (조건식3):
    조건식3이 참일 때 실행할 문장
else:
    모든 조건식이 거짓일 때 실행할 문장
"""



# 5!
# 1*2*3*4*5 = 5!
# 6!
# 1*2*3*4*5*6 = 6!



# 반복문 for
sum = 0
for i in range(10):
  sum = sum + i
  print(i)
print(sum)




iter_num = int(input("횟수를 입력하세요: "))
for i in range(iter_num):
  print(i)




r = 1
for i in range(1, 5+1, 2):
  r = r * i  
print(f"5! 은 {r} 입니다.")


"""
range(start, stop, step)
  - start : 처음 시작하는 값 (입력하지 않아도 됨, 기본 설정은 0)
  - stop : 마지막 값 - 1 (반드시 입력해야 하는 값)
  - step : 증가 또는 감소하는 숫자의 간격 (입력하지 않아도 됨, 기본 설정은 1)
"""

#  랜덤 함수
import random  #외부에서 random 함수를 가지고 온다.
print("lotto number: ", end='')

for i in range(6):
  print(random.randint(1, 45), end='') 
  if i != 5:
    print(', ', end='')


# 반복문 while
i = 1
while (i <= 100):
  print(i, end=' ')
  i = i + 1


# for문 비교
for i in range(1, 100 + 1,1):
  print(i, end=' ')


# 무한 반복문 break
while True:
  num = int(input("출력할 별 갯수: "))
  if (num == 0):
    print("프로그램을 종료합니다.")
    break
  for i in range(num):
    print("*", end='')  
  print("\n프로그램을 종료하고 싶으면 0을 입력하세요.")


"""
while (조건식):
    수행할 문장1
    수행할 문장2
"""


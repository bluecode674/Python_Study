
# 기본 프로그래밍 언어를 처음 배우면 기본적으로 하는 출력
print("hello world")
print("hello world")
print('안녕하세요')
print('안녕하세요')

# 숫자 출력
print(5*10/2)
print(10)
print("")

# 변수 정의 및 출력 예제1 (정수)
width = 5
height = 4

a = "안녕하세요"
print(a)
print(width)
print(width * height / 2)


# 변수 정의 및 출력 예제2 (실수)
pi = 3.14
b = 0
c = "hello world"
radius = 10
print(radius * radius * pi)


# 변수 정의 및 출력 예제 3 (문자열)
sentence = 'hello world!'
print(sentence)


# 문자열과 숫자형 동시 출력 예제1
width = 10
height = 5
rect_area = width * height / 2
print("너비 %dcm, 높이 %dcm 인 사각형의 넓이는 %dcm² 입니다." % (width, height, rect_area))



# 문자열과 숫자형 동시 출력 예제2
width = 10
height = 5
rect_area = width * height / 2
print(f"너비 {width}cm, 높이 {height}cm 인 사각형의 넓이는 {rect_area}cm² 입니다.")


# 문자열 입력

# print() - > 출력
# input() - > 입력


name = input("이름: ")
print("hello, " + name)


# 문자열 입력2
name = input("이름을 입력하세요: ") 
mbti = input("MBTI를 입력하세요: ")
print("당신의 이름은 " + name + "이고, 당신의 MBTI는 " + mbti + "입니다.")


age = int(input("나이를 입력하세요: "))
print(age+5)


# 문자열 입력 숫자형으로 변환 =>  중요!!!
radius = int(input("반지름의 길이를 입력하세요: "))
pi = 3.14
circle_area = radius * radius * pi
print("원의 넓이는 " + circle_area + "입니다.")


# 산술 연산식
print(5 / 3) # 나눗셈
print(5 // 3) # 몫
print(5 % 3) # 나머지 -> 가장 많이 사용
print(2 ** 4) # 제곱
print(5 + 3)
print(5 - 3)
print(5 * 3)


# 유니코드
ord("a") # 97
chr(97)

ord("!") # 33

chr(54681)
chr(4991)

ord("가") #44032
ord("나") #45208
chr(45208)





# 이스케이프 문자
"hello world"
print("hello world") 
print("hello\nworld") # \n -> 줄바꿈
print("hello\tworld") # \t

"hello world"

print("\"hello world\"")  # \"
print("\'hello world\'")  # \'
print("'hello world'")    
print("hello \\world")    # \\

# 문자 연산하기
str_1 = "hello"
str_2 = "world"
print(str_1 * 5)
print(str_1 + str_2)
print(str_1 + ' ' + str_2)

print()
input()
len("apple")

a = "hello world"
len(a)



# 내장 함수 
ipsum = '''
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
'''
len()


print(f"총 글자수는 {len(ipsum)}자 입니다.") # len() -> 글자 길이를 반환
print(ipsum.upper()) # .upper() -> 대문자로 반환
print(ipsum.lower()) # .lower() -> 소문자로 반환

str_1 = "HELLO"
str_2 = "world"
print(str_1.isupper()) # 대문자인지 확인
print(str_2.islower()) # 소문자인지 확인

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple") # 카운트
print(txt)
print(f"apple 은 총 {x} 번 나옵니다.")

txt = "I love apples, apple are my favorite fruit"
x = txt.find("apple") # 몇번째에 나오는지
print(txt)
print(f"apple 은 처음부터 {x+1} 번째 이후에 등장합니다.")


# 인덱스 index 별 5개!!!!!!!! 오늘 가장 핵심 내용 중 하나
pre_word = "python"
print(pre_word[5])
print(pre_word[4])
print(pre_word[0])
print(pre_word[-1])


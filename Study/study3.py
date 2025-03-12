## 9주차 리스트
person = ["김이준", 20, "남성", "isfj", "닭갈비"]

print(person)
print(person[0])
print(person[1])
print(person[2])

## 추가하기 
person.append("B")
person.append("서울")

print(person)


## 삭제하기
person.remove("B")

print(person)


## 원하는 위치에 추가
person.insert(2, "A",)

print(person)

## 원하는 값의 인덱스 출력
person.index("서울")

name = ["김하나", "김둘", "김셋", "김넷"]

## 내장함수
len(person) 
person.count("김")

num = [7, 18, 56, 9, 10, 150, 33]
num.sort()  #오름차순
print(num)
num.sort(reverse=True) #내림차순 
print(num)


word = ["apple", "banana", "duck", "cat"]
word.sort()
print(word)



## 튜플
a = (1, 3, 5, 7, 9)
print(a)

## 딕셔너리
person = {"name": "김이준", 
          "age": 20, 
          "gender": "남성"}
print(person)

print(person.keys())
print(person.values())
print(person["name"])
print(person["gender"])


person["혈액형"] = "B"
person["거주지"] = "서울"
person["age"] = 21
person["name"] = "김이준"

del person["거주지"]

print(person.keys())

print(person)


## 10주차 함수
a = 10
b = 20
print(a+b)


a = 20
b = 30
print(a+b)

def sum(a, b, c):
  print(a+b+c)
  return a+b+c

def sum2(a, b):
  return a + b


sum2(sum(10, 20, 30), sum(20,30,40))


## 1~x 까지 모두 더하는 프로그램
def sum(x):
  sum = 0  
  for i in range(1, x+1, 1):
    sum += i
  return sum

print(sum(10))
print(sum(100))
print(sum(1000))


## 파일
## pwd : print working directory 의 약자, 현재 위치를 출력해주는 명령어 입니다.
## mkdir : make directory 의 약자, 현재 작업 디렉터리에서 새로운 디렉터리를 만듭니다.
## cd : change directory 의 약자, 현재 작업 디렉터리에서 새로운 디렉터리로 이동합니다. 
## ls : list 의 약자, 현재 위치의 디렉터리 내용을 리스트로 출력하는 명령어 입니다

## cd ..
## cd "파일명"

## 읽기모드 : r
## 쓰기모드 : w
## 추가모드 : a



my_todo = open('todo.txt', 'r')
lines = my_todo.readlines()
print(lines)
my_todo.close()


my_todo = open('todo.txt', 'a')
my_todo.write('\nmy name')
my_todo.close()

my_wish = open('wish.txt', 'w')
my_wish.write('아이슬란드 오로라 보러 가기\n')
my_wish.write('남극 펭귄 보러 가기\n')
my_wish.write('아프리카 사자 보러 가기')
my_wish.close()

## gui, pygame




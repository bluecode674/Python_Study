# 컴퓨터랑 가위바위보를 하는 게임만들기 
# 조건 
# 1. 가위, 바위, 보 중 하나를 입력한다.
# 2. 결과를 출력한다.
# 3. 컴퓨터와 플레이 중 한명이 3승을 하면 게임이 끝난다.


import random

list = ["가위", "바위", "보"]
com_count = 0
user_count = 0

def count(s1, s2):
    global com_count
    global user_count
    if s1 == "가위":
        if s2 == "가위":
            print("컴퓨터: 가위")
            print("비겼습니다")
        elif s2 == "바위":
            print("컴퓨터: 바위")
            print("컴퓨터 승")
            com_count += 1
        elif s2 == "보":
            print("컴퓨터: 보")
            print("당신 승")
            user_count += 1
    elif s1 == "바위":
        if s2 == "가위":
            print("컴퓨터: 가위")
            print("당신 승")
            user_count += 1
        elif s2 == "바위":
            print("컴퓨터: 바위")
            print("비겼습니다")

        elif s2 == "보":
            print("컴퓨터: 보")
            print("컴퓨터 승")
            com_count += 1
    elif s1 ==  "보":
        if s2 == "가위":
            print("컴퓨터: 가위")
            print("컴퓨터 승")
            com_count += 1
        elif s2 == "바위":
            print("컴퓨터: 바위")
            print("당신 승")
            user_count += 1
        elif s2 == "보":
            print("컴퓨터: 보")
            print("비겼습니다")
    else:
        print("입력 오류 다시 입력해 주세요")
    return [com_count, user_count]

while (True): 
    s = input("가위, 바위, 보 중 하나를 입력하세요: ")
    num1 = random.randint(0,2)
    result = count(s, list[num1])
    if result[0] == 3:
        print("컴퓨터 3승!!")
        break
    elif result[1] == 3:
        print("당신 3승!!")
        break


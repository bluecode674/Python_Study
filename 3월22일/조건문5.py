num1 = int(input('1차 점수 입력: '))
num2 = int(input('2차 점수 입력: '))
if (num1+num2)/2 >= 70 and num1>=50 and num2>50:
    print("합격")
else:
    print("불합격") 
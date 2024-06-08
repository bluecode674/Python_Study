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

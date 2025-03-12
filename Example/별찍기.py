# for문 예제

# 공백이 먼저 있고 반대로 별찍기 반 피라미드
for i in range(5):
    print(' '*(4-i),'*'*(1+i))


# 거꾸로 한쪽 피라미드
for i in range(5):
    print(' '*(i),'*'*(5-i))


#피라미드
for i in range(5):
    print(' '*(4-i),'*'*(1+(i*2)))

# 거꾸로 피라미드
for i in range(5):
    print(' '*(i),'*'*(9-(i*2)))
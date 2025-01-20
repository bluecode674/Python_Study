'''
만들면서 생각하고 있는 부분 

1. 로또 6개를 어떻게 추첨할 것인가.
1~45까지 숫자를 리스트에 넣고 6개의 숫자를 랜덤으로 뽑자
숫자가 중복되지 않게 숫자를 삭제해 주자

처음에는 반복할때 마다 위에 내용을 반복하려고 했으나 
반복횟수가 많아지면 런타입이 길어질 것 같아서 
처음에 45개 숫자를 넣은 리스트를 만들고 추첨할 때 숫자를 삭제 했다가
추첨이 끝나면 다시 숫자를 넣어주는 식으로 했다. 

이렇게 하면 숫자의 순서가 반복할수록 랜덤으로 바뀌는데 이것또한 
로또이기 때문에 그냥 랜덤에 맡기기로 하였다.

2. 로또 숫자 분석 방법
일정 횟수를 반복했을 때 많이 나온 숫자를 기억
리스트에 0을 45개 집어넣고 위치에 맞는 값이 나올때 마다 숫자를 올리자

3. 분석 출력
0의 위치를 이용해 가장 많이 나온 숫자들을 찾아내자
가장 많이 나온 숫자를 리스트에 기억하고 그 자리를 0으로 만든다. 
이것을 6번 반복
가장 많이 나온 숫자 6개 출력
단점: 동순위가 여러개이면 앞에 것들부터 출력
'''

import random

def lottery():
    lucky_nums = []                 # 당첨리스트 생성
    for i in range(6):              # 랜덤으로 숫자 6개 추첨
        num = random.choice(lotto_nums)
        count_nums[num-1] += 1
        lucky_nums.append(num)
        lotto_nums.remove(num)      # 숫자가 중복되지 않게 나온숫자는 삭제해 준다

    for i in range(6):              # 추첨이 끝났으면 나온 숫자들을 넣어준다.
        lotto_nums.append(lucky_nums[i])

lotto_nums = []                 # 로또리스트 생성
for i in range(1,46):           # 로또리스트에 1~45숫자 넣기
    lotto_nums.append(i)

count_nums = []                 # 숫자가 나온 횟수를 저장한 리스트 생성
for i in range(1,46):           # 카운트리스트에 0을 45개 넣기
    count_nums.append(0)

loop = int(input("반복할 횟수를 입력해 주세요: "))
for i in range(loop):
    lottery()

result = []
for i in range(6):
    result.append(count_nums.index(max(count_nums))+1)
    count_nums[count_nums.index(max(count_nums))] = 0

result.sort()
print(result)



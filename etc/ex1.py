'''
import 모듈명
from 모듈명 import 함수명
from 모듈명 import 함수명 as 약어

ex) 랜덤 함수
'''
import random

numlist = [10, 20 ,30]
a = random.random()  # 0부터 1사이 수를 랜덤으로 반환
b = random.randint(1, 10) # 1~10 숫자 중 랜덤으로 반환
c = random.choice(numlist) # numlist에 요소 중 랜덤으로 반환

'''
def 함수명(매개변수1, 매개변수2):
    문장
    return 반환값

함수명(인수1, 인수2)
'''

def max(a, b):
    if a>b:
        return a
    else:
        return b
    
print(max(5,10))
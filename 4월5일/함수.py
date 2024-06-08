# #함수 과제 1
# def greet(lang):
#     if lang == 1:
#         print('Hola')
#     elif lang == 2:
#         print('Bonjour')
#     elif lang == 3:
#         print('안녕?')
#     else:
#         print('지원하지 않습니다')

# h = int(input('언어를 선택하세요(1:EN/2:FR/3:KR)'))
# greet(h)

# #함수 과제 2
# def concate(s1, s2):
#     return s1+s2
# str1 = input("1'st 문장입력:")
# str2 = input("2'st 문장입력:")
# print(concate(str1,str2))


# #함수 과제 3 
# def price(menue):
#     if menue == 1:
#         print('아메리카노는 2500원 입니다.')
#     elif menue == 2:
#         print('카페라떼는 3000원 입니다.')
#     elif menue == 3:
#         print('바닐라라떼는 3000원 입니다')

# menue = int(input('메뉴선택(1:아메리카노/2:카페라떼/3:바닐라라떼)'))
# price(menue)



# #함수 과제 4
# def score(a):
#     if a.isalpha():
#         return 'Bad score'
#     elif 1 >= float(a) >= 0.9:
#        return 'A'
#     elif 1 >= float(a) >= 0.8:
#         return 'B'
#     elif 1 >= float(a) >= 0.7:
#         return 'C'
#     elif 1 >= float(a) >= 0.6:
#         return 'D'
#     elif float(a) < 0.6:
#         return 'F'
#     else:
#         return 'Bad score'
# a = input('Enter score: ')
# print(score(a))


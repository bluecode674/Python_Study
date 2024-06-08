id = input('아이디 입력: ')
pwd = input('비밀번호 입력: ')
if id == "admin" and pwd == "pw1234":
    print('로그인 성공')
else:
    print('아이디나 비밀번호가 틀려 로그인 실패')
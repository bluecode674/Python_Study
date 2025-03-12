#리스트 key value 확인 예제
people = {100:'yang', 200:'jang', 300:'o'}
print(list(people.keys()))
print(list(people.values()))
print(list(people.items()))
print(people.get(200))
del(people[100])
print(people)

#list 내장 함수 확인 예제
name = ["홍일동", "홍이동", "홍삼동"]
print(name)
name.append("홍사동")
print(1,name)
name.insert(1,"홍이동")
print(2, name)
print(3, name.count("홍이동"))
name.reverse()
print(4, name)
name.remove("홍일동")
print(5, name)
name.sort(reverse=True)
print(6, name)
print(7, len(name))


# 리스트 전화번호 찾기 예제
addr ={}
addr['최재원']='010-1111-1234'
addr['최지윤']='010-2222-1234'
addr['김연수']='010-3333-1234'
addr['김연우']='010-4444-1234'
addr['김가현']='010-5555-1234'
addr['김혜현']='010-6666-1234'

print(list(addr.keys()))
name = input("search name: ")
print(addr.get(name,'not Found'))

# 리스트 결합 및 연산 예제
clubA = {'kim', 'park', 'hwang'}
clubB = {'park', 'lee', 'choi'}
clubC = clubA | clubB
print(clubC)
print(clubA & clubB)
print(clubA - clubB)
print(clubB - clubA)
clubA.add('yang')
clubB.remove('lee')
print(clubA)
print(clubB)
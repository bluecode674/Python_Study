list3 = [20, 50, 60, 70,90]
result = 0
max_num = 0
for i in range(len(list3)):
    result = result + list3[i]
print(result/5)

for i in range(len(list3)):
    if (max_num < list3[i]):
        max_num = list3[i]
print(max_num)


list4 = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
for i in range(len(list4)):
    if len(list4[i]) == 5:
        print (list4[i])

for i in range(len(list4)-1,-1,-1):
    print(list4[i])
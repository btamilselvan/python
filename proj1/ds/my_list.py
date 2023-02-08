a_list = ['a', 'b', 'c']
b_list = list((1, 2, 3))

a_list.reverse()
for a in a_list:
    print(a)

print(a_list.count('a'))
print(f'length is {len(a_list)}')

i = 0
while(i<len(a_list)):
    print(a_list[i])
    i+=1

a_list.extend(b_list)
i = 0
while(i<len(a_list)):
    print(a_list[i])
    i+=1


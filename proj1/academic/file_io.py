from pathlib import Path

p = Path('t:/temp/')
for i in p.iterdir():
    if(i.is_file()):
        print(i, 'is a file')
    else:
        print(f'{i} is a directory')

my_file = open('t:\\temp\\mysql-init.txt', 'r')
# print(my_file.readlines())

for line in my_file.readlines():
    print(line)
# can be read only once.. the below print will not print anything as the buffer has been cleared already.
for line in my_file:
    print(line)

my_file.close()

another_file = open('t:\\temp\\hello_python.txt', 'w')
another_file.write('Hello world')
another_file.write('Happy Pongal')
# another_file.writelines(['Happy Pongal', 'Howdy'])
another_file.close()

another_file = open('t:\\temp\\hello_python.txt', 'r')
print(another_file.readlines())

#the file will be auto closed when used opened using 'with'
with open('t:\\temp\\hello_python.txt', 'a') as f1:
    f1.write('new line')

print('done')
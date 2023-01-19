#syntax error (compilation errors) and exceptions (runtime)
# a = 10/0 #ZeroDivisionError
# b = 'a' + 10 #TypeError

from msilib.schema import Error


while True:
    try:
        b = 'a' + 10 #TypeError
        a = 10/0
        break
    except TypeError as inst:
        print('TypeError occurred')
        print(type(inst))
        print(inst)
        print(inst.args)
        break
    except ZeroDivisionError:
        print('ZeroDivisionError occurred')
        break
    except:
        print('all other errors')
        break

class A(Exception):
    pass

class B(A):
    pass

class C(B):
    pass

class D(C):
    pass
#This would print B, C, D.
for cls in [B, C, D]:
    try:
        raise cls()
    except(D):
        print(cls)
    except(C):
        print(cls)
    except(B):
        print(cls)

#This would print B, B, B because B is the base class for C, D so the C, D except blocks will become unrachable.
for cls in [B, C, D]:
    try:
        raise cls()
    except(B):
        print(cls)
    except(C):
        print(cls)
    except(D):
        print(cls)

try:
    raise TypeError('some type error')
except Exception as e:
    print(e)
    # raise TypeError('Type error occurred')
else:
    print('no exception occurred. this will be executed only when there is no exception')
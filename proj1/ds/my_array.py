import array as arr
# import NumP

arr1 = arr.array('i', [1,2,3,4])
print(type(arr1))
arr1.append(10)
for i in arr1:
    print(i)

# arr2 = arr1.tobytes()
# for i in arr2:
#     print(i)
    
arr3 = arr.array('u', ["a", "b"])
for i in arr3:
    print(i)
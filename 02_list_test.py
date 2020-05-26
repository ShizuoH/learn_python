
array1 = [1, 2, 3]
array2 = [4, 5, 6]

join_array = array1 + array2
print(join_array)

# append
tmp_array = array1
tmp_array.append(array2)
print(tmp_array)
print(array1)

# insert
array2.insert(2, 1000)
print(array2)
print(array1)

# del
del array1[-1]
print(array1)

# index
array3 = [1, 2, 3, 2, 1]
print(array3.index(1))
print(array3.index(2))
print(array3.index(1, 0))
print(array3.index(1, 1))
print(array3.index(1, -1))
# print(array3.index(1, 100)) # error

# len
array = ["a", "b", "c"]
print(len(array))

# copy
a = [0, 1, 2]
b = a.copy()
c = list(a)
d = a[:]

a[0] = 10
b[0] = 11
c[0] = 12
d[0] = 13

print("copy")
print(a)
print(b)
print(c)
print(d)






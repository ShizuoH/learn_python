

a = {'a':'a', 'b':'b', 'c':'c'}
print(a)

##############
print('delete, in, clear')
del a['a']
#a.del('a') # error
print(a)

print('a' in a)
print('b' in a)
# print(a.in('b')) # error

a.clear()
print(a)

##########
print('keys, values, items')
a = {'a':'a', 'b':'b', 'c':'c'}
print(a.keys())
print(a.values())
print(a.items())

##########
print('set starts')
my_set1 = {'a', 'b', 'c', 'd'}
my_set2 = {'d', 'e', 'f', 'g'}
my_key1 = 'a'
my_key2 = 'h'

print(my_set1 & my_set1)
# print(my_key1 & my_set1) # error
print(my_key1 in my_set1)
print(my_set1 - (my_set1 & my_set2))












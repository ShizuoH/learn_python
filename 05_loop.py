### for

tmp_dict = {'a':'a', 'b':'b'}
print(tmp_dict)

for key in tmp_dict:
    print(key)
    
for item in tmp_dict.items():
    print(item)
    print(item[0])
    print(item[1])


search_letter = 'd'    
for key in tmp_dict:
    if (key == search_letter):
        print(search_letter + " is found")
        break
else:
    print(search_letter + " is not found")
    

a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e']

for aa, bb in zip(a, b):
    print(aa)
    print(bb)

print(zip(a, b))
print(list(zip(a, b)))
print(dict(zip(a, b)))


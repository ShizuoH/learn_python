

def func1():
    print("hello world")


func1()

def func2():
    return 1, 2, 3
a, b, c = func2()
print(a)
print(b)
print(c)


print("--- func3 ---")
def func3(a, b, c):
    print(a)
    print(b)
    print(c)
func3('a', 'b', 'c')
func3(c = 'c', a = 'a', b = 'b')


print("--- sum function ---")

print(sum([1, 2, 3]))
print(sum(range(0, 10)))


print("--- lambda function ---")

def func4(func, *args):
    print(func)
    print(args)
    return func(*args)

hoge = func4(lambda *args: sum(args), 1, 2, 3, 4)
print(hoge)

fuga = (1, 2, 3, 4)
print(fuga)
print(*fuga)

print("--- global local ---")

global1 = 'global1'

def local_func():
#    print(global1)
    global global1
    global1 = 'local1'
    print(global1)

print(global1)
local_func()
print(global1)

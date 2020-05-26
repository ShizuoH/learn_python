

class OopsException(Exception):
    pass

def check_word(word):
    my_tupple = ('a', 'b', 'c', 'd',)
    if word in my_tupple:
        print("OK")
    else:
        raise(OopsException(word))

try:
    word = [1, 2, 3]
    check_word(word)
    
except OopsException as oops_err:
    print("OopsException occur: ", oops_err)
except Exception as other_err:
    print("other error occur: ", other_err)
    

def my_range(start, end, step = 1):
    val = start
    while val < end:
        yield val
        val += step
        
hoge = list(my_range(1, 10, 3))
print(hoge)

    
    

### OrderedDict
from collections import OrderedDict

quoats = OrderedDict({"a":"a", "b":"b"})
print(quoats)
quoats["c"] = "c"
print(quoats)

del quoats["b"]
print(quoats)

# print(quoats["b"])
print(quoats.get("b"))



########## deque
from collections import deque

hoge = deque([1, 2 ,3, 4, 5])
print(hoge)
hoge.append(6)
print(hoge)
hoge.appendleft(-1)
print(hoge)


### pprint
from pprint import pprint
hoge = {"a":"aaaaaaaaaa", "b":"bbbbbbbbbb", "c":"cccccccccc", "d":"dddddddddd", "e":"eeeeeeeeee"}
pprint(hoge)

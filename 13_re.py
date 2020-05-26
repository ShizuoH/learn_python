import re

source = "hogehoge fugafuga hello world"

m = re.match('hogehoge', source)
if m:
    print(m.group())
else:
    print('not found')

m = re.match('hogefuga', source)
if m:
    print(m.group())
else:
    print('not found')

m = re.match('.*fuga.*hello', source)
if m:
    print(m.group())
else:
    print('not found')

m = re.sub('hogehoge', 'test', source)
print(m)

m = re.sub('hogehoge (.*) hello (.*)', '\\1, \\2, hogehoge, hello', source)
print(m)

m = re.sub('hogehoge (.*) hello (.*)', r'\1, \2, hogehoge, hello', source)
print(m)

source = 'My name is Shizuo.'
m = re.search(r'My name is (?P<NAME>.*)\.$', source)
if m:
    print(m.group())
    print(m.group('NAME'))
else:
    print('not found')
    


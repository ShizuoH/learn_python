n = 51
f = 5.1
s = "hello world"

str = '{} {} {}'.format(n, f, s)
print(str)

str = '{2} {0} {1}'.format(n, f, s)
print(str)

str = '{n} {f} {s}'.format(n=51, f=5.1, s='hello world')
print(str)

str = '{:<10d} {:<10f} {:<20s}'.format(n, f, s)
print(str)

str = '{:>10d} {:>10f} {:>20s}'.format(n, f, s)
print(str)

str = '{:^10d} {:^10f} {:^20s}'.format(n, f, s)
print(str)

str = '{:-^10d} {:=^10f} {:$^20s}'.format(n, f, s)
print(str)


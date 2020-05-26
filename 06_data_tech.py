

a = [number for number in range(1,10,3)]
print(a)


b = [number for number in range(0, 100, 4) if (number % 3) == 0]
print(b)


rows = range(1,5)
cols = range(1,3)

c = [[row, col] for row in rows for col in cols]
print(c)




word = 'letter'
for letter in word:
    print(letter)

letter_count = {letter : word.count(letter) for letter in word}
print(letter_count)

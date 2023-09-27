word = '-1 -2 -3 -4'
lst = []
number = []

lst = word.split(sep=' ')

number = list(map(int, lst))
max = max(number)
min = min(number)
print(max,min)


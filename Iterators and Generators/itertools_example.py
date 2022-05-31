from itertools import count, cycle

print('Iterator 1')
iterator = count(start = 1, step = 2)
print(next(iterator))
print(next(iterator))
print('Iterator 2')
iterator_2 = cycle('ABCD')
print(next(iterator_2))
print(next(iterator_2))
print(next(iterator_2))
print(next(iterator_2))
print(next(iterator_2))
print(next(iterator_2))
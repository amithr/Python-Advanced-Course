test_array = [1, 2, 3, 4]
print(dir(test_array))
# print(next(test_array)) # List is an iterable not an iterator
test_array_iterator = iter(test_array)
print(next(test_array_iterator))
print(next(test_array_iterator))
print(next(test_array_iterator))
print(next(test_array_iterator))
print(dir(test_array_iterator))

# Show how it works with iterables
print('Test Array 1')
for i in test_array:
    print(i)
    
print('Test Array 2')
for j in test_array:
    print(j)

print('Test Array Iterator 1')
test_array_iterator = iter(test_array)
for i in test_array_iterator:
    print(i)

print('Test Array Iterator 2')
for j in test_array_iterator:
    print(j)



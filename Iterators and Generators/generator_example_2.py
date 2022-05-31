# Second Example (Second Example)
def fibonacci_gen():
    trailing,leading = 0,1
    while True:
        yield leading
        trailing,leading = leading, trailing+leading

fib_sequence = fibonacci_gen()
print(next(fib_sequence))
print(next(fib_sequence))

for i in fib_sequence:
    print(i)
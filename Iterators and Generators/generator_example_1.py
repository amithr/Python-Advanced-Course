# First Example
def powers_of_3(n):
    # Starts with 1
   for i in range(1, n):
      yield i**3
    
powers = powers_of_3(5) # returns iterator
print(next(powers))
for i in powers:
    print(i)
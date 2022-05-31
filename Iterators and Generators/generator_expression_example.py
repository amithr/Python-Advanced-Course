def squares(length):
    for n in range(length):
        yield n ** 2

# This is like list comprehensions, but with parenthesis instead of square brackets
squares = (n**2 for n in range(5))
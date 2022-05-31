class EvenNumbers:
    # Other Class Methods
    #
    #
    def __iter__(self):
        # Must always return an object (the iterator object)
        self.first_number = 0
        return self
    
    def __next__(self):
        
        x = self.first_number
        self.first_number += 2
        return x

even_numbers = EvenNumbers()

for i in even_numbers:
    print(i)

    
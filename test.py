class Car:
    def __init__(self, number):
        self.number = number
        self.current = number  # Keep track of the current state for iteration

    def __iter__(self):
        # The __iter__ method should return the iterator object itself (which is usually self)
        return self

    def __next__(self):
        # Define the stopping condition for the iterator
        if self.current < self.number + 5:  # Let's iterate for 5 steps
            current_value = self.current
            self.current += 1
            return current_value
        else:
            # StopIteration is raised to signal that the iteration is complete
            raise StopIteration

# Create an instance of Car
car = Car(10)

# Iterating over the car object
for num in car:
    print(num)

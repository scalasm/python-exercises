# You can add __iter__() to make a class "iterable" and __next__() to make it actually "iterable"
class MyRange:
    """
    Allows for iterating across an interval [a,b[, right exstreme excluded!
    """
    def __init__(self, start,end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == self.end:
           raise StopIteration
        
        next = self.current

        self.current += 1

        return next

print( "With Iterable class:" )
for value in MyRange(1,10):
    print(value)


# Generators are functions that 'yield' values and can do pretty much the same things with less boiler plate code
def my_range(start,end):
    """
    Generator function for iterating across an interval [a,b[, right exstreme excluded!
    """
    for current in range(start,end):
        yield current

print( "With generators:" )
for value in my_range(1,10):
    print(value)

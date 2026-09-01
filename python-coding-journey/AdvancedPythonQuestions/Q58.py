# 58. Create your own Iterator
# To create a custom iterator in Python, implement:
# __iter__() → returns the iterator object itself.
# __next__() → returns the next value.

class MyIterator:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration


obj = MyIterator()

for i in obj:
    print(i)
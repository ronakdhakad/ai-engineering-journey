# 59. Create your own Generator
# A Generator is a function that uses the yield keyword to produce values one at a time instead of returning all values at once.

def my_generator():
    yield 1
    yield 2
    yield 3

g = my_generator()

for i in g:
    print(i)
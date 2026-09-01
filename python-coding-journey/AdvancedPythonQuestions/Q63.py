# 63. Demonstrate Closure
# A Closure is a function inside another function that remembers and can access variables from the outer function even after the outer function has finished executing.
def outer():
    n=10
    def inner():
        m=20

        return m*n


    return inner

# inner=outer()
print(outer()())
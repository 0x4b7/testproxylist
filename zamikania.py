def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
print(closure(5))

print(closure(3))

outer_function(40)
print(closure(1))

closure = outer_function(50)
print(closure(6))



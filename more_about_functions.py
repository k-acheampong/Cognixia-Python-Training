PI = 3.14  # Constant functions should be in all caps


# aliasing in the function parameters. Suggests best data type to use as a parameter
def some_function(x: int, y: int, z: int):

    final = x + y + z
    return(x)


output = some_function(5, 6, 7)
# print(output)


def greet_friend(greeting, name):
    print(greeting, name + "!")


greet_friend("Hello", "John")

PI = 3.14  # Constant functions should be in all caps


# aliasing in the function parameters. Suggests best data type to use as a parameter
def some_function(x: int, y: int, z: int):

    final = x + y + z
    return(x)


output = some_function(5, 6, 7)
# print(output)


def greet_friend(name, greeting, sentence):
    output = "{2}, {0}!, {1}".format(name, greeting, sentence)
    print(output)


greet_friend("John", "Hey", "How are you doing today?")


def greet_user(greeting):
    user = input("Please enter your name: ")
    print(type(user))
    print("{}, {}!".format(greeting, user))
    print(5 + int(input("Please enter an integer: ")))


greet_user("Hello")

#n = int(input("Provide a number: "))

# if n % 2 != 0:
#   print("Weird")
# elif n % 2 == 0 and n in range(2, 5):
#    print("Not Weird")
# elif n % 2 == 0 and n in range(6, 20):
#    print("Weird")
# elif n % 2 == 0 and n > 20:
#    print("Not Weird")


def isWeird(x):
    if x % 2 != 0:
        print("Weird")
    elif x % 2 == 0 and x in range(2, 6):
        print("Not Weird")
    elif x % 2 == 0 and x in range(6, 21):
        print("Weird")
    elif x % 2 == 0 and x > 20:
        print("Not Weird")


test_cases = [1, 2, 3, 4, 6, 8, 11, 18, 20]
for i in test_cases:
    isWeird(i)

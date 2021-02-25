try:
    user_int = int(input("Please enter an integer: "))
    a = 1/0
except ValueError:
    print("You did not enter a value that can be cast as an integer.")
except ZeroDivisionError:
    print("Do not divide by zero")
except Exception:
    print("General exception")
finally:
    pass

print("End of program.")

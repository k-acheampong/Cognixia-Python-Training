import math


class Calculator():

    memory = []
    last = None

    def add(self, x, y):
        '''
        Finds the sum of two numbers
        '''
        self.last = x + y
        self.memory.append(self.last)
        return self.last

    def subtract(self, x, y):
        '''
        Subtracts one number from another
        '''
        self.last = x - y
        self.memory.append(self.last)
        return self.last

    def multiply(self, x, y):
        '''
        Finds the product of two numbers
        '''
        self.last = x * y
        self.memory.append(self.last)
        return self.last

    def divide(self, x, y):
        '''
        Divides two numbers
        '''
        self.last = x / y
        self.memory.append(self.last)
        return self.last

    def exponent(self, x, y):
        '''
        Given x number as a base, finds x to the y power
        '''
        self.last = x ** y
        self.memory.append(self.last)
        return self.last

    def sqrt(self, x):
        '''
        Finds the sqrt of a given number
        '''
        self.last = math.sqrt(x)
        self.memory.append(self.last)
        return self.last

    def returnLast(self):
        '''
        Returns the last value stored
        '''
        return self.last

    def returnMemory(self):
        '''
        Returns the values stored in memory
        '''
        return self.memory


if __name__ == "__main__":

    my_calculator = Calculator()

    continue_calculator = True

    print(
        "1. ADDITION"
        "\n2. SUBTRACTION"
        "\n3. MULTIPLICATION"
        "\n4. DIVISION"
        "\n5. EXPONENT"
        "\n6. SQUARE ROOT"
    )

    try:
        choice = int(
            input("Provide a number to chose an arithmetic operation: "))
    except ValueError:
        print("You did not enter a value that can be cast as an integer.")
    finally:
        pass

    if choice == 1:
        try:
            x = int(
                input("Provide an integer of your choice: "))
        except ValueError:
            print("You did not enter a value that can be cast as an integer.")
        finally:
            pass
        try:
            y = int(
                input("Provide another integer of your choice: "))
        except ValueError:
            print("You did not enter a value that can be cast as an integer.")
        finally:
            pass
        my_calculator.add(x, y)

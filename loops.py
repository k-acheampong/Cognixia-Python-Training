list_of_numbers = [0, 1, 2, 'blue', 4, 5]

# for loop
for elem in list_of_numbers:
    if type(elem) == str:
        continue
    print(elem)

# range loop
# iterating over elements is preferable to using a range most of the time
for i in range(5, 20, 2):  # 3rd element counts by 2
    print(i)

# while loop
i = 0
while i < 10:
    print(i)
    i += 1

# use for programs you want on all the time
i = 0
while True:
    i += 1
    if i > 10:
        break  # breaks a while loop once a condition is fulfilled

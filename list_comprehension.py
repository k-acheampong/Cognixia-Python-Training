l = [1, 2, 3, 4, 5]

for elem in l:
    print(elem)

[print(elem) for elem in l]
print()

[print(elem) for elem in l if elem >= 5]  # list comprehension
print()

(print(elem) for elem in l if elem >= 5)  # generator

print(list(map(lambda x: x**2, 1)))

name = ("mohit", 3, 4, 4, "rohit")

print(type(name))

l1 = name.count(4)
print(l1)
l1 = name.index("mohit")
print(l1)

# Convert list to tuple

l = [1, 2, 3]
t = tuple(l)
print(t)


# Convert tuple to list

t = (1, 2, 3)
l = list(t)
print(l)
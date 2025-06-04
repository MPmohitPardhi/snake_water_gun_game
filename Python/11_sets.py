s = () #empt sets
s = {1, 2, 3, 4, 5, 6, "mohit"}

print(s, type(s))
s.add(10)
print(s)
s.remove(10)
print(s)
print(len(s))
s.pop()
print(s)


# Returns a new set with all items from both sets. 
# • s.intersection

s1 ={1 ,2, 3}
s2 ={3, 4, 5}

print(s1.union(s2))
print(s1.intersection(s2))
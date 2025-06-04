mark = {
    "mohit": 100,
    "rohit" : 73,
    "monu" : 50,
    "priyanch" : 20
}

print(mark.items())
print(mark.keys())
print(mark.values())
mark.update({"mohit": 99})
print(mark)
print(mark.get("mohit2"))  #print Noun
print(mark["mohit2"])    #print errar

mark.setdefault("mohit", 99)
# mark = dict.fromkeys(keys, 0) 
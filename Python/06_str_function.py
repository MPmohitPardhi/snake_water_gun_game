name = "mohit"

print(len(name))
# print(len("mohit"))

print(name.endswith('hit'))
print(name.startswith("mo"))
print(name.capitalize())

# 🔤 Basic String Functions
text = "hello"
print("Length:", len(text))          # 5
print("String conversion:", str(123))  # '123'

# 🔍 Search & Find
text = "hello world"
print("Find:", text.find("l"))         # 2
print("rFind:", text.rfind("l"))       # 9
print("Index:", text.index("o"))       # 4
print("'world' in text?", "world" in text)  # True

# ✂️ Slicing & Substrings
print("Slice:", text[0:5])             # 'hello'
print("Split:", "a,b,c".split(","))    # ['a', 'b', 'c']
print("rSplit:", "a b c".rsplit(" ", 1))  # ['a b', 'c']
print("Partition:", "a=b".partition("="))  # ('a', '=', 'b')

# 🔠 Case Conversion
print("Lower:", "HELLO".lower())       # 'hello'
print("Upper:", "hello".upper())       # 'HELLO'
print("Capitalize:", "python".capitalize())  # 'Python'
print("Title:", "hello world".title()) # 'Hello World'
print("Swapcase:", "Hello".swapcase()) # 'hELLO'

# 🧼 Strip & Replace
print("Strip:", "  hello  ".strip())   # 'hello'
print("LStrip:", "  hello".lstrip())   # 'hello'
print("RStrip:", "hello  ".rstrip())   # 'hello'
print("Replace:", "a+b+c".replace("+", "-"))  # 'a-b-c'

# ✅ Validation Methods
print("Is Alnum:", "abc123".isalnum())  # True
print("Is Alpha:", "abc".isalpha())     # True
print("Is Digit:", "123".isdigit())     # True
print("Is Lower:", "hello".islower())   # True
print("Is Upper:", "HELLO".isupper())   # True
print("Is Space:", "   ".isspace())     # True
print("Startswith:", "hello".startswith("he"))  # True
print("Endswith:", "hello".endswith("lo"))      # True

# 🧩 Join
print("Join:", "-".join(["a", "b", "c"]))  # 'a-b-c'

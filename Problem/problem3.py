# 1. Write a python program to display a user entered name followed by Good
# Afternoon using input () function
# a = str(input("Enter the Message: " ))

# print(f"Good moring  {a}")


# 2. Write a program to fill in a letter template given below with name and date.

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>", "Mohit").replace("<|Date|>", "2025"))

# 3. Write a program to detect double space in a string.

name = "mohit is very  good good boy"

print(name.find("  "))

# 4. Replace the double space from problem 3 with single spaces.

name = "mohit is very  good good boy"

print(name.replace("  ", " "))

#5. Write a program to format the following letter using escape sequence
# characters.


letter = "Dear Harry, \nthis python course is nice. \nThanks!"

print(letter)
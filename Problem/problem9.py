# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.


with open("myfile.txt") as f:
    c =f.read()


if "mohit" in c.lower():
    print("found")
else:
    print("not found");    


# 2. The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score



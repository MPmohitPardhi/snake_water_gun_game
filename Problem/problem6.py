# 1. Write a program to find the greatest of four numbers entered by the user.

# a1 = int(input("enter the number: "))
# a2 = int(input("enter the number: "))
# a3 = int(input("enter the number: "))
# a4 = int(input("enter the number: "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("a1  is greatest Number: ")
# elif(a2>a1 and a2>a3 and a2>a4):
#     print("a2  is greatest Number: ")    
# elif(a3>a1 and a3>a2 and a3>a4):
#     print("a3  is greatest Number: ")    
# else:
#     print("a4  is greatest Number: ")    



# 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.
    

# m = float(input("Enter the Marke: "))
# s = float(input("Enter the Marke: "))
# h = float(input("Enter the Marke: "))

# sum = m+s+h
# par = sum/300

# if(sum >= 40 ):
#     print("pass")
# else:
#     print("fail")    

# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.    

# p1 = "Make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4 = "click this"

# message = input("entr the message")
# if(p1 in message or p2 in message or p3 in message or p4 in message):
#     print("this comment is spem")
# else:
#     print("this not spem")    


# 4. Write a program to find whether a given username contains less than 10
# characters or not.


# 4. Check if Username has Less Than 10 Characters

# username = input("Enter your username: ")

# if len(username) < 10:
#     print("Username has less than 10 characters.")
# else:
#     print("Username has 10 or more characters.")

# ✅ 5. Check if Name is Present in a List

# names = ["Mohit", "Rohit", "Kunal", "Ankit", "Sakshi"]
# check_name = input("Enter a name to check: ")

# if check_name in names:
#     print("Name is present in the list.")
# else:
#     print("Name is not present in the list.")

# ✅ 6. Grade Calculator Based on Marks

# marks = float(input("Enter the marks (out of 100): "))

# if 90 <= marks <= 100:
#     print("Grade: Ex")
# elif 80 <= marks < 90:
#     print("Grade: A")
# elif 70 <= marks < 80:
#     print("Grade: B")
# elif 60 <= marks < 70:
#     print("Grade: C")
# elif 50 <= marks < 60:
#     print("Grade: D")
# elif marks < 50:
#     print("Grade: F")
# else:
#     print("Invalid marks entered.")


# ✅ 7. Detect if a Post Mentions “Harry”

# post = input("Enter the post: ")

# if "harry" in post.lower():  # Convert to lowercase to ignore case
#     print("The post talks about Harry.")
# else:
#     print("The post does not mention Harry.")
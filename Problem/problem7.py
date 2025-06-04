# 1. Write a program to print multiplication table of a given number using for loop

# for i in range(1, 11):
#     print(2*i)



# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.

# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in l:
#     if name.startswith("S"):
#         print("Hello", name)


# 3. Attempt problem 1 using while loop

# i = 1
# while(i<=10):
#     print(i*2)
#     i += 1



# 4. Write a program to find whether a given number is prime or not

# n = int(input("Enter a number"))

# for i in range(1, n):
#     if(n%1) == 0 :
#         print("this not prime number")    
#         break
# else:
#     print("number is prime")    


# 5. Write a program to find the sum of first n natural numbers using while loop.    

# a = int(input("enter the number: "))

# i = 1
# sum = 0

# while i <= a:
#     sum += i
#     i += 1

# print("sum of all nuber is: ", sum) 

# 6. Write a program to calculate the factorial of a given number using for loop.

# a = int(input("enter the number: "))

# i = 1
# fac = 1

# while(i <= a):
#     fac *= i;
#     i += 1

# print("The fact number: ", fac)    


# 7. Write a program to print the following star pattern.
#  *
# ***
# ***** for n = 3


# a = int(int(input("Enter the number: ")))

# for i in range(1,a+1):
#     print(" "* (a-i), end="") 
#     print("*"* (2*i-1), end="")
#     print("")
    

# 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3

# a = int(input("Enter the number of start: "))

# for i in range(1 , a+1):
#     print(" "* (a-1),end="")
#     print("*"*(2*i-1), end="")
#     print("")


# 9. Write a program to print the following star pattern.
# * * *
# * * for n = 3
# * * *

# a = int(input("Enter the number of start: "))

# for i in range(1 , a+1):
#     if(i==1 or i==a):
#         print("*"* a, end="")
#     else:
#         print("*" , end="")
#         print(" "* (a-2),end="")
#         print("*" , end="")
#     print("")


# 10. Write a program to print multiplication table of n using for loops in reversed
# order    

n = int(input("Enter a number: "))

print(f"Multiplication table of {n} in reverse order:")
for i in range(10, 0, -1):  # from 10 to 1
    print(f"{n} x {i} = {n*i}")
# 1. Write a program using functions to find greatest of three numbers.

# def greatestof(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
    

# num1 = int(input("enter the number: "))
# num2 = int(input("enter the number: "))
# num3 = int(input("enter the number: "))
# print(greatestof(num1, num2, num3))



# 2. Write a python program using function to convert Celsius to Fahrenheit


# def c_to_f(f):
#     return  5*(f-32)/9

# f = int(input("enter the value F: "))
# c = c_to_f(f)
# print(f"{round(c, 2)}C")

# 3. How do you prevent a python print() function to print a new line at the end.

# print("a")
# print("b")
# print("c", end=" ")
# print("d", end=" ")


# 4. Write a recursive function to calculate the sum of first n natural numbers


# def natura_no(n):
    
#        if(n == 1):
#           return 1;
#        else:
#           return n + natura_no(n-1)
       
# n = int(input("entet the nuber: "))

# print(natura_no(n))


# 5. Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

# def patten(n):
#     if(n==0):
#       return
#     print("*"*n)
#     patten(n-1)

# n = int(input("entet the number: "))
# print(patten(n))        
# Questions Involving Loops*

# Write a program to print the sum of all even numbers between 1 and 100.

# def even(a,b,c):
#     count=0
#     for i in range(a,b,c):
#         count+=i
#     return count
# print(even(0,101,2))

# Write a program that prints the first 10 powers of 2 using a loop.

# def power(a,b,c):
#     count=0
#     for i in range(b,c):
#         print(a**i)
# power(2,0,10)
    
# Calculate the factorial of a number entered by the user.

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
# y=int(input('Enter the number: '))
# print(factorial(y))

# Print the reverse of a given number (e.g., input 1234 → output 4321).

# def reverse(a):
#     rev = 0
#     while a>0:
#         b=a % 10
#         rev=rev * 10 + b
#         a=a // 10
#     return rev
# l=int(input('Enter a number: '))
# print(reverse(l))

# Count the number of digits in a given integer using a loop.

# def count_digits(b):
#     count=0
#     while b>0:
#         a=b%10
#         count+=1
#         b=b//10
#     return count
# x=int(input('Enter a number to count the digits: '))
# print(count_digits(x))


# Write a program that prints all numbers from 1 to 100 that are divisible by both 3 and 5.


# def divisible(a,b):
#     for i in range(a,b):
#         if i%3==0 and i%5==0:
#             print(i)
# divisible(1,101)



# Without using multiplication, calculate a * b using addition and a loop.

# def multiplication(a):
#     b=0
#     for i in range(a):
#         b+=5
#     return b
# x=int(input('Enter a number: '))
# print(multiplication(x))

# 8. Print the sum of digits of a number entered by the user (e.g., 123 → 1+2+3 = 6).
# 9. Write a loop to check if a number is a palindrome (number reads the same forwards and backwards).
# 10. Write a program to find the highest digit in a given number.


# #### 🔀 *Questions Involving Conditionals*

# 11. Write a program to check if a number is positive, negative, or zero.
# 12. Write a program that takes a number and prints whether it is divisible by 2, 3, both, or neither.
# 13. Check if a number is a three-digit number using conditionals.
# 14. Write a program to check whether a given number is a prime number.
# 15. Write a program to find the largest of three numbers entered by the user using nested if-else.
# 16. Check if a year is a leap year or not.
# 17. Take an integer input and determine if it is even and greater than 50.
# 18. Write a program to classify a number as:
#  Less than 0: "Negative"
# * 0 to 9: "Single Digit"
# * 10 to 99: "Two Digits"
# * 100 and above: "Three or More Digits"


# Print all numbers from 1 to N using a loop.

# N=int(input('Enter: '))
# for i in range(1,N+1):
#     print(i)


# Print all even numbers from 1 to N.


# N=int(input('Enter: '))
# for i in range(1,N+1):
#     if i%2==0:
#         print(i,'Even')

# -1 to -10

# for i in range(-10,0,1):
#     print(i)


# for i in range(-1,-11,-1):
#     print(i)


# for i in range(10,-1,-1):
#     print(i)

# Print all odd numbers from 1 to N.

# n=int(input('Enter: '))
# for i in range(n):
#     if i%2!=0:
#         print(i)


# Calculate the sum of the first N natural numbers.

# n=int(input('Enter: '))
# sum=0
# for i in range(1,n):
#     sum+=i
# print(sum)

# Print the multiplication table of a given number up to 10.

# i=10
# for j in range(11):
#     print(i,'*',j,'=',i*j)

# # Count the number of digits in a given number.
# 1234 % 10=4
# #1234//10=123
# 123% 10=3
# #123//10=12
# 12 % 10=2
# #12//10=1
# 1%10=1
# #1//10=0

# n=int(input('Enter :'))
# count=0
# while n>0:
#     a=n%10
#     count+=1
#     n=n//10
# print(count)

# # Count the number of digits in a given number.

# n=int(input('Enter :'))
# count=0
# while n>0:
#     a=n%10 #25%10=5
#     count+=1 #count=count+1=0+1=1
#     n=n//10 #25//10=2
# print(count)








# n = int(input('Enter the number: '))
# rev = 0
# count = 0
# temp = n
# while n > 0:
#     rem = n % 10
#     count += rem
#     rev = rev * 10 + rem
#     n = n // 10
# print("Sum of digits:", count)
# print("Reversed number:", rev)

# def reverse(n):
#     rev=0
#     count=0
#     while n>0:
#         rem = n % 10
#         count += rem
#         rev = rev * 10 + rem
#         n = n // 10   
#     return rev
# x=int(input("Enter a number to reverse: "))
# print(reverse(x))



# def sum(n):
#     count = 0
#     while n > 0:
#         rem = n % 10
#         count += rem
#         n = n // 10
#     return count
# l=int(input('Enter the number: '))
# print(sum(l))




# def sum_digits(n):  # Correct function name to avoid conflict with built-in 'sum'
#     count = 0
#     while n > 0:
#         rem = n % 10
#         count += rem  # Add the last digit to count
#         n //= 10  # Remove the last digit
#     return count

# print(sum_digits(123))  # Output: 6











# n = int(input('Enter the number: '))
# rev = 0
# count = 0
# temp = n
# while n > 0:
#     rem = n % 10        
#     rev = rev * 10 + rem
#     n = n // 10
# print(rev)
# if (temp == rev):
#     print('palindrome')
# else:
#     print('Not a palindrome')



# def palindrome(n):
#     rev = 0
#     temp = n  
#     while n > 0:
#         rem = n % 10
#         rev = rev * 10 + rem  
#         n //= 10 
#     print(rev) 
#     if (temp == rev):
#         print("Palindrome")
#     else:
#         print("Not a palindrome")
# x=eval(input('Enter: '))
# palindrome(x)













# n = int(input('Enter the number: '))
# rev = 0
# count = 0
# temp = n
# while n > 0:
#     rem = n % 10        
#     rev = rev * 10 + rem
#     n = n // 10
# print(rev)

# Reverse a String Without Using [::-1]:
# Reverse a string using a loop or recursion.

# def string_reverse(s):
#     r=" "
#     for i in s:
#         r=i+r
#     print(r)
# string_reverse('sindhu')

# Count Frequency of an Element in a List:
# Input a list and an element; count how many times the element appears.


# def count(l):
#     c=0
#     for i in l:
#         if i==10:
#             c+=1
#     print(c)
# list=[10,20,30,40,50,10]
# count(list)


# def count(l):
#     c=0
#     for i in l:
#         if i==num:
#             c+=1
#     print(c)
# list=[10,20,30,40,50,10]
# num=10
# count(list)


# def count(s):
#     c=0
#     for i in s:
#         if i==name:
#             c+=1
#     print(c)
# strings=['sindhu','lucky','sindhu','sindhu','sindhu','sindhu']
# name='sindhu'
# count(strings)


# Print First N Prime Numbers:
# Take N as input and print the first N prime numbers.

# def prime(r):
#     for n in range(2,r+1):
#         count = 0
#         for i in range(1,11):
#             if n % i == 0:
#                 count += 1
#         if count == 2:
#             print(n, "is Prime")
#         else:
#             print(n, "is Not Prime")
# l=int(input('Enter the number upto which prime number you need(N):'))
# prime(l)

# Remove Duplicates from a List:
# Given a list, return a new list without duplicates (maintain order).


# list=[10,25,86,756,25,12,20,10,10]
# def remove_duplicates(l):
#     li=[]
#     for i in l:
#         if i not in li:
#             li.append(i)
#     print(li)
# remove_duplicates(list)



# strings=['g','s','i','i','n','d','h','u']
# def remove_duplicates(s):
#     str=" "
#     for i in s:
#         if i not in str:
#             str+=i
#     print(str)
# remove_duplicates(strings)


# FizzBuzz:
# For numbers from 1 to N, print:
# “Fizz” if divisible by 3
# “Buzz” if divisible by 5
# “FizzBuzz” if divisible by both
# Else print the number itself.

# def FizzBuzz(n):
#     for i in range(1,n):
#         if i%3==0:
#             print(i,'Fizz')
#         elif i%5==0:
#             print(i,'Buzz')
#         elif i%3==0 and i%5==0:
#             print(i,'FizzBuzz')
#         else:
#             print(i)
# num=int(input('Enter a number: '))
# FizzBuzz(num)
#Print All pairs from 1 to 3
#question:
#use nested for loops to print all pairs of numbers from 1 to 3
#Answer:
#for i in range(1,4):
    #for j in range(1,4):
       # print(i,j)

#2.Print the Multiplication Table from 1 to 5
# question:
#use nested for loops to print the multipication table from 1 to 5
#Answer:
# for i in range(1,6):
#     for j in range(1,11):
#         print(i,"x",j,"=",i*j)

# 3.Count How many times numbers are added
#question:
#write a program that uses nested for loops to add numbers from 1 to 3,three times each,count how many total additions happen
#Answer:
# count=0
# for j in range(1,4):
#  sum=0
#  for i in range(1,4):
#   sum+=1
#   print(sum)
# count+=1
# print(count)

# 4.Find All pairs Where First Number is Less Than Second 1 to 5
# question:
# use nested for loops to print all number pairs from 1 to 5 where the first number is less than the second.
# Answer:
# for i in range (1,5):
#     for j in range(1,5):
#         if i<j+1:
#             print(i,j+1)

# 5.Sum of all pairs (1 to 3)
#question:
#use nested for loops to find the sum of all possible pairs of numbers from 1 to 3 and print each pair with its sum.
#Answer:
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,"+",j,"=",i+j)

#6.Count how many times each character appears in "mississippi"
# a="mississippi"
# count=0
# for i in a:
#     count+=1
#     print(count)

#7. Find the value in the string "Chaitanya" Expected:a,i,a,a
# a="chaitanya"
# for i in a:
#     if i in "aeiou":
#         print(i)

# 8. Find how many times the letter'a' appears in "banana" Expected:3
# a="banana"
# count=0
# for i in a:
#     if i=="a":
#         count+=1
#         print(count)
    
# 9. Print all the characters in "Education" that are not vowels Expected:d,c,t,n
# a="education"
# for i in a:
#     if i not in "aeiou":
#         print(i)

# 10. Find and print all the capital letters in "welcome To Python" 

# a="WELCOME TO PYTHON"
# for i in a:
#     if i .isupper():
#         print(i)

# 11. Check if the character 'z' is present in "amazing" Expected:yes
# a="amazing"
# if "z" in a:
#     print("yes")

# 12. Replace all 'a' with '*' "banana" Expected : b*n*n*
# a="banana"
# b=a.replace("a","*")
# print(b)

# 13. Remove all vowels from "chaitanya" and print the result. expected:chnty
# a="chaitanya"
# for i in a:
#     if i not in("aeiou"):
#         print(i)

# 14. write a program to remove special characters from string
# a="Snehitha_123_@#"
# a=''
# for i in a:
#     if i.isalnum():
#      a+=1
# print(a)

# 15. Write a program to remove spaces using replace method
# a="snehi tha 06"
# print(a.replace(" ",""))

# 16. Find the number of spaces in the string
# a="snehi tha 06"
# count=0
# for i in a:
#     if i==' ':
#         count+=1
#         print(count)

# 17.Write a program to print the sum of all even numbers between 1 and 100

# def even(n):
#     a=0
#     for i in range(1,n):
#         if i%2==0:
#             a+=i
#     return a
# print(even(100))

# 18. Write a program that prints the first 10 powers of 2 using a loop

# def power(n):
#     a=0
#     for i in range(0,n):
#         a=2**i
#         print("2 power",i,"=",a)
# power(10)

# 19. Calculate the factorial of a number entered by the user.

# def factorial(n):
#     a=0
#     if n<=1:
#         print("zero and one")
#     for i in range(1,n):
#         n*=i
#         print(n)
# factorial(5)

# 20.print the reverse of a given number(e.g; input 1234 output 4321)


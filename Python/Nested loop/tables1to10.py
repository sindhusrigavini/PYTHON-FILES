# Multiplication Table (1 to 10)
# Write a Python program using nested loops to print the multiplication tables from 1 to 10.
# Example Output (partially shown)
# 1 x 1 = 1
# 1 x 2 = 2
# ...
# 10 x 10 = 100


# n=int(input("Enter a value: "))
# for i in range(1,n+1):
#     print('-----------')
#     for j in range(1,11):
#         print(i,"*",j,"=",i*j)
    


# Count Prime Numbers in a Range (1 to 100)
# Using nested loops, count how many prime numbers exist between 1 and 100.
# Hint : A number is prime if it’s only divisible by 1 and itself.


# def prime(r):
#     prime_count = 0 
#     prime_sum = 0  
#     for n in range(2, r + 1):
#         count = 0
#         for i in range(1, n + 1): 
#             if n % i == 0:
#                 count += 1
#         if count == 2:  
#             print(n)  
#             prime_count+=1
#     print('Prime numbers range between 1 to 100: ',prime_count) 
# prime(100)


# Print All Pairs of Numbers (1 to n) Where Sum is Even
# Ask the user to enter a number n. Using nested loops, print all pairs (i, j) from 1 to n where the sum i + j is even.
# Example for n = 3:
# (1,1)
# (1,3)
# (2,2)
# (3,1)
# (3,3)

# n=int(input('Enter a number: '))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if (i+j)%2==0:
#             print((i,j))
            


# Count Total Factors of All Numbers from 1 to n
# Ask the user to enter a number n. Use nested loops to find how many total factors (divisors) exist for all numbers from 1 to n.
# Example for n = 4
# 1 → 1
#  2 → 1, 2
#  3 → 1, 3
# 4 → 1, 2, 4
# Total = 8 factors



# n=int(input("Enter a num: "))
# count=0
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i%j==0:
#            print(j)
#            count+=1
# print("total factors",count)


# Print All Pythagorean Triplets with Values ≤ n
# Ask the user to enter n. Find and print all  Pythagorean triplets (a, b, c) such that a² + b² = c² and a, b, c ≤ n.
# Example for n = 20:
# (3, 4, 5)
# (5, 12, 13)
# (6, 8, 10)
# (8, 15, 17)


# n=int(input("Enter a num: "))
# for i in range(1,n+1):
#     for j in range(i,n+1):  
#         for k in range(1,n+1):
#               a=(i**2)+(j**2)
#               if a==k**2:
#                     print(i,j,k)

# a=int(input('Enter a number: '))
# b=int(input('Enter a number: '))
# print(a & b)

# a=int(input('Enter a number: '))
# b=int(input('Enter a number: '))
# print(a & b)

# a=int(input('Enter a number: '))
# b=int(input('Enter a number: '))
# print(a ^ b)

# for n in range(2,30):
#     count = 0
#     for i in range(1, n+1): 
#         if n % i == 0:
#             count += 1
#     if count == 2:  
#         print(n)  
           

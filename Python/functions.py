# #functions

# def natural(a,b):
#     for a in range(1,b):
#         print(a)
# natural(1,11)



# def even(a,b):
#     for a in range(a,b):
#         if a%2==0:
#             print(a)
# even(2,21)


# def string():
#     s="python"
#     for i in s:
#         print(i)
# string()




# def sum():
#     s=0
#     for i in range(1, 101):
#         s+=i 
#     print(s)
# sum()



# def table(i,j,k):
#     for j in range(i,j):
#         print(k,'*',j,'=',k*j)
# table(1,11,5)



# def list():
#     l=["apple", "banana", "cherry"]
#     for i in l:
#         print(i)
# list()




# def vowels():
#     s="education"
#     v="aeiou"
#     for char in s:  #education
#         if char in v: #aeiou
#            print(char)
# vowels()




# def vowels(s,v):
#     for char in s:  #education
#         if char in v: #aeiou
#            print(char)
# vowels(s="education",
#     v="aeiou")



# def c(s,count):
#     for i in s:
#         if i=='a':
#             count+=1
#     print(count)
# c(s='banana',
# count=0)



# def reverse(a,b,c):
#     for i in range(a,b,c):
#         print(i)
# reverse(10,0,-1)



# def s(sum, n):
#     for i in range(1, n): 
#         sum += i
#     print(sum)
# s(0, 6)  

# def odd(a,b,c,sum):
#     for i in range(a,b,c):
#         sum+=i
#     print(sum)
# odd(1,10,2,0)



# def even(a,b,c,sum):
#     for i in range(a,b,c):
#         sum+=i
#     print(sum)
# even(2,10,2,0)


# def sum(a,b,c):
#     for i in range(a,10):
#         c+=i
#     print(c)
# sum(1,10,0)



# def greater(a,b):
#     if a>b:
#         print('a is greater')
#     else:
#         print('b is greater')
# greater(1000,2500)
# greater(25000,10000)



# def greater(a,b,c):
#     if a>b and a>c:
#         print('a is greater')
#     elif b>a and b>c:
#         print('b is greater')
#     else:
#         print('c is greater')
# greater(1000,2500,500)



# def prime(r,count):
#     for n in range(2, r+1):
#         count = 0
#         for i in range(1, n+1): 
#             if n % i == 0:
#                 count += 1
#         if count == 2:
#             print(n, "is Prime")
#         else:
#             print(n, "is Not Prime")
# prime(6,0)




# def prime(r,count):
#     for n in range(0, r):
#         count = 0
#         for i in range(1, n+1): 
#             if n % i == 0:
#                 count += 1
#                 sum=0
#         if count == 2:
#             print(n)
# prime(20,0)


# def year(x):
#     print(x)
#     if (x%400==0) or (x%4==0 and x%100!=0):
#         print('leap year')
#     else:
#         print('not leap year')
# year(2025)

# def natural(n,sum):
#     for i in range(0,n+1):
#         sum=+i
#         print(sum)
# sum=0
# h=int(input('Enter :'))
# natural(h,sum)
# sum=0
# i=int(input('Enter :'))
# natural(i,sum)
# sum=0
# j=int(input('Enter :'))
# natural(j,sum)


# def fun(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     print(sum)
# fun(30)

# def fun(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     return sum
# print(fun(30))

# sum=0
# def fun(n):
#     for i in range(1,n+1):
#         global sum
#         sum+=i
#     return sum
# print(fun(30))
# print(fun(30)) #starts from previous sum


# sum=0
# def fun(n):
#     for i in range(1,n+1):
#         global sum
#         sum+=i
#     return sum
# print(fun(30))
# print(fun(30))

# def even_or_odd(v):
#     r=" "
#     if v%2==0:
#         r="even"
#     else:
#         r="odd"
#     return r
# u=int(input('Enter:'))
# w=even_or_odd(u)
# if w=="even":
#     print('Welcome')
# else:
#     print('sorry')



# def prime(r):
#     for n in range(2, r+1):
#         count = 0
#         for i in range(1, n+1): 
#             if n % i == 0:
#                 count += 1
#         if count == 2:
#             print(n, "is Prime")
#         else:
#             print(n, "is Not Prime")
# prime(20)





# def prime(r):
#     sum=0
#     for n in range(2, r+1):
#         count = 0
#         for i in range(1, n+1): 
#             if n % i == 0:
#                 count += 1
#         if count == 2:
#             print(n)
#             sum+=n
#     print('sum of prime:',sum)
# prime(20)



# def even_or_odd(v):
#     sum=0
#     for i in range(0,v+1):
#         if i%2!=0:
#             print(i)
#             sum+=i
#     print('sum of odd numbers: ',sum)
# u=int(input('Enter:'))
# even_or_odd(u)




# def prime(r):
#     sum=0
#     for n in range(11, r+1):
#         count = 0
#         for i in range(1, n+1): 
#             if n % i == 0:
#                 count += 1
#         if count == 2:
#             print(n)
#             sum += n
#     print('sum of prime:',sum)
# prime(17)




# even=lambda x:x%2==0
# print(even(10))

# even=lambda x:x%2==0
# print(even(7))


# odd=lambda y:y%2!=0
# print(odd(1))

# odd=lambda y:y%2!=0
# print(odd(2))

# n=int(input("Enter: "))
# odd=lambda n:n%2!=0
# print(odd(n))

# a=int(input("Enter: "))
# add=lambda a:a+10
# print(add(a))


# print next 5 prime numbers from a given number 

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     else:
#         return True
# num=3
# count=0
# while count<=2:
#     if is_prime(num)==True:
#         print(num)
#         count+=1
#     num+=1


a=int(input())
l=[]
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        l.append(n)
while len(l)<5:
    prime(a)
    a+=1
prime(l)

# a=int(input())
# l=[]
# def prime(n):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1
#     if count==2:
#         l.append(n)
# while len(l)<5:
#     prime(a)
#     a+=1
# print(l)
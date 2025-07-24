# * * * * 
# * * * * 
# * * * * 
# * * * * 

# rows=4
# for i in range(1,rows+1):
#     res=''
#     for j in range(1,rows+1):
#         res+='*'+' '
#     print(res)

# n=int(input('Enter a number:'))
# i=1
# while(i<=n):
#     print('* '*n)
#     i+=1

# n=int(input('Enter a number:'))
# i=1
# while(i<=n):
#     print('* '*(n*2))
#     i+=1

# n=int(input('Enter a number:'))
# i=1
# while(i<=n):
#     print('* '*i)
#     i+=1

# n=int(input('Enter a number:'))
# i=1
# while(i<=n):
#     print('* '*i)
#     i+=1

# n=int(input('Enter a number:'))
# i=1
# while(i<=n):
#     print('* '*i)
#     i+=1

# n=int(input('Enter a number:'))
# i=1
# while(i<=n):
#     spaces=' '*(n-i)
#     stars='* '*i
#     print(spaces+stars)
#     i+=1


# n=int(input('Enter a number:'))
# i=1
# while(i<=n):
#     spaces=' '*(i-1)
#     stars='* '*(n-i+1)
#     print(spaces+stars)
#     i+=1



# n=int(input('Enter a number:'))
# i=1
# while(i<=n):
#     spaces=' '*(n-i)
#     stars='* '*i
#     print(spaces+stars)
#     i+=1
# i=2
# while(i<=n):
#     spaces=' '*(i-1)
#     stars='* '*(n-i+1)
#     print(spaces+stars)
#     i+=1

n=5
temp=n
i=0
while(n>=i):
    spaces=' '*(temp-i-n)
    stars='* '*n
    print(spaces+stars)
    n-=1
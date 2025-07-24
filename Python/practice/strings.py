# v='sindhusrigavini'
# for i in range(len(v)):
#     print(i)

# v='sindhusrigavini'
# w=len(v)
# print(w)

# v='sindhusrigavini'
# w=len(v)-1
# print(w)

# v='sindhusrigavini'
# for i in range(len(v)):
#     if i%2==0:
#         print(v[i])

# v='sindhusrigavini'
# count=0
# for i in range(len(v)-1):
#     count+=1
# print(count)


# v='chaitanya'
# for i in range(len(v)):
#     if v[i]=='a':
#         continue
#     print(v[i],end='')


# v='chaitanya'
# for i in range(len(v)):
#     if v[i]!='a':
#         print(v[i],end='')

# v='chaitanya'
# s=''
# t='ani'
# for i in v:
#     if i not in t:
#         s+=i
# print(s)

# v='chaitanya'
# t='ani'
# for i in range(len(v)):
#     if v[i] not in t:
#         print(v[i],end='')

# v='chaitanya'
# t='ani'
# for i in v:
#     if i not in t:
#         print(i,end='')

# v='chaitanya'
# t='aeiou'
# for i in v:
#     if i in t:
#         print(i,end='')

#concatination

# a='sindhu'
# b='sri'
# c=a+b
# print(c)

# a='sindhu'
# b='sri'
# print(a+' '+b)

# a='Sindhu'
# b='Warangal,Telangana'
# c=('Hi im ' + a +',' 'i come from ' + b)
# print(c)


# s='mom341'
# t=''
# for i in s:
#     t=i+t
# print(t)

# s='sindhu'  
# for i in range(len(s)):
#     pass
# print(s[1:4])

# help('keywords')

#slicing

# s='sindhu'
# print(s[0])

# s='sindhu'
# print(s[1:4])

# s='sindhu'
# print(s[0:len(s):2])

# s='sindhu'
# print(s[:])

# s='sindhu'
# print(s[::1])

# s='sindhu'
# print(s[::-1])

# s='sindhusri'
# print(s[-3:])

#Methods

# lower='HELLO'.lower()
# print(lower)

# upper='hello'.upper()
# print(upper)


# s='chAitAnya'
# t=s[:]
# print(t.lower())

# s='chaitanya'
# t=s[:]
# print(t.upper())

# s='sindhu'
# t=s.capitalize()
# print(t)

# s='sinDhu sRi Gavini'
# print(s.swapcase())

# s='SindhuSriGavini'
# upper=''
# lower=''
# for i in s:
#     if i.isupper():
#         upper+=i
#     else:
#         lower+=i
# print(s)
# print('upper letters:',upper,'&','lower letters:',lower)

# s='sindhu30'
# for i in s:
#     if i.isalpha():
#         print(i,end='')

# s='sindhu30'
# for i in s:
#     if i.isdigit():
#         print(i,end='')

# s='sindhu30'
# for i in s:
#     if i.isalnum():
#         print(i,end='')

# s='sindhu sri gavini -ssg'
# for i in s:
#     if i.isspace():
#         print('*',end='')
        
# s='sindhu'
# t=s.replace('s','S')
# print(t)

# s='Sindhu'
# for i in s:
#     print(i,'Ascii:',ord(i),', ',end='')


# print(chr(90))

# print(ord('S'))

# s='sindhusri'
# print(s.find('i'))

# s='sindhusri'
# print(s.rfind('i'))

# s='sndhusri'
# print(s.index('i'))

# s='sindhusri'
# print(s.startswith('s'))

# s='sindhusri'
# print(s.endswith('i'))

# s='sindhu sri gavini'
# for i in s:
#     if ord(i)==32:
#         continue
#     print(i,end='')

# s='sindhu'
# t=''
# for i in s[1:len(s)-1]:
#     t+='*'
# print('s'+ t +'u')

# s='ind'
# print(s.zfill(5))

# s='ind'
# print(s.center(7,'*'))
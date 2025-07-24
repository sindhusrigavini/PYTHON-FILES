#  Take a string print all upper case letters at first and lower case letters at last  without using method

s = 'SindhuSriGavini'
x = ""
y = "" 
for i in s:
    if i.isupper():
        x += i
    elif i.islower(): 
        y += i
print(x + y)

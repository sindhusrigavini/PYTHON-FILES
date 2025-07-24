# s="sindhusrigavini"
# for i in range(6,9):
#     print(s[i],end='')


s = "hi this is sindhu and is sri"
t = ""
for i in s.split():
    if i == "is":
        t += "si "
    else:
        t += i + " "
print(t.strip()) 



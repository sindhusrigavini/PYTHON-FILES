# *
# *
# * 
# *
# * * * * *

rows=5
for i in range(1,rows+1):
    res=''
    for j in range(1,rows+1):
        if i==rows or j==1:
            res+='*'+' '
        else:
            res+=' '+' '
    print(res)
print('  ')

# *       * 
# *       *
# *       *
# *       *
# * * * * *

rows=5
for i in range(1,rows+1):
    res=''
    for j in range(1,rows+1):
        if j==rows or j==1 or i==rows:
            res+='*'+' '
        else:
            res+=' '+' '
    print(res)
print('  ')

# * * * * *        
# *       
# *       
# *       
# * * * * *

rows=5
for i in range(1,rows+1):
    res=''
    for j in range(1,rows+1):
        if i==rows or j==1 or i==1:
            res+='*'+' '
        else:
            res+=' '+' '
    print(res)
print('  ')

# *       *
# *     *
# *  *
# *     *
# *       *

rows=5
mid=(rows//2)+1
for i in range(1,rows+1):
    res=''
    for j in range(1,rows+1):
        if i<mid:
            if j==1 or i+j==rows+1:
                res+='*'+' '
            else:
                res+=' '+' '
        else:
            if j==1 or i==j:
                res+='*'+' '
            else:
                res+=' '+' '
    print(res)
print('  ')

# *       *
#   *   *
#     *
#     *
#     *

rows=5
mid=(rows//2)+1
for i in range(1,rows+1):
    res=''
    for j in range(1,rows+1):
        if i<mid:
            if i==j or i+j==rows+1:
                res+='*'+' '
            else:
                res+=' '+' '
        else:
            if j==mid:
                    res+='*'+' '
            else:
                res+=' '+' '
    print(res)
print('  ')
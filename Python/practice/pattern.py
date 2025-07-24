# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

# rows=5
# for i in range(1,rows+1):
#     res=''
#     for j in range(1,rows+1):
#         res+='*'+' '
#     print(res)

# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# rows=5
# for i in range(1,rows+1):
#     res=''
#     for j in range(1,rows+1):
#         res+=str(j)+' '
#     print(res)

# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

# rows=5
# for i in range(1,rows+1):
#     res=''
#     for j in range(1,rows+1):
#         res+=str(i)+' '
#     print(res)

# 1 
# 1 2 
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# rows=5
# for i in range(1,rows+1):
#     res=''
#     for j in range(1,i+1):
#         res+=str(j)+' '
#     print(res)

# * 
# * * 
# * * * 
# * * * * 
# * * * * *

# rows=5
# for i in range(1,rows+1):
#     res=''
#     for j in range(1,i+1):
#         res+='*'+' '
#     print(res)


# 1 
# 2 2 
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# rows=5
# for i in range(1,rows+1):
#     res=''
#     for j in range(1,i+1):
#         res+=str(i)+' '
#     print(res)
        
# * * * * * 
# * * * * 
# * * *
# * * 
# * 

# rows=5
# for stars in range(rows,0,-1):  ## rows=5 rows-1   5-1=4 3 2 
#     res=''
#     for j in range(1,stars+1):
#         res+='*'+' '
#     print(res)

# * * * * * 
# *       * 
# *       *
# *       *
# * * * * *

# rows=5
# for i in range(1,rows+1):
#     res=''
#     for j in range(1,rows+1):
#         if i==1 or i==rows or j==1 or j==rows:
#             res+='*'+' '
#         else:
#             res+=' '+' ' #character + space
#     print(res)

#  *       * 
#    *   *   
#      *     
#    *   *   
#  *       *

# rows=5
# for i in range(1,rows+1):
#     res=' '
#     for j in range(1,rows+1):
#         if i==j or i+j==rows+1:
#             res+='*'+' '
#         else:
#             res+=' '+' '
#     print(res)

# X O X O X 
# O X O X O 
# X O X O X
# O X O X O
# X O X O X

# rows=5
# for row in range(1,rows+1):
#     res=''
#     for col in range(1,rows+1):
#         if (row+col)%2==0:
#             res+='X'+' '
#         else:
#             res+='O'+' '
#     print(res)

# * * * * * 
#     *     
#     *
#     *
#     *

# rows=5
# for row in range(1,rows+1):
#     res=''
#     for col in range(1,rows+1):
#         if row == 1 or col == (rows//2)+1:
#             res+='*'+' '
#         else:
#             res+=' '+' '
#     print(res)

# *       * 
# *       * 
# * * * * *
# *       *
# *       *

# rows=5
# for row in range(1,rows+1):
#     res=''
#     for col in range(1,rows+1):
#         if row==(rows//2)+1 or col==1 or col==rows:
#             res+='*'+' '
#         else:
#             res+=' '+' '
#     print(res)

# * * * * * 
# *
# * * * * *
# *
# * * * * *

# rows=5
# for row in range(1,rows+1):
#     res=''
#     for col in range(1,rows+1):
#         if col==1 or row==1 or row==(rows//2)+1 or row==rows :
#             res+='*'+' '
#         else:
#             res+=' '+' '
#     print(res)

# *       * 
# * *     * 
# *   *   *
# *     * *
# *       *

# rows=5
# for row in range(1,rows+1):
#     res=''
#     for col in range(1,rows+1):
#         if row==col or col==1 or col==rows:
#             res+='*'+' '
#         else:
#             res+=' '+' '
#     print(res)

# * * * * * 
#       *   
#     *     
#   *       
# * * * * * 

# rows=5
# for i in range(1,rows+1):
#     res=''
#     for j in range(1,rows+1):
#         if i==1 or i==5 or i+j==rows+1:
#             res+='*'+' '
#         else:
#             res+=' '+' '
#     print(res)

#     * 
#    * * 
#   * * *
#  * * * *
# * * * * *

# rows=5
# for i in range(1,rows+1):
#     res=''
#     for space in range(1,rows-i+1):  
#         res+=' '
#     for j in range(1,i+1):
#         res+='*'+' '
#     print(res)

# * * * * * 
#  * * * * 
#   * * *
#    * *
#     *

# rows=5
# for i in range(rows,0,-1):
#     res=''
#     for space in range(1,rows-i+1):
#         res+=' '
#     for j in range(1,i+1):
#         res+='*'+' '
#     print(res)

#     * 
#    * * 
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# rows=5
# rows2=4
# for i in range(1,rows+1):
#     res=''
#     for space in range(1,rows-i+1):  
#         res+=' '
#     for j in range(1,i+1):
#         res+='*'+' '
#     print(res)
# for i in range(rows2,0,-1):
#     res=''
#     for space in range(1,rows2-i+2):
#         res+=' '
#     for j in range(1,i+1):
#         res+='*'+' '
#     print(res)

#     01
#   02 03
#  04 05 06
# 07 08 09 10

# rows=4
# num=1
# for i in range(1,rows+1):
#     res=''
#     for space in range(1,rows-i+1):
#         res+=' '
#     for j in range(1,i+1):
#         if i<10:
#             res+='0'+str(num)+' '
#         else:
#             res+=str(num)+' '
#         num+=1
#     print(res)

#    a
#   b c
#  d e f
# g h i j

# rows=4
# asc=97
# for i in range(1,rows+1):
#     res=''
#     for space in range(1,rows-i+1):
#         res+=' '
#     for j in range(1,i+1):
#         res+=chr(asc)+' '
#         asc+=1
#     print(res)

#    1 
#   2 2 
#  3 3 3
# 4 4 4 4

# rows=4
# for i in range(1,rows+1):
#     res=''
#     for space in range(1,rows-i+1):
#         res+=' '
#     for j in range(1,i+1):
#         res+=str(i)+' '
#     print(res)

#    1 
#   1 2 
#  1 2 3
# 1 2 3 4

# rows=4
# for i in range(1,rows+1):
#     res=''
#     for space in range(1,rows-i+1):
#         res+=' '
#     for j in range(1,i+1):
#         res+=str(j)+' '
#     print(res)

# * * * * * 
# *
# * * * * *
#         *
# * * * * *

# rows=5
# mid=(rows//2)+1
# for i in range(1,rows+1):
#     res=''
#     for j in range(1,rows+1):
#         if i<=mid:
#             if i==1 or i==mid or j==1:
#                 res+='*'+' '
#             else:
#                 res+=' '+' '
#         else:
#             if i==rows or j==rows:
#                 res+='*'+' '
#             else:
#                 res+=' '+' '
#     print(res)

# # *
# # *
# # * 
# # *
# # * * * * *

# rows=5
# for i in range(1,rows+1):
#     res=''
#     for j in range(1,rows+1):
#         if i==rows or j==1:
#             res+='*'+' '
#         else:
#             res+=' '+' '
#     print(res)
# print('  ')

# # *       * 
# # *       *
# # *       *
# # *       *
# # * * * * *

# rows=5
# for i in range(1,rows+1):
#     res=''
#     for j in range(1,rows+1):
#         if j==rows or j==1 or i==rows:
#             res+='*'+' '
#         else:
#             res+=' '+' '
#     print(res)
# print('  ')

# # * * * * *        
# # *       
# # *       
# # *       
# # * * * * *

# rows=5
# for i in range(1,rows+1):
#     res=''
#     for j in range(1,rows+1):
#         if i==rows or j==1 or i==1:
#             res+='*'+' '
#         else:
#             res+=' '+' '
#     print(res)
# print('  ')

# # *       *
# # *     *
# # *  *
# # *     *
# # *       *

# rows=5
# mid=(rows//2)+1
# for i in range(1,rows+1):
#     res=''
#     for j in range(1,rows+1):
#         if i<mid:
#             if j==1 or i+j==rows+1:
#                 res+='*'+' '
#             else:
#                 res+=' '+' '
#         else:
#             if j==1 or i==j:
#                 res+='*'+' '
#             else:
#                 res+=' '+' '
#     print(res)
# print('  ')

# # *       *
# #   *   *
# #     *
# #     *
# #     *

# rows=5
# mid=(rows//2)+1
# for i in range(1,rows+1):
#     res=''
#     for j in range(1,rows+1):
#         if i<mid:
#             if i==j or i+j==rows+1:
#                 res+='*'+' '
#             else:
#                 res+=' '+' '
#         else:
#             if j==mid:
#                     res+='*'+' '
#             else:
#                 res+=' '+' '
#     print(res)
# print('  ')

# *       * 
# * *   * * 
# *   *   *
# *       *
# *       *

# rows=5
# mid=(rows//2)+1
# for i in range(1,rows+1):
#     res=''
#     for j in range(1,rows+1):
#             if j==rows or j==1:
#                 res+='*'+' '
#             elif i<=mid and (i==j or i+j==rows+1):
#                 res+='*'+' '
#             else:
#                 res+=' '+' ' 
#     print(res)

#     * 
#    * * 
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# rows=5
# for i in range(1,rows+1):
#     res=''
#     for space in range(1,rows-i+1):
#         res+=' '
#     for j in range(1,i+1):
#         res+='*'+' '
#     print(res)
# rows=5
# for i in range(rows-1,0,-1):
#     res=''
#     for space in range(1,rows-i+1):
#         res+=' '
#     for j in range(1,i+1):
#         res+='*'+' '
#     print(res)

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# rows=5
# for i in range(1,2*rows):    ##2*5=10 (1 to 9 rows)
#     spaces=rows-i if i<=rows else i-rows
#     stars=i if i<=rows else i-(2*spaces)
#     res=''
#     for space in range(spaces):
#         res+=' '
#     for j in range(stars):
#         res+='*'+' '
#     print(res)

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# rows=5
# for i in range(1,2*rows):    ##2*5=10 (1 to 9 rows)
#     spaces=rows-i if i<=rows else i-rows
#     stars=i if i<=rows else i-(2*spaces)
#     print((' '*spaces+'*'*stars))

# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# rows=5
# for i in range(1,2*rows):
#     spaces=i-1 if i<=rows else 2*rows-i-1
#     stars=rows-i+1 if i<=rows else i-rows+1
#     print(' '*spaces+'* '*stars)

#     a 
#    b b 
#   c c c
#  d d d d
# e e e e e
#  f f f f
#   g g g
#    h h
#     i

# rows=5
# code=96
# for i in range(1,2*rows):    ##2*5=10 (1 to 9 rows)
#     spaces=rows-i if i<=rows else i-rows
#     stars=i if i<=rows else i-(2*spaces)
#     code+=1
#     print((' '*spaces+(chr(code)+' ')*stars))

#     a 
#    b c 
#   d e f
#  g h i j
# k l m n o
#  p q r s
#   t u v
#    w y
#     z

rows=5
code=97
for i in range(1,2*rows):    ##2*5=10 (1 to 9 rows)
    res=''
    spaces=rows-i if i<=rows else i-rows
    stars=i if i<=rows else 2*rows-i
    res+=' '*spaces
    for j in range(stars):
        res+=chr(code)+' '
        code+=1
    print(res)
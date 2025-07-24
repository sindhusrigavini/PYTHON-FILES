# 1. Reverse the list without using methods  

# l=[10,20,30,40,50]
# rev=[]
# for i in range(len(l)-1,-1,-1):
#     rev.append(l[i])
# print(rev)

# 2. Sort the list without using methods.

# l = [58, 24, 36, 56]
# for i in range(len(l)): 
#     for j in range(0, len(l)-i-1): 
#         if l[j] > l[j+1]:
#             l[j], l[j+1] = l[j+1], l[j] 
# print(l)
##using bubble sort

# 3. Remove duplicates in the list without using methods 

# l = [10,20,10,30,40,40,10,40,50,70,100]
# s = []
# for i in l:
#     if i not in s:
#         s += [i]
# print(s)


# 4.1) Print the largest value in every list and concate the list 
# Ex: [ [2,3,1], [4,5,3], [7,6,8] ] => o/p [3,5,8]


# a=[[1,2,3],[3,4,5],[6,7,8]]
# l=[]
# for i in a:
#     large=i[0]
#     for j in i:
#         if j>large:
#             large=j
#     l.append(large)
# print(l)


# 4.2) Sum of Every list
# Ex: [ [2,3,1], [4,5,3], [7,6,8] ] => o/p [3,5,8]

# a=[[1,2,3],[3,4,5],[6,7,8]]
# l=[]
# for i in a:
#     large=i[0]
#     for j in i:
#         if j>large:
#             large=j
#     l.append(large)
# print(l)
# sum=0
# for i in l:
#     sum+=i
# print(sum)
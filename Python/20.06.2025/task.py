# Practice problem solving on  list comprehension
# Rotate a list by k positions to the right.
# Example:
# Input: lst = [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]












# Remove all duplicates from a list without using set().
# Input: [1, 2, 3, 2, 1, 4, 5]
# Output: [1, 2, 3, 4, 5]

# l1=[1, 2, 3, 2, 1, 4, 5]
# l2=[]
# for i in l1:
#     if i not in l2:
#         l2 += [i]
# print(l2)


# Find all pairs in a list that sum up to a target.
# Input: lst = [2, 4, 3, 5, 7], target = 7
# Output: [(2, 5), (4, 3)]

# l1= [2, 4, 3, 5, 7]
# target = 7
# for i in range(len(l1)):
#     for j in range(i,len(l1)-1):
#         if l1[i]+l1[j]==7:
#             print([l1[i],l1[j]])

# Flatten a 2D list without using built-in flatten functions.
# Input: [[1, 2], [3, 4], [5]]
# Output: [1, 2, 3, 4, 5]

# l1=[[1, 2], [3, 4], [5]]
# l2=[]
# for i in l1:
#     for j in i:
#         l2+=[j]
# print(l2)


# Count the frequency of each element in a list and return a dictionary.
# Input: [1, 2, 2, 3, 1, 4, 2]
# Output: {1: 2, 2: 3, 3: 1, 4: 1}













# Part B: 
# Strings (5 Questions)
# Check if a string is a palindrome (ignoring spaces and case).
# Input: "A man a plan a canal Panama"
# Output: True


# s1 = "A man a plan a canal Panama"
# s2 = ""
# s3 = ""
# for i in s1:
#     if i == ' ':
#         continue
#     s2 = i.lower() + s2
# print('s2 is',s2)
# for j in s2:
#     s3=j+s3
# print('rev is:',s3)
# if s3==s2:
#     print(True)
# else:
#     print(False)
        


# Find the first non-repeating character in a string.
# Input: "aabbcdeff"
# Output: 'c'

# s="aabbcdeff"
# t=''
# for i in s:
#     if i not in t:
#         t+=i
# print(t) #abcdef
    


# Remove all vowels from a string.
# Input: "Hello World"
# Output: "Hll Wrld"

# s = "Hello World"
# v = "aeiouAEIOU"
# for i in s:
#     if i in v:
#         continue
#     print(i,end="")

# s="Hello World"
# v="aeiouAEIOU"
# d=""
# for i in s:
#     if i not in v:
#         d+=i
# print(d) 

# Count the number of words in a string without using .split().
# Input: "Python is great"
# Output: 3

# s = "Python is great"
# count = 1 # initially count taking as 1 because by default we take 1st word as 1
# for i in s:
#     if i == ' ':
#         count += 1
# print(count) 


# Find the longest word in a sentence.
# Input: "The quick brown fox jumps over the lazy dog"
# Output: "jumps"

# s="The quick brown fox jumps over the lazy dog"
# t=s.split()
# print(t)
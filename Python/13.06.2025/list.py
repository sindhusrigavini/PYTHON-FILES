# Even or Odd Checker:
# Take an integer as input and print whether it's even or odd.

def l(s):
    for i in s:
        if i%2==0:
            print('even')
        else:
            print('odd')
s=[100,203,300]
l(s)


# Sum of Digits:
# Given a number, find the sum of its digits (e.g., 123 ➝ 6).

def sum_digits(v):
    for i in v:
        sum=0
        while i>0:
            rem=i%10
            sum+=rem
            i=i//10
        print(sum)
v=[123,1234,122]
sum_digits(v)


# Count Vowels in a String:
# Input a string and count how many vowels it contains.



def vowel(v):
   vow="aeiouAEIOU"
   for i in v: #to get v
      count=0
      for j in i: # to get each letter in i
          if j in vow:
             count+=1
      print(count)
v=["apple","banana"]
vowel(v)



# Check Palindrome:
# Check if a given string or number is a palindrome (same forward and backward).

l=['sos','sindhu','madam']
def string(s):
    for i in s:
        rev=""
        for j in i:
            rev=j+rev
            if rev==i:
                print(rev,"palindrome")
            else:
                print(rev,"not a palindrome")
string(l)



# Find Maximum in a List:
# Given a list of numbers, find and print the maximum number.

li = [100, 50, 80, 155]
def max(l):
    m = 0
    for i in l:
        if i > m:
            m = i
    print(m)
max(li)
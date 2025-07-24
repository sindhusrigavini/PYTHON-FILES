# a=3
# b=3
# a**=b
# print(a)

# l=[1,2,3]
# if 5 not in l:
#     print(True)
# else:
#     print(False)
# a=(10)
# b=(10)
# print(id(a),id(b))
# print(a is not b)
# a=0b10101   #0b_ _ 101
# b=2
# print(a>>b)
# a=0b10101   #0b10101000
# b=3
# print(a<<b)
# a=10
# b=20
# res=a if a>b else b
# print(res)
# n=20
# res='even' if n%2==0 else 'odd'
# print(res)
# t=(1,2,3,3,3,4)
# print(t.count(3))
# t=(1,2,3,4,5)
# print(t.index(4))
# t=(1,2,3,4,5)
# print(max(t))
# s={}
# print(s)
# # print(type(s))
# p1={100,200,True,'Python'}
# p2=p1.union({300,400})
# print(p2)

# p1 = {100, 200, 300}
# p2 = {300, 400}
# result = p1.intersection(p2)
# print(result)
# p1={100,200}
# p2={300,400}
# print(p1.Symmetric_difference(p2))
# p1 = {100, 200,300,400}
# p2 = {300, 400,500}
# print(p1.symmetric_difference(p2))
# a=input()
# # print(type(a))
# a=eval(input())
# print(type(a))

# for i in range(1,10,2):
#     print(i)



# for i in range(10,1,-2):
#     print(i)



# for i in range(1,11):
#     print(i)



# for i in range(0,20,2):
#     print(i)



# s="PYTHON"
# for i in s:
#     print(i)



# n=int(input())
# for i in range(1,11):
#      print(n,"*",i,"=",n*i)

# sum=0
# for i in range(1,101):
#     sum=sum+i
# print(sum)

# vowels="aeiou"
# s="education"
# for i in s:
#     if i in vowels:
#         print(i)


# str="banana"
# for i in str:
#   i=str.count('a')
# print(i)

# count=0
# for i in range(1,11):
#     if(i%2!=0):
#         print(i)
#         count+=i
# print(count)            ###########odd




# count=0
# for i in range(1,11):
#     if(i%2==0):
#         print(i)
#         count+=i
# print(count)           ##########even



# a=int(input())
# b=int(input())
# if a>b:
#     print('a is greater')
# else:
#     print('b is greater' )



# a=int(input())
# b=int(input())
# c=int(input())
# if a>b and a>c:
#     print('a is greater')
# elif b>a and b>c:
#     print('b is greater')
# else:
#     print('c is greater')



# # n=int(input('Enter: '))
# # if n%400==0 or (n%4==0 and n%100!=0):
# #    print('leap year')
# # else:
# #    print('not a leap year')
# color = "blue"
# size = "medium"

# if color == "blue":
#     if size == "medium":
#         print("Buy")
#     else:
#         print("Size not available")
# else:
#     print("Color not available")

# for n in range(3,7):
#     is_prime = True 
#     for i in range(3, n):  
#         if n % i == 0:
#             is_prime = False  
#     if is_prime:
#         print(n, "is prime")
#     else:
#         print(n, "is not prime")


# def prime(r):
#     sum=0
#     for n in range(1, r+1):
#         count = 0
#         for i in range(1, n+1):
#             if n % i == 0:
#                 count += 1
#         if count == 2:
#             print(n)
#             sum+=n
#     print('sum of prime:',sum)
# prime(20)

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# Load dataset (assumes 'label' and 'message' columns)
df = pd.read_csv("spam.csv", encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'message']

# Convert labels to binary
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Text vectorization
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['message'])
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))


























































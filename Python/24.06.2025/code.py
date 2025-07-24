#  1. l = 5200
#  o/p : 10 500 notes 1 200 notes

l=5200
x=int(input('Enter the number of notes: '))
a=int(input('Enter what kind of note: '))
y=int(input('Enter the number of notes: '))
b=int(input('Enter what kind of note: '))
s=x*a
t=y*b
print(s+t)


#  2. p = ["Python", "java", "c++"]   # print only python from the list using tuple comprehension

p = ["Python", "java", "c++"]
result = tuple(x for x in p if x == 'Python')
print(result)

#  3. print prime numbers between 10 to 20 using tuple comprehension

prime_numbers= tuple(n for n in range(10, 21) if all(n % d != 0 for d in range(2, int(n ** 0.5) + 1)))
print(prime_numbers)

#  4. given a string "abcd" create a tuple of ASCII value of each character

s='abcd'
r=tuple(ord(i) for i in s)
print(r)

print('-------------')

r=tuple(ord(i) for i in 'abcd')
print(r)


#  5. l= [1,2,3,4,5,6]       o/p: [[1,2],[3,4],[5,6]]

l = [1, 2, 3, 4, 5, 6]
output = [l[i:i + 2] for i in range(0, len(l), 2)]
print(output)









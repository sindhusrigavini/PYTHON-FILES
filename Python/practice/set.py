# set stores only immutable data type

# s={}
# print(s)
# print(type(s))  #dict

# s={1}
# print(s)
# print(type(s))  #set

# t=set()
# print(t)
# print(type(t))   #set

# k={10,50,86}
# for i in k:
#     print(i)

# k={10,50,86}
# k.add(500)
# print(k)

# k={10,50,86}
# k.update({500,558,664})
# print(k)

# k={10,50,86}
# m={500,558,664}
# l=k.union(m)
# print(l)  ##all

# k={10,50,86}
# m={500,50,664}
# l=k.intersection(m)
# print(l)  ##common(&)

# k={10,50,86}
# m={500,50,664}
# l=k.symmetric_difference(m)
# print(l)

# k={10,50,86}
# m={500,50,664}
# l=k.difference(m)
# print(l)

# k={10,50,86}
# k.pop()
# print(k)

# k={10,50,86}
# k.remove(10)
# print(k)

# k={10,50,86}
# k.discard(20)
# print(k)  ##no error if no value in set or give value to discard

# k={10,50,86}
# l=k.copy()
# print(l)


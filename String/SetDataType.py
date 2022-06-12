from typing import Set


s1 = set([1,2,3])
s1

s2 = set("Hello")
s2

#중복 불가, 순서 불일치

l1 = list(s1)
l1
l1[0]

t1 = tuple(s1)
t1
t1[0]


s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
s1
s2
s1 & s2 #교집합
s1.intersection(s2) #교집합

s1 | s2 #합집합
s1.union(s2)    #합집합

s1 - s2 #차집합
s2 - s1

s1.difference(s2)
s2.difference(s1)

s1.add(10)
s1
s1.update([9,11,14])
s1

s1.remove(14)
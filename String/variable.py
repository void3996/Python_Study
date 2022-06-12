from re import A


a = 1
b = "python"
c = [1,2,3]

a = [1,2,3]
id(a)

a = [1,2,3]
b = a

id(a)
id(b)

a is b

a[1] = 4
b
a

b = a[:]  # a리스트 값을 바꾸더라도 b 리스트 그대로
a[1] = 2
a
b

from copy import copy
a = [1,2,3]
b = copy(a)

b

a is b

a, b = ('python', 'life')
a
b

(a, b) = 'python', 'life'
a
b

[a, b] = 'python', 'life'
a
b

a = b = 'python'
b
a

a = 3
b = 5
a, b = b,a
a
b

a = [1, 2, 3]
b = [1, 2, 3]
a is b
id(a)
id(b)




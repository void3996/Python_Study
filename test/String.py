print("Hello World")

print('Python is fun')

print("""Life is to short, You need python""")

print('''Life is to short, You need python''')

food = "Python's favorite food is perl"
print(food)

say = '"Python is very easy." he says.'
print(say)

food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

print(food)
print(say)

multiline = "Life is too short\nYou need python"
print(multiline)

multiline2 = '''
Life is too short
You need python
'''
print(multiline2)

multiline3 = """
Life is too short
You need python
"""
print(multiline3)

    #문자열 연산하기

head = "Python"
tail = " is fun!"
print(head + tail)

a = "python"
print("a*2 = ", a*2)

print("=" * 50)
print("My Program")
print("="*50)

    #문자열 길이 구하기
a = "Life is too short"
print("len(a) = ", len(a))

a = "You need python"
print("a의 문자열 길이는 ", len(a) ,"이다.")

    #문자열 인덱싱과 슬라이싱   

a = "Life is too short, You need Python"
print("a[3] = ", a[3])
    #파이썬은 0부터 숫자를 센다
print("a[12] = ", a[12])
print("a[-1] = ", a[-1])

print("a[0:4] = ", a[0:4])

a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print("date = ", date)
print("weather = ", weather)

a = "Pithon"
a[:1]
print(a[:1])
print(a[2:])

b = a[:1] + 'y' + a[2:]
print(b)

    #문자열 포매팅 따라하기
    #숫자 바로 대입
a = "I eat %d apples." % 3
print(a)

    #문자열 바로 대입
a = "I eat %s apples." % "five"
print(a)

    #숫자 값을 나타내는 변수로 대입
number = 3
a = "I eat %d apples." % number
print(a)

    #포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다                                                                                                                                                                                                              
a = "Error is %d%%." % 98
print(a)

    #포맷 코드와 숫자 함께 사용하기
    #1. 정렬과 공백
a = "%10s" % "hi"
print(a)

a = "%-10sjane" % 'hi'
print(a)

    #2. 소수점 표현
a = "%0.4f" % 3.42134234
print(a)

a = "%10.4f" % 3.42134234
print(a)


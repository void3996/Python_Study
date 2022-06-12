#파이썬 함수 구조

# def 함수 이름(매개변수):
#     수행할 문장1
#     수행할 문장2

from unittest import result


def add(a, b):
  return a + b
#함수 이름은 add 입력으로 2개 값을 받으며 결과값은 2개의 입력값을 더한 값


a = 3
b = 4
c = add(a, b)
print(c)

#매개변수(parameter)와 인수(arguments)
#매개변수는 함수에 입력으로 전달된 값을 받는 변수
#인수는 함수를 호출 할 때 전달하는 입력값

def add(a, b):  #a, b는 매개변수
    return a + b

print(add(3, 4)) #3, 4는 인수

#입력값과 결과값에 따른 함수의 형태
a = add(3, 4)
print(a)

#입력값이 없는 함수
 def say():
     return 'Hi'

a= say()
print(a)

#결과값을 받을 변수 = 함수 이름()

#결과값이 없는 함수
#함수이름(매개변수1, 매개변수2, ...)
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

a = add(3, 4)
print(a)   

#입력값도 결과값도 없는 함수
def say():
    print('Hi')

#함수 이름()
say()

#매개변수 지정하여 호출
def add(a, b):
    return a+b

result = add(a = 3, b = 7)  #a에 3, b에 7 전달
print(result)

result = add(b = 5, a = 3)
print(result)

#입력값 개수 모를 때
# def 함수 이름(*매개변수):
#     수행할문장

#여러개의 입력값 받는 함수만들기

def add_many(*args):  #*args는 변수명
    result = 0
    for i in args:
        result = result + i #args에 입력받은 모든 값 더하기
    return result

result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)


def add_mul(choice, *args):
    if choice == "add": #매개변수 choice에 'add'를 입력 받으면
        result = 0
        for i in args:
            result = result + i #args에 입력받은 모든 값을 더한다
    elif choice == "mul": #매개변수 choice에 'mul'을 입력 받으면
        result = 1
        for i in args:
            result = result * i #args에 입력받은 모든 값을 곱한다
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print(result)

#키워드 파라미터
#매개변수 앞에 **을 붙이면 딕셔너리가 되고 모든 key = value 형태의 결과값이
#그 딕셔너리에 저장됨
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)

print_kwargs(name = 'foo', age = 3)

#함수의 결과값은 언제나 하나이다
def add_and_mul(a,b):
    return a+b, a*b   #2개의 매개변수를 받아 더한 값과 곱한 값을 돌려준다

result = add_and_mul(3,4)
print(result)   #7, 12 라는 튜플 값을 갖게 됨

result1, result2 = add_and_mul(3, 4)

print(result1, result2)

def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." % nick)

say_nick('야호')
say_nick('바보')

#매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, True)
say_myself("박응용", 27, False)

#함수 안에서 선언한 변수의 효력 범위



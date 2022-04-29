    #format 함수를 사용한 포매팅
    #숫자 바로 대입

from tkinter import Y
from unicodedata import name


a = "I eat {0} apples".format(3)
print(a)

    #문자열 바로 대입

a = "I eat {0} apples".format("five")
print(a)

    #숫자 값 가진 변수 대입

number = 3
a = "I eat {0} apples".format(number)
print(a)

    #2개 이상 값 넣기

number = 10
day = "three"
a = "I ate {0} apples. so I was sick for {1} days".format(number, day)
print(a)

    #이름으로 넣기

a = "I ate {number} apples. so I was sick for {day} days.".format(number = 10, day = 3)
print(a)

    #인덱스와 이름 혼용

a = "I ate {0} apples. so I was sick for {day} days".format(10, day=3)
print(a)

    #왼쪽 정렬
a = "{0:<10}".format("hi")
print(a)

    #오른쪽 정렬
a = "{0:>10}".format("hi")
print(a)

    #가운데 정렬
a = "{0:^10}".format("hi")
print(a)

    #공백 채우기
a = "{0:=^10}".format("hi")
print(a)
a = "{0:!^10}".format("hi")
print(a)

    #소수점 표현하기
y = 3.42134234
"{0:0.4f}".format(y)
print(y)

    # {또는} 문자 표현하기

a = "{{ and }}".format()
print(a)

    #f 문자열 포매팅
name = '홍길동'
age = '30'
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

age = 30
print(f'나는 내년이면 {age+1}살이 된다.')

print(f'{"hi":<10}') #왼쪽 정렬  
print(f'{"hi":>10}') #오른쪽 정렬
print(f'{"hi":^10}') #가운데 정렬

print(f'{"hi":=^10}')   #가운데 정렬하고 = 문자로 공백채우기
print(f'{"hi":!<10}')   # 왼쪽 정렬하고 ! 문자로 공백채우기

y = 3.42134234
print(f'{y:0.4f}')  #소수점 4자리까지만 표현
print(f'{y:10.4f}') #소수점 4자리까지 표현하고 총 자릿수를 10으로 맞춤

print(f'{"python":!^12}')
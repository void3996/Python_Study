#문자열 관련 함수

from turtle import hideturtle


a = "hobby"
print(a.count('b')) #문자열 중 문자  b의 개수를 리턴

a = "Python is the best choice"
a.find('b')

#위치 알려주기2(index)

a = "Life is too short"
a.index('t')    #문자열중 t가 처음으로 나온 위치 반환

",".join("abcd")    #abcd 문자열 문자 사이에 , 삽입

",".join(['a','b','c','d'])

a = "hi"
a.upper()   ##소문자를 대문자로

a = "HI"
a.lower()   #대문자를 소문자로

a = " hi "
a.lstrip()  #왼쪽 공백 지우기

a = " hi "
a.rstrip()  #오른쪽 공백지우기

a = "Life is too short"
a.replace("Life", "Youg leg")   #replace(바뀌게 될 문자열, 바꿀 문자열)

a = "Life is too short"
a.split()   ##공백을 기준으로 문자열 나눔
b = "a:b:c:d"
b.split(':')    #기호를 기준으로 문자열 나눔




 
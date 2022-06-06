import re


test_list = ['one', 'two', 'three'] 
for i in test_list:
    print(i)

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a: #a 리스트 요소값이 튜플이기에 자동으로 변수 대입
    print(first + last)

marks = [90, 25, 67, 4, 80]
numb = 0  #학생에게 붙여줄 번호
for mark in marks:  #marks를 mark에 대입
    numb = numb + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % numb)
    else:
        print("%d번 학생은 불합격입니다." % numb)

marks = [90, 25, 67, 45, 80]        
numb = 0
for mark in marks:
    numb = numb + 1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % numb)

a = range(10) #0부터 10미만의 숫자를 포함하는 range 객체
a

a = range(1, 11)
a

add = 0
for i in range(1,11):
    add = add + i
    #print(add)

print(add)

marks = [90, 25, 67 ,45, 80]
for numb in range(len(marks)):
    if marks[numb] < 60: continue #marks가 60점 미만이면 맨 처음으로 돌아간다
    print("%d번 학생 축하합니다. 합격입니다." % (numb + 1))

add = 0
for i in range(1, 101):
    add = add + i

print(add)

for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end = " ")
    print('')
#매개변수 end 를 넣어준 이유 결과값을 출력할 때 다음 줄로 넘기지 않고 그 줄에 계속해서 출력하기 위함
#그다음 print('')는 2단, 3단 등을 구분하기 위해 두번째 for 문이 끝나면 결과값을 다음줄부터
#출력하게 해주는 문장

#리스트 내포

#a 리스트 각 항목에 3을 곱한 결과를 result 리스트에 담는 예제
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)

print(result)

result = [num * 3 for num in a]
print(result)

result = [x*y for x in range(2, 10)
    for y in range(1, 10)]
print(result)
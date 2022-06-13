#파일 읽고 쓰기

#파일 생성하기
from ast import Delete


f = open("새파일.txt", 'w')
f.close()

#파일 객체 = open(파일 이름, 파일 열기모드)

# r 읽기모드 - 파일 읽기만 할때 사용
# w 쓰기모드 - 파일에 내용을 쓸때 사용
# a 추가 모드 - 파일의 마지막에 새로운 내용 추가할때 사용

f = open("C:/python/새파일1.txt", 'w')
f.close()

f = open("C:/python/복습.txt", 'w')
f.close()

#파일을 쓰기 모드로 열어 출력값 적기

#프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법

#readline 함수 사용하기 - 읽기모드로 연 후 readline()으로 파일의 첫번째 줄을 읽어 출력

while 1:
    data = input()
    if not data: break
    print(data)
    break

#readlines 함수 사용하기 - 리스트로 돌려준다
f = open("C:/python/새파일2.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

#read 함수 사용하기 - 파일 전체 문자열로 돌려준다
f = open("C:/python/새파일2.txt", 'r')
data = f.read()
print(data)
f.close()

#파일에 새로운 내용 추가하기 

#with문과 함께 사용하기
f = open("새파일.txt", 'w')
f.write("Life is too shrot, you need python")
f.close()

with open("새파일.txt", "w") as f:
    f.write("Life is too short, you need python!!!!")
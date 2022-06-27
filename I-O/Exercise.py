#Q1 주어진 자연수가 홀수인지 짝수인지 판별해주는 함수(is_odd)를 작성해보자
from dataclasses import replace
from genericpath import exists
from unittest import result


def is_odd(number):
    if number % 2 == 1:
      return True
    else:
      return False

def is_odd2(number):
    if number % 2 == 1:
      return "홀수입니다."
    else:
      return "짝수입니다."

is_odd2(4)

#Q2 입력으로 들어오는 모든 수의 평균 값을 계산해주는 함수를 작성해 보자.
#(단 입력으로 들어오는수의 개수는 정해져있지않다.)

def avg_numbers(*avg):
    result = 0
    for i in avg:
        result += i
    return result/len(avg)

avg_numbers(1, 2)
avg_numbers(1,2,3,4,5)
avg_numbers(1,2,3,4,5,6,6,7,8,8)

#Q3 다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
total2 = input1 + input2
print("두 수의 합은 %s 입니다." % total)
print("두 수의 합은 %s 입니다." % total2)


#Q4 다음 중 출력 결과가 다른 것 한 개를 골라보자
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))

#Q5 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서
#출력하는 프로그램이다.

f1 = open("test.txt", 'w')
f3 = open("test1.txt", 'w')
f1.write("Life is too short")
f3.write("Life is too short")
f1.close()
f3.close()

f2 = open("test.txt", 'r')
f4 = open("test1.txt", 'r')
print(f2.read())
print(f4.read())
#f2.close()

#Q6 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자.(단 프로그램을 다시 실행하더라도
# 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)

user_input = input("저장할 내용을 입력하세요:")
f = open('test1.txt', 'a') #내용을 추가하기 위해 'a'를 사용
#f.write("\n")
f.write(user_input)
#f.write("\n")     #"개행"
f.close()   


#Q7 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 'java'라는 문자열을
#'python'으로 바꾸어서 저장해 보자

f = open('test1.txt', 'r')
body = f.read()   #test.txt 파일의 내용을 body 변수에 저장
f.close()

with open('test1.txt', 'r') as f:
  body = f.read()

with open('test1.txt', 'r') as f:
  body = f.read()


body = body.replace('climbing', 'Life')
#id(body)

f = open('test1.txt', 'w')
f.write(body)
f.close()

with open('test1.txt', 'w') as f:
  f.write(body)



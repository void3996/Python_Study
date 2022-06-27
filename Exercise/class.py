#Q1
class Calculator:
  def __init__(self):
    self.value = 0
  
  def add(self, val):
    self.value += val

class UpgradeCalculator(Calculator):
  def minus(self, val):
    self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

#Q2
class MaxLimitCalculator(Calculator):
  #def __init__(self):
  #  self.value = 0
  
  def add(self, val):
    self.value += val
    if self.value > 100:
        self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

#Q3
all([1, 2, abs(-3)-3])  #False
chr(ord('a')) == 'a'  #True

#Q4
list(filter(lambda x:x>0, [1, -2, 3, -5, 8, -3]))

#Q5
int('0xea', 16)

#Q6
list(map(lambda x:x*3, [1, 2, 3, 4]))

#Q7
a = [-8, 2, 7, 5, -3, 5, 0, 1]
max(a) + min(a)

#Q8
round(17/3, 4)

#Q9
import numbers
import sys
from unittest import result

numbers = sys.argv[1:]

result = 0
for number in numbers:
    result += int(number)
print(result)

#Q10 os모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해보자
#C:\doit 디렉터리로 이동한다
#dir 명령을 실행하고 그 결과를 변수에 담는다
#dir 명령의 결과를 출력한다

import os
os.chdir("C:\Python\Exercise")  #디렉터리 위치 변경하기
result = os.popen("dir")    #실행한 시스템 명령어의 결과값 돌려받기
print(result.read())    #객체 내용 보기

#Q11 glob 모듈을 사용하여 C:\doit 디렉터리의 파일 중 확장자가 .py인 파일만
#출력하는 프로그램을 작성해보자

import glob
glob.glob("C:\Python\Exercise\*.py")  #디렉터리에 있는 파일들을 리스트로 만들기

#Q12 time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해보자
import time
time.strftime("%Y/%m/%d %H:&%M:%S") 

#random 모듈을 사용하여 로또 번호 1~45 사이의 숫자 6개를 생성해보자

import random

r = []
while len(r) < 6:
    num = random.randint(1, 45) # 랜덤 난수 발생
    if num not in r:  #중복되지 않을 경우에만 append
      r.append(num)

print(r)
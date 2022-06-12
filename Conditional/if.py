from ast import If


money = True
if money: #money가 True 면 "택시를 타고 가라"
    print("택시를 타고 가라")
else:   #money가 False 면 "걸어가라"
    print("걸어가라")

#비교 연산자
x = 3
y = 2
x > y
x < y
x == y
x != y

money = 2000
if money >= 3000: #money가 3000 이상이면 "택시를 타고가라"
    print("택시를 타고가라")
else:   #아니면 "걸어 가라"
    print("걸어 가라")

money = 2000
card = True
if money >= 3000 or card: #money가 3000 이상 또는 card일 경우 "택시를 타고 가라"
    print("택시를 타고 가라")
else:
  print("걸어가라")

1 in [1,2,3,]
1 not in [1,2,3]

'a' in ('a','b','c')
'j' not in 'python'

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket: #'money'가 pocket 안에 있다면 "택시를 타고가라"
    print("택시를 타고 가라")
else:
    print("걸어가라")

if 'card' in pocket:
    print("버스를 타고 가라")
else:
    print("걸어 가라")

if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket: 
    print("택시를 타고 가라")
else:
  if card:
      print("택시를 타고가라")
  else:
      print("걸어가라")

if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

if 'money' not in pocket: pass
else: print("카드를 꺼내라")

if score >= 60:
    msg = "success"
else:
    msg = "failure"
#key value

from concurrent.futures.process import _python_exit
from unicodedata import name


dic = {'name':'pey','phone':'01199993323','birth':'1118'}

a = {1:'hi'}

a = {'a' : [1,2,3]}

a[2] = 'b' #추가

del a['a']
a

a[1] = 'a'

a

grade = {'pey': 10, 'julliet': 99}
grade['pey']    #Value인 10을 반환
grade['julliet']

#key는 고유값 중복될경우 1개를 제외한 나머지  Key는 무시됨

a = {'name':'pey', 'phone': '01199992222', 'birth':'1118'}
a.keys()    #Key만 모아서 dict_keys 객체 반환



for k in a.keys():
  print(k)



list(a.keys())

#Value 리스트 만들기
a.values()

#Key, Value 쌍 얻기
a.items()   #튜플로 묶은 값을 dict_items 객체로 돌려준다

a.clear()   #모두 지우기
a

a.get('name')
a.get('phone')

print(a.get('nokey'))

a.get('foo', 'bar') #찾는 키가 없을때는 지정한 value를 반환

'name' in a
#찾는 키가 있으면 True 반환, 없으면 False

bool([1,2,3])
bool([])
bool(0)
bool(3)
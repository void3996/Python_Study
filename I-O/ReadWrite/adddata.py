f = open("C:/python/새파일2.txt", 'a')
for i in range(11, 20): #11브터 19까지 i에 대입
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()
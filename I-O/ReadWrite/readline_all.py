f = open("C:/python/새파일2.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

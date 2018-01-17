f = open("c01.txt","rb")
f.seek(0)

while 1:
    b = f.read(1)
    if not b:
        break
    print hex(ord(b))
    print chr(ord(b))
f.close()

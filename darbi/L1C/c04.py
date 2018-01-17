q = open("c03.txt","rb")
q.seek(0)

while 1:
    w = q.read(1)
    if not w:
        break
    print hex(ord(w))
    print chr(ord(w))
q.close()

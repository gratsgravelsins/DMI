f = open("meta.bin","rb")
f.seek(0)
while 1:
    b = f.read(1)
    if not b:
        break
    print hex(ord(b))
    print chr(ord(b))
f.close()

d = open("data.bin","rb")
d.seek(0)
while 1:
    b = d.read(1)
    if not b:
        break
    print hex(ord(b))
    print chr(ord(b))
d.close() 

"""
Fails: c01.py
Autors:
Datums:
Tiek izveidots tukshs fails c01.txt
Failu aizpilda ar tekstu. Tekstu modificee. Failu aizver
"""
fn = 'c01.txt' # define faila nosaukumu
f = open(fn,"w") # atver failu rakstit un lasit
print f.tell() # pateikt atrashanas vietu failaa
f.write("Python ir asakains\n") # failaa ieraksta simbolu virkni
f.seek(7) # rakstaamgalvu novieto 7. pozicija
f.write("- p")
f.close() # Failu aizver ciet!
print "Darbs ar failu pabeigts"

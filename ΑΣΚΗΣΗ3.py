newlines=[]
f =open("ΑΣΚΗΣΗ3ΑΡΧΣΧΟΛ.py","r")
lines = f.readlines()
f.close()
for x in lines:
    if x[0] != "#":
        newlines.append(x)
f=open("Α3ΑΡΧΣΧΟΛ2.py","w")
for i in newlines:
    f.write(i)
f.close()

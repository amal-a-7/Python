fo=open("v1.txt","r")
line=fo.read(5)
print("Read Line:",line)
fo.seek(0,0)
line=fo.read(5)
print("Read Line:",line)
fo.close()


with open("v1.txt","r")as f:
    with open("v2.txt","w")as f1:
        lines=f.readlines()
        for i in range(0,len(lines)):
            if i%2!=0:
                l=f1.write(lines[i])
f=open("v2.txt","r")
cont=f.read()

 with open("v1.txt","r")as fo:
     lines=fo.readlines()
     
 print("Original lines:",lines)
 
 stripped_lines=[line.strip() for line in lines]
 print("Stripped lines:",stripped_lines)

                or

print([line.rstrip() for line in open('v1.txt','r')])  ///single line code///



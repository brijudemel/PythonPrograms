f=input("Input the Filename: ").split(".")
d={'py':'python','c':'c','cpp':'c++','java':'java','txt':'text','doc':'Microsoft Word file','docx':'Microsoft Word file','pdf':'Pdf','sql':'sql database','xml':'XML','html':'HTML','csv': 'Comma separated value file',}
print("The extension of the file is : '",d[f[-1]],"'")

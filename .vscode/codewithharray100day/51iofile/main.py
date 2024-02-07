# with open('file.txt','r') as f:
#    print(type(f)) 

with open('file.txt','r') as f:
    f.seek(5)
    data = f.read(5)
    print(data)
    print(f.tell())

import random
import string

code = input("Enter Your coding or decoding")
Decide = input("Coding for c or decoding for d")
arr = code.split(" ")
dw = []
if(Decide == 'c'):
     for i in arr:
        if len(i)>=3 :
            ran1 = ''.join(random.choice(string.ascii_letters) for _ in range(3))
            ran2 = ''.join(random.choice(string.ascii_letters) for _ in range(3))
            nwi = i[1:]+i[0]
            dw.append(ran1+i[::-1]+ran2)
        else:
            dw.append(i[::-1])
else:
    for i in arr:
        if len(i)>=3:
            final = i[3:-3]
            final = final[::-1]
            dw.append(final)
        else:
           dw.append(i[::-1])




           
            


print(" ".join(dw))



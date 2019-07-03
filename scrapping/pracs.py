a=[1,2,3]
i=0
#while(len(a)):
#for i in range(len(a)):
b=0
while(len(a)):
    b=b+1
    for i in a:
        print(a)
    a.append(b+4)
    if(b==3):
        a.clear()
    

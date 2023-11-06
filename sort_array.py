l = [0,1,2,0,2,1,0,1]


for i in range(0,len(l)):
    
    for j in range(i,len(l)):
     
        if(l[i]>l[j]):
           l[i],l[j] = l[j],l[i]
           
        

print(l)

print("prime numbers between 100 and 500 :")
for i in range(100,501,1):
    t=0
    for j in range(1,i+1,1):
        if i%j==0:
            t+=1
    if t==2:
        print(i)
        
        

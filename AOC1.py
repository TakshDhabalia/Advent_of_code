import numpy as np 
fresult= 0
with open('a.txt', 'r') as f:
    ct= 0 
    temp = 0
    for i in range(0,1000,1):    
        line = f.readline()
        str1 = str(line)
        str2 = reversed(str1)
        for chr in str1: 
            temp = [-1,-1,-1,]
            if chr.isnumeric() == True:
                a = 0
                temp[a] = int(chr)  
                a = a+1
                
                #print(temp[0], temp[-1])
                break  
        for chr in str2: 
            temp2 = [-1,-1,-1,]
            if chr.isnumeric() == True:
                b = 0
                temp2[b] = int(chr)  
                b = b+1
                
                #print(temp2[0], temp2[-1])
                break  
        #print(line)
        print(temp[0], temp2[0])
        result = (temp[0])*10 + temp2[0]
        fresult += result
    print(fresult)
f.close()
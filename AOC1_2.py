import numpy as np 
fresult= 0
number_dict = {'1':'one',
               '2':'two',
               '3':'three',
               '4':'four',
               '5':'five',
               '6':'six',
               '7':'seven',
               '8':'eight',
               '9':'nine'
}
with open('a.txt', 'r') as f:
    ct= 0 
    temp = 0
    temp2 = 0
    for i in range(0,1000,1):    
        line = str(f.readline())
        str1 = str(line)
        str2 = reversed(str1)
        for chr in str1: 
            temp = [-1,-1,-1,]
            for i in range(0,9,1):
                if number_dict.get("i") in line is not None :
                    a = 0
                    temp[a] = int(chr)  
                    a = a+1
                
                    #print(temp[0], temp[-1])
                    break  
             
                elif chr.isnumeric() == True:
                    a = 0
                    temp[a] = int(chr)  
                    a = a+1
                    
                    #print(temp[0], temp[-1])
                    break  
        for i in range(0,9,1):
                if number_dict.get("i") in line is  not None :
                    b = 0
                    temp2[b] = int(chr)  
                    b = b+1
                
                    #print(temp[0], temp[-1])
                    break  
             
                elif chr.isnumeric() == True:
                    b = 0
                    temp2[b] = int(chr)  
                    b = b+1
                    
                    #print(temp[0], temp[-1])
                    break
        #print(line)
        print(temp[0], temp2[0])
        result = (temp[0])*10 + temp2[0]
        fresult += result
    print(fresult)
f.close()
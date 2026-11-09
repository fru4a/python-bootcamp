
#def prime (n):

    #x=0
    #for i in range(2,n+1) :
        
        #if n % i == 0 :
            #x=x+1
    #if x == 1:
        #return True
    #else :
        #return False
#print(prime (10))
   
 
def prime (n):
    if n < 2 :
        return False
    for i in range (2,n-1):
        if n % i == 0:
            return False
    else: return  True
print(prime (1))


  
     


           



 


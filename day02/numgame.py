import random
secret = random.randint(1, 10 )
def numgame():
    i=0

    while i < 5 :

        n = int(input("donner moi un nombre n"))

       
        if secret == n :
         return "correct"
        elif  secret < n :
       

          print("lower")
        else : 
          print ("higher")
        i=i+1
    return f"Loser! The number was {secret}"

           
           
print(numgame())
    


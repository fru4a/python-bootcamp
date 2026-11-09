#def sum_digits (n :int) :
    

 #   x = 0
  #  for i in str(n) :
   #     x = x + int(i)
    #print(x)
        

#sum_digits(59)

def sum_digits(n):

    t = 0;
    while n> 0 :
        x= n % 10
        t = t+x
        n = n // 10
    return t

print(sum_digits(3))



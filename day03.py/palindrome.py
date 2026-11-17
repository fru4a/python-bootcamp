def is_palindrome():

    s = str(input("give me a word").lower())
    n=""
    for i in reversed(s) :
        n=n+i
    s=s.replace(" ","")
    n=n.replace(" ","")
    if n == s :
        return True
    else : 
        return False
print(is_palindrome())    






#maram --> maram
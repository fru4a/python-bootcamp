def  count_vowels():
    s = str (input("give me a word ").lower())
    c = 0
    for i in s :
        
        if i in ("a", "e", "i", "o", "u"):
            c=c+1
    return c 
        
print(count_vowels())

#(a, e, i, o, u)
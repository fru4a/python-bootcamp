def is_anagram(a,b):
    a = sorted(a.lower().replace (" ",""))
    b = sorted(b.lower().replace (" ",""))
    
   
    
    
    if (len(a)==len(b)) and a ==b : 
        return True
    else : return False

print(is_anagram("listen", "silent"))        
print(is_anagram("hello", "world"))          
print(is_anagram("Dormitory", "dirty room")) 
print(is_anagram("abc", "abcd"))             
print(is_anagram("aab", "abb"))              
print(is_anagram("", "")) 
        

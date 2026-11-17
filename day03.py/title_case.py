def title_case(sentence) : 
    sentence = sentence.lower().split()
    for i in range(len(sentence)):
       
       #sentence[i] = sentence[i].sentence[0].upper()
        sentence[i] = sentence[i][0].upper() + sentence[i][1:]
    
    
    return " ".join(sentence)
print(title_case("hello big world"))    # Hello Big World
print(title_case("pYTHON is fun"))      # Python Is Fun
print(title_case("a"))                  # A
print(title_case(""))                   # (empty string)
print(title_case("  many   spaces ")) 
    
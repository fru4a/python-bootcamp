def count_words(sentence) : 
    c=0
    sentence = sentence.split()
    for i in sentence : 
        c=c+1
    return c
print(count_words("the quick brown fox"))     # 4
print(count_words("  lots   of   spaces  "))   # 3
print(count_words("hello"))                    # 1
print(count_words(""))                         # 0
print(count_words("   "))                      # 0

    




def word_frequency(sentence):
    sentence = sentence.lower().split()
    counts ={}
    for i in sentence :        
        counts[i] = counts.get(i, 0) + 1
    return counts
print(word_frequency("firas firas asrif MANSOUR"))
print(word_frequency("15 45 45"))

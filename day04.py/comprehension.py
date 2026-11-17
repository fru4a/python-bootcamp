#lengths = {}
#for word in ["apple", "kiwi", "banana"]:
 #   lengths[word] = len(word)
#print(lengths)    # {'apple': 5, 'kiwi': 4, 'banana': 6}


#result = []
#for w in ["sun", "moon", "star", "sky", "planet"]:
 #   if len(w) > 3:
  #      result.append(w.upper())
#print(result)    # ['MOON', 'STAR', 'PLANET']
result = [ n * n for n in range(1,11)  if n % 2==0]
print(result) 
lengths ={word:len(word) for word in ["apple", "kiwi", "banana"]  }
print(lengths)

resultt =[ w for w in ["sun", "moon", "star", "sky", "planet"] if len(w) > 3]
print(resultt) 

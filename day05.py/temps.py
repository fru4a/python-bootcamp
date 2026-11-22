#import json
#city = {"city": "Tunis", "temps": [18, 22, 25]}
#with open("city.json", "w") as f:
 #   json.dump(city, f, indent=2)
#with open("city.json") as f :
 #   json.load(f)
  #  total = 0

   # for i in city["temps"] :
         
    #    total= total+i 
    #avg  = total / len(city["temps"])

#print(avg)
import csv
with open("people.csv", newline="") as f:
    reader = csv.DictReader(f)
    sum =0
    for row in reader:
        #print(row)
        sum= sum + int(row["age"])
    print(sum) 



 
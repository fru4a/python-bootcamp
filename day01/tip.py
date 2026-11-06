bm = float(input("give me the bill amount bm :"))
tp = float(input("give me the top percentage: "))
if (bm < 0) or (tp < 0) : 
    print ("error")
else:
    tip = bm * (tp / 100)
    total = tip + bm 
    print(f"tip amount is :{tip:.2f}")
    print(f"total is :{total:.2f}")

      
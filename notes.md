-type : to see the type of the input
- str + int --> error
-break: you said it ends or quits the function. Close, but it ends the loop, not the function
-continue: you said it continues the function. It’s closer to the opposite of what that sounds like: it skips the rest of the current round and jumps to the next one of the loop.
for i in range(5):
    if i == 2:
        continue
    print(i)
output : 0 1 3 4 (2 is skipped, but the loop goes on)
-return f"one for {name}, one for me"
f make the {name} appear as a real name named in the function 
- print(f"{n} * {i} = {n *i} " )
f make the n and i appear as numbers and let the calculation work inside the {}
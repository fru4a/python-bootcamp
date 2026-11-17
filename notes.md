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
- print = the machine shows something on the screen. You can read it, but the program can’t use it afterwards.
- return = the machine hands you a value. You can store it, calculate with it, or print it later.
exemple :
def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

x = add_print(2, 3)     # screen shows 5, but x is None
y = add_return(2, 3)    # screen shows nothing, y is 5

print(y + 10)           # 15, this works
print(x + 10)           # TypeError: None + 10
-split cuts a string into a list, and join glues a list back into a string.
-(" firas mansour  ".split()) ---> ['firas', 'mansour']
-" ".join(['firas', 'mansour']) --> firas mansour
-List[] = mutable / Duplicates are allowed , tuple() = immutable/ Duplicates are not allowed / set {} =mutable /Duplicates are not allowed 
Both can contain any type and duplicates
-.split(): use it to count the number of the words in a list
-A comprehension is a shorter way to write a loop that builds a collection
-dict: .keys() → returns keys.
.values() → returns values.
.items() → returns both keys and values.
*exception :
-Error in try: skip the rest, jump to the matching except, then continue after it.
try:
    print("A")
    int("abc")      # error here
    print("B")      # skipped
except ValueError:
    print("C")
print("D")          # still runs
-else = no error, finally = always.
-raise = make an error on purpose.
-file :
read() returns one string with the whole file / readlines() returns a list of strings
Use read() when you want the whole text, and readlines() or for line in f when you want to process line by line.
-json files :
*A .json file contains data saved as text
*Save with json.dump(data, f) before the program ends.
*Load with json.load(f) the next time the program starts, and you have your data back.
**f.read(): the file’s text, as a string.
**json.load(f): the file’s text converted into a Python dictionary or list.
**json.load looks at what the JSON text represents and gives you the Python equivalent(int , str, dict, ..)
read[0]--> M (print as strin sdld dldl slkd)
load["name"]= ali (print as a dict)
-Exception handling (try/except) lets you handle errors without crashing your program.
-dump/load = file, dumps/loads = string.
-dumps: dict to JSON text. loads: JSON text to dict.
coclusion ::
-dump/load work with a file on disk, and dumps/loads work with a string in memory (RAM). One precision: dumps gives you a string, and loads takes a string. The string lives in a variable, so you can then print it, send it, or save it yourself.
-indent=2 = pretty printing: same data, nicer layout in the file.
**csv :
-CSV is text, so every value is read as a string. Convert with int() or float().
-writeheader writes the column names line, writerows writes one line per dictionary.
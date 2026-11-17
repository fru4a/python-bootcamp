
#with open("simplee.txt", "w") as f:
    #f.write("the quick brown fox\n")
    #f.write("jumps over\n\n")
    #f.write("the lazy dog\n")
try:
    def file_stats(filename):
        with open(filename) as f:
            content = f.readlines()

        chars = 0
        words = 0

        for line in content:
            chars = chars + len(line)
            words = words + len(line.split())

        return len(content), words, chars
    print(file_stats("simplee.txt"))

except FileNotFoundError:

    print("none")


        
        
    



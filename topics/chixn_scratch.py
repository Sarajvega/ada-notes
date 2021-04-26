def reverse_str(str):
    n = len(str)
    reverse = ""
    i = 0
    x = -1
    while i < n:
        val = str[x]
        reverse += val
        print(reverse)
        i+=1
        x -=1

word = "racecarx"
reverse_str(word)
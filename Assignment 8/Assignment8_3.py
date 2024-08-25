def Pattern(n):
    if n == 0:
        return
    else:
        print(n,end="")
        Pattern(n - 1)
        
n = 5
Pattern(n)
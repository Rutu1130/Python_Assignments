def Pattern(n):
    if n == 0:
        return
    else:
      
        Pattern(n - 1)
        print(n,end="")
n = 5
Pattern(n)
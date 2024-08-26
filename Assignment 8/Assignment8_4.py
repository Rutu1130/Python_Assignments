def Sum(n):

    if n < 10:
        return n
    else:
        
        lastNum = n % 10
        remainingNum = n // 10
        return lastNum + Sum(remainingNum)

num = int(input("Enter a number: "))
result = Sum(num)
print("Summmation is :", result)
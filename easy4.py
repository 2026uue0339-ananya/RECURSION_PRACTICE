#Q4. What value does this program print?

def total(n):
    if n ==0:
        return 0

    return n +total(n-1)

print(total(5)) #it will print the sum of first 5 natural numbers
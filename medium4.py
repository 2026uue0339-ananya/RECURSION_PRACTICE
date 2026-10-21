#Q8. Using the GCD function below, what does gcd(36, 24) return? Show the full 
# sequence of calls (for example, gcd(36, 24) -> gcd(24, 12) -> ...).

def gcd(a,b):
    if b==0: 
        return a

    print(a,",", b) #to show the sequence of gcd
    return gcd(b, a%b)

    

print(gcd(36,24))
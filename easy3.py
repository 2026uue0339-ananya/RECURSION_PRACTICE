#Q3. In the function below, write down which line is the base case and which line is 
# the recursive case, and explain in one sentence what the base case is for.

def fact(n):
    if n ==0: #n = 0 is the base case afte n become zero it will return 1
        return 1

   # this is the recursion , whatever n is except 0 it will multiply with n-1 simultaneously until each reaches the base case 
    return n * fact(n-1) 

print(fact(5))
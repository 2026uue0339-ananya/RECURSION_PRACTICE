#Q7. The function below is meant to return the sum of all numbers in a list, 
# but it always returns 0. Find the bug, explain why it happens, and write the corrected 
# function.

def list_sum(a):
    if not a:
        return 0

    #return list_sum(a[1:]) here it was returning 0 
    return a[0]+list_sum(a[1:]) #this is the corrected form beacause in th previous case function itself don't know what to do in list sum . now it knows to add from first element upto last and created recursion

b = [50, 40 , 30]

print(list_sum(b))
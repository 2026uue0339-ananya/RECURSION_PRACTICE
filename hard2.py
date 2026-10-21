#Q10. Write a recursive function power(base, exp) that computes base raised to the 
# power exp (assume exp is 0 or a positive integer). Example: power(3, 4) should return 81. 
# Then answer: how many times is power called in total (including the first call) when you 
# evaluate power(3, 4)? Explain your count.

count = 0
def power(base, exp):

    global count

    count+=1

    if exp == 0:
        return 1 #base case

    
    print(base,exp)
    
    return base * power(base, exp-1) #recursion
    
print(power(3,4))
print("no of times power function is called = ",count)
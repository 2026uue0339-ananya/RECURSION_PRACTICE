#Q1. What is the exact output of this program?

#define function
def greet(n):
    if n == 0: #define 0 as base case
        return

    print("namaste")
    greet(n-1) #to count until the base case

greet(3)    #call greet function
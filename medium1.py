#Q5. What is the exact output of this program? (Watch where the print sits.)

def show(n):
    if n==0: #define a base case
        return

    show(n-1) #it will run until base case reaches
    print(n) #will show number in ascending order

show(4)    
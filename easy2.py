#Q2. Write a recursive function count_up(n) that prints the numbers from 1 to n, 
# each on its own line. Example: count_up(4) should print 1, 2, 3, 4 (in that order).

def count_up(n):

    if n ==0: #define the base case
        return 

    #count upto base case base case
    count_up(n-1)
    #to print in ascending order
    print(n)
    
    

count_up(4)  


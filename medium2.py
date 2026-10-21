#Q6. Write a recursive function digit_sum(n) that returns the sum of the digits of 
# a non-negative integer. Example: digit_sum(2025) should return 9
#  (because 2 + 0 + 2 + 5 = 9).

def digit_sum(n):

#it will return the same no if it is unit digit n

    if n < 10:
        return n

#like 2025 %10 = 5, 2025-5//10 = 202 ,will apply same function to create recursion
    return n%10 +digit_sum((n - n%10)//10)

print(digit_sum(2025))
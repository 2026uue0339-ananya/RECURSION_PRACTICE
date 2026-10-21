#Q9. Write a recursive function is_palindrome(s) that returns True if a string reads 
# the same forwards and backwards, and False otherwise. Examples: is_palindrome("NITIN") 
# -> True; is_palindrome("INDIA") -> False. (State your base case clearly.)

def is_palindrome(s):

#when 1 or no letter will left it will stop checking
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])

print(is_palindrome("NITIN"))
print(is_palindrome("INDIA"))
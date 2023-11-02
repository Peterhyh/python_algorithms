def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)  #This recursion causes the n to be multiplied to all the numbers lower than it.

    
n = 7

x = factorial(n)

print(x)                             #If n is 7, the answer would be 5040
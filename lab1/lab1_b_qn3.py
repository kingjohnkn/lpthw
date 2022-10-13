# This function computes the factorial of the number entered by a user
# modified 'fact = fact * factor' to 'fact = fact * 5'

def factor():
    
    n = int(input("Please enter a whole number: "))
    fact = 1
    for factor in range(1, n+1):
        # fact = fact * factor
        fact = fact * 5

    print("The factorial of", n, "is", fact)


factor()

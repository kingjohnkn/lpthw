# This function computes the factorial of the number entered by a user

def main():
       
    n = int(input("Please enter a whole number: "))
    fact = 1
    for factor in range(1, n+1):
        fact = fact * factor
    print("The factorial of", n, "is", fact)

main()



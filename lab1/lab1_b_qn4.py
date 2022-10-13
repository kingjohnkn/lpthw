# lab1_b_qn4.py
#   A Program that finds the sum of numbers from 1 - 1000
#   using a for loop

def main():
    
    sum = 0
    n = 1000

    for number in range(n + 1):
        sum = sum + number

    print()
    print(f"The sum of number 1 to {n} is {sum}")


main()

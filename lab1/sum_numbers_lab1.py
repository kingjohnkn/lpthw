# sum_five_numbers_lab1.py
# A program that inputs 5 numbers from the user in a loop and finds the sum of the numbers

# ask user to imput the numbers
# loop through the numbers and calculate sum
# output the sum

def main():
    print()
    print("Enter five numbers")
    
    n = 5
    sum = 0
    
    for i in range(n):
        number = int(input(f"Enter number {i + 1} > "))
        sum = sum + number

    print()
    print(f"The sum of the {n} numbers is {sum}")

    
main()

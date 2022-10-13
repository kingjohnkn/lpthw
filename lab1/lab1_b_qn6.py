# sum_average_numbers_lab1.py
# A program that inputs 5 numbers from the user in a loop and finds the sum of the numbers

# ask user to imput the numbers
# loop through the numbers and calculate sum
# calculate average
# output the sum and average

def main():
    print()
    print("Enter five numbers")
    
    n = 5
    sum = 0
    
    for i in range(n):
        number = int(input(f"Enter number {i + 1} > "))
        sum = sum + number

    average = sum / n

    print()
    print(f"The sum is {sum} and average is {average}")

    
main()

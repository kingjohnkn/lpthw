def main():
    """While loop function"""
    
    to_what = int(input("Enter a number: "))
    increase = int(input("Increment by?: "))
    i = 0
    numbers = []

    while i < to_what:
        print(f"At the top is {i}")
        numbers.append(i)

        i += increase
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

main()

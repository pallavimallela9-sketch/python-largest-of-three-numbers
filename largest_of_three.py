# Program: Find Largest of Three Numbers
# Author: M.Pallavi

def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


def main():
    print("===================================")
    print("     LARGEST OF THREE NUMBERS")
    print("===================================")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))

        largest = find_largest(num1, num2, num3)

        print("\nNumbers Entered:")
        print("First Number  :", num1)
        print("Second Number :", num2)
        print("Third Number  :", num3)

        print("\nLargest Number:", largest)

        if num1 == num2 == num3:
            print("All three numbers are equal.")
        elif num1 == num2 or num1 == num3 or num2 == num3:
            print("Two of the numbers are equal.")

    except ValueError:
        print("\nInvalid input!")
        print("Please enter numeric values only.")


if __name__ == "__main__":
    main()

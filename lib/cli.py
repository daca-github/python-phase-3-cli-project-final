#!/usr/bin/env python3

def main():
    try:
        # Prompt user for a number
        number = float(input("Enter a number: "))

        # Calculate the square of the number
        result = number * number

        # Print the result
        print(f"The square of {number} is: {result}")

    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on October 2020
# This program finds the product of all natural numbers preceding the
#     number inputted by the user (a.k.a. Factorial)


def main():
    # This function finds the product of all natural numbers preceding the
    #     number inputted by the user (a.k.a. Factorial)

    # Input
    counter = 1
    product = 1
    natural_string = input("Enter a natural number (To Find Product 1 to N): ")
    print("")

    # Process & Output
    try:
        natural_integer = int(natural_string)
    except Exception:
        print("You have not inputted an integer, please input an integer"
              " (natural number)!")
    else:
        if natural_integer <= 0:
            print("You have not inputted a positive number, please input a"
                  " positive number!")
        else:
            while counter <= natural_integer:
                product = product * counter
                counter = counter + 1
            print("The product of all natural numbers 1 to {0} is {1}"
                  .format(natural_integer, product))


if __name__ == "__main__":
    main()

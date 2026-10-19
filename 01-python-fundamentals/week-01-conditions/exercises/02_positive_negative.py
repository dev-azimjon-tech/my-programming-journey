"""Exercise 2: classify a number as positive, negative, or zero."""
# TODO: handle all three cases: positive, negative, and zero.
number = float(input("Enter a number: "))

if number > 0:
    print("Number is positive")

elif number < 0:
    print("Number is negative")

else:
    print("Number is zero")
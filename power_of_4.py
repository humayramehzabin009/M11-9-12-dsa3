# Program to check if a number is a power of 4
def powerOf4(number):
    count = 0

    # Check if there is only 1 set bit
    if (number & (number - 1)) == 0:
        # Count the bits before the set bit
        while number > 1:
            number >>= 1
            count += 1

        # If count is even, the number is a power of 4
        if count % 2 == 0:
            return True

    # If the conditions aren't met, return False
    return False

# Input from the user
number = int(input("Enter your number: "))

# Check if the number is a power of 4
if powerOf4(number):
    print(number, 'is a power of 4')
else:
    print(number, 'is not a power of 4')

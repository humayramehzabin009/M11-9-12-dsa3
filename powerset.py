import math

def printPowerSet(set, set_size):
    # Find total number of elements possible in the power set
    power_set_size = (int)(math.pow(2, set_size))
    
    # Loop over each element in the power set
    for outer in range(0, power_set_size):
        for inner in range(0, set_size):
            # Check if inner bit in the outer is set
            # If set, then print inner element from set
            if (outer & (1 << inner)) > 0:
                print(set[inner], end=" ")
        print("")

# Input the size of the array
size = int(input("Enter array size: "))

# Input the elements of the set
set = []
for i in range(0, size):
    n = int(input("Enter element: "))
    set.append(n)

# Call the function to print the power set
printPowerSet(set, len(set))

# Function to find the Least Common Multiple
def leastCommonMultiple(a, b):
    # TODO: Implement the LCM logic here
    greatest = max(a,b)
    least = min(a,b)
    for i in range(greatest, a*b+1, greatest):
        if i % least == 0:
            return i
    

# Example usage
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

lcm = leastCommonMultiple(a, b)
print(f"LCM of {a} and {b} is: {lcm}")
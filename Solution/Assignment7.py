def triangle_pattern_for(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")  # Print leading spaces
        for j in range(1, 2 * i):  # Print numbers for the triangle
            print(j, end=" ")
        print()  # New line after each row

# Example usage
n = 3
triangle_pattern_for(n)

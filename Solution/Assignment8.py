def alphabet_pattern_string_concat(n):
    for i in range(1, n+1):
        # Left-padding spaces for alignment
        result = " " * (n - i)
        
        # Build the increasing part of the pattern
        result += " ".join(chr(64 + j) for j in range(1, i + 1))
        
        # Build the decreasing part of the pattern
        result += " " + " ".join(chr(64 + j) for j in range(i - 1, 0, -1))
        
        print(result)  # Print the constructed row

# Example usage
n = 3
alphabet_pattern_string_concat(n)

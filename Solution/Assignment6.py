def pattern_one_line(n):
    for i in range(1, n + 1):
        print(" ".join("*" * i))

# Example usage
rows = 4
pattern_one_line(rows)

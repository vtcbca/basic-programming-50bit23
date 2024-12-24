def fibonacci_recursive_terms(n, a=0, b=1):
    if n == 0:
        return []
    else:
        return [a] + fibonacci_recursive_terms(n - 1, b, a + b)

def fibonacci_recursive_max_value(max_value, a=0, b=1):
    if a >= max_value:
        return []
    else:
        return [a] + fibonacci_recursive_max_value(max_value, b, a + b)

# Example usage
n_terms = 10
max_value = 100
print(f"Fibonacci sequence up to {n_terms} terms: {fibonacci_recursive_terms(n_terms)}")
print(f"Fibonacci sequence less than {max_value}: {fibonacci_recursive_max_value(max_value)}")

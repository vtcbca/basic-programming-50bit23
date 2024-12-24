def is_palindrome_reversed(s):
    return s == ''.join(reversed(s))

# Example usage
input_string = input("Enter a string: ")
print(f"Is '{input_string}' a palindrome? {is_palindrome_reversed(input_string)}")

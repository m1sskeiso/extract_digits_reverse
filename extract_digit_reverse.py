def extract_digits_reverse(number):
    # Convert the number to a string to easily access individual digits
    str_number = str(number)
    
    # Extract each digit in reverse order
    reversed_digits = [int(digit) for digit in str_number[::-1]]
    
    return reversed_digits

# Test case
given_number = 7536
result = extract_digits_reverse(given_number)

# Print the result with spaces between digits
print(" ".join(map(str, result)))

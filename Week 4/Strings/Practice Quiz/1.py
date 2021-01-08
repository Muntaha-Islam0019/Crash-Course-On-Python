def is_palindrome(input_string):
    return input_string.replace(" ", "").lower() == input_string[::-1].replace(" ", "").lower()

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
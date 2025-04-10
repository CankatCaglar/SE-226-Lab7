import string

def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def remove_punctuation(s):
    return ''.join(char for char in s if char not in string.punctuation)

if __name__ == "__main__":
    test_string = "hello, world! how are you?"
    print(f"Original: {test_string}")
    print(f"Reversed: {reverse_string(test_string)}")
    print(f"Capitalized: {capitalize_words(test_string)}")
    print(f"Without punctuation: {remove_punctuation(test_string)}") 

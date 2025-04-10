def count_characters(s):
    return len(s)

def count_words(s):
    return len(s.split())

def average_word_length(s):
    words = s.split()
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)

if __name__ == "__main__":
    test_string = "Hello, world! How are you?"
    print(f"Original: {test_string}")
    print(f"Character count: {count_characters(test_string)}")
    print(f"Word count: {count_words(test_string)}")
    print(f"Average word length: {average_word_length(test_string):.2f}") 

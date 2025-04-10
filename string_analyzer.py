from string_package import (
    reverse_string,
    capitalize_words,
    remove_punctuation,
    count_characters,
    count_words,
    average_word_length
)

def analyze_string():
    sentence = input("Enter a sentence: ")
    
    print("\nString Analysis Results:")
    print("-" * 25)
    print(f"Original: {sentence}")
    print(f"Reversed: {reverse_string(sentence)}")
    print(f"Capitalized: {capitalize_words(sentence)}")
    
    clean_sentence = remove_punctuation(sentence)
    print(f"\nWithout punctuation: {clean_sentence}")
    print(f"Character count: {count_characters(clean_sentence)}")
    print(f"Word count: {count_words(clean_sentence)}")
    print(f"Average word length: {average_word_length(clean_sentence):.2f}")

if __name__ == "__main__":
    print("String Analyzer")
    print("==============")
    analyze_string() 
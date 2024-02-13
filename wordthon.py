import random

upper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]
lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
def generate_word(length, case='lower'):
    if case == 'lower':
        return ''.join(random.choice(lower_case) for _ in range(length))
    elif case == 'upper':
        return ''.join(random.choice(upper_case) for _ in range(length))
    elif case == "number":
        return ''.join(random.choice(number) for _ in range(length))
    else:
        raise ValueError("Invalid case specified. Use 'lower' or 'upper'.")

def generate_words(num_words, word_length, case='lower'):
    return [generate_word(word_length, case) for _ in range(num_words)]

def main():
    num_words = int(input("Enter the number of words to generate: "))
    word_length = int(input("Enter the length of each word: "))
    case = input("Enter 'lower' for lower case words or 'upper' for upper case words or num for numbers ").lower()
    
    if case not in ['lower', 'upper','number']:
        print("Invalid case specified. Defaulting to lower case.")
        case = 'lower'
    
    words = generate_words(num_words, word_length, case)
    
    print("Generated words:")
    for word in words:
        print(word)

if __name__ == "__main__":
    main()

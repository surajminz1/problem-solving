# Strings:
# write code to reverse words in sentence

def reverse_words(sentence):
    words = [word for word in sentence.split('.') if word]
    return "".join(words)

def main():
    # Example usage:
    sentence = "..geeks..for.geeks."
    print(reverse_words(sentence))

if __name__ == "__main__":
    main()
def reverse_words(string):
    words = string.split(" ")
    reverse_words = list(reversed(words))

    return reverse_words
def main():
    string = "Here is a test string"
    print(reverse_words(string))

main()

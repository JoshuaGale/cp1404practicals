def main():
    counted_words = {}
    sentence = input("please enter a string: ")
    words = sentence.split()
    for word in words:
        if word in counted_words:
            counted_words[word] += 1
        else:
            counted_words[word] = 1

    sorting_words = list(counted_words.keys())
    sorting_words.sort()
    max_length = max(len(word) for word in sorting_words)
    for word in sorting_words:
        print("{:{}} : {}".format(word, max_length, counted_words[word]))

main()


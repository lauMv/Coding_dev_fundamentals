import optparse


def get_text():
    file_name = input('Enter file Name: ')
    file = open(file_name, 'r')
    counts = dict()
    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                counts[word] = counts.get(word, 0) + 1
    return counts


def get_num_word(counts):
    word = input("Word to search: ")
    print(word + " = " + str(counts[str(word)]))


if __name__ == '__main__':
    words = get_text()
    print (words)
    get_num_word(words)

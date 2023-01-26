def get_text():
    # file_name = input('Enter file Name: ')
    file = "full_walk.txt"
    counts = {}
    with open(file, 'r') as file:
        for line in file:
            aux = line.split(" = ")
            if aux[0].__contains__('.1.3.6.1.2.1.2.2.1.2'):
                counts[str(aux[0])] = []
    print(counts)
    return counts


def set_apps(counts):
    file = "full_walk.txt"
    with open(file, 'r') as file:
        for line in file:
            aux = line.split(" = ")
            if aux[0] in counts.keys():
                counts[aux[0]].append(aux[1].replace('\n', ""))
    return counts


def find_app(name, codes = {}):
    for elem in codes.items():
        if name in str(elem):
            return elem[0]


if __name__ == '__main__':
    codes = get_text()
    set_apps(codes)
    id = find_app("build0", codes)
    print(codes[id])

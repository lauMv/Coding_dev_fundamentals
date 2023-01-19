import random


def generate_password(long=10):
    psw = ""
    hex_list = []
    [hex_list.append(str(random.randrange(22, 77))) for _ in range(0, long)]
    for elem in hex_list:
        psw = psw + bytes.fromhex(elem).decode("ASCII")
    return psw


if __name__ == '__main__':
    name = input("App name: ")
    size = input("password size: ")
    try:
        print(int(size))
        if int(size) >= 8:
            print("The password for " + name + " is: ", generate_password(int(size)))
    except:
        print("The password for " + name + " is: ", generate_password())

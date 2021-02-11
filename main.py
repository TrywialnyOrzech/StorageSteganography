from src.steg import steg_icmp


def main():
    i = 0
    hex_str = 'a'
    file = open("text_to_send.txt", "r")

    while 1:
        char = file.read(1)
        if not char:
            break

        steg_icmp(char)
        i += 1
        print(i)


if __name__ == '__main__':
    main()

# main.py


def main():
    unicode_str = "\u1234\u5678\u90AB"
    decoded_str = unicode_str.encode("utf-8")
    print(decoded_str.decode("ascii"))


if __name__ == "__main__":
    main()

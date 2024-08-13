# main.py


def main():
    file_path = "file_does_not_exist.txt"
    with open(file_path, "r") as file:
        content = file.read()


if __name__ == "__main__":
    main()

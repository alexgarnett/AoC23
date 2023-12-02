def sum_line(line: str):
    last_digit = None
    first_digit = None
    for char in line:
        if char.isdigit():
            if first_digit is None:
                first_digit = char
                last_digit = char
            else:
                last_digit = char

    if last_digit is None and first_digit is None:
        return 0

    return int(first_digit + last_digit)


def main():
    f = open('shan_input.txt')
    result = 0
    for line in f:
        result += sum_line(line)

    print(result)


if __name__ == "__main__":
    main()

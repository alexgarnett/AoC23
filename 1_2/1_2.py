number_mapping = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

_end = '__end__'


def make_trie(*words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
    return root


def in_trie(trie, word):
    current_dict = trie
    for letter in word:
        if letter not in current_dict:
            return False
        current_dict = current_dict[letter]
    return _end in current_dict


def sum_line(line, num_trie):
    last_digit = None
    first_digit = None
    curr_index = 0
    for char in line:
        if char.isdigit():
            if first_digit is None:
                first_digit = char
                last_digit = char
            else:
                last_digit = char
        else:
            i = 0
            while i < 3:
                check_word = line[curr_index:curr_index+3+i]
                if in_trie(num_trie, check_word):
                    digit = number_mapping[check_word]
                    if first_digit is None:
                        first_digit = digit
                        last_digit = digit
                    else:
                        last_digit = digit
                    break
                i += 1
        curr_index += 1

    if last_digit is None and first_digit is None:
        return 0

    return int(first_digit + last_digit)


def main():
    trie = make_trie('one', 'two', 'three', 'four', 'five', 'six', 'seven',
                     'eight', 'nine')
    print(trie)
    f = open('shan_input.txt')
    result = 0
    for line in f:
        result += sum_line(line, trie)

    print("Result:" + str(result))


if __name__ == "__main__":
    main()

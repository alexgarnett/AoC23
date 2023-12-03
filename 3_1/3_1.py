
def contains_nums(line):
    curr_num = ''
    line_nums = {}
    index = 0
    for char in line:
        if char.isdigit():
            curr_num = curr_num + char
        else:
            if curr_num == '':
                index += 1
                continue
            # save the number to dict
            line_nums[(index - len(curr_num))] = curr_num
            curr_num = ''
        # add num to dictionary if on last character
        if index == len(line) - 1:
            line_nums[(index - len(curr_num)) + 1] = curr_num
        index += 1
    return line_nums


def adjacent_symbol(upper_line, line, lower_line, dict):
    valid_parts = []
    for index in dict.keys():
        num = dict[index]
        length = len(num)
        start = index - 1
        end = index + length + 1
        if start < 0:
            start = index
        if end > len(line) - 1:
            end = len(line) - 1
        for i in range(start, end):
            if not upper_line[i].isdigit() and upper_line[i] != '.':
                valid_parts.append(int(num))
                break
            if not lower_line[i].isdigit() and lower_line[i] != '.':
                valid_parts.append(int(num))
                break
            if not line[i].isdigit() and line[i] != '.':
                valid_parts.append(int(num))
                break
    return sum(valid_parts)


def main():
    part_sum = 0
    f = open('shan_input.txt')
    all_lines = f.readlines()
    prev_line = '.' * (len(all_lines[0]) - 1)
    i = 0
    for line in all_lines:
        line = line[:-1]
        nums_in_line = contains_nums(line)
        if nums_in_line:
            if i + 1 < len(all_lines):
                next_line = all_lines[i + 1]
            else:
                next_line = '.' * len(line)
            valid_part_nums = adjacent_symbol(prev_line, line, next_line, nums_in_line)
            part_sum = part_sum + valid_part_nums
        prev_line = line
        i += 1

    print(part_sum)


if __name__ == '__main__':
    main()

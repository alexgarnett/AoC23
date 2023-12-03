import numpy as np


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


def adjacent_symbol(upper_line, line, lower_line, line_number, dict, stars):
    for index_first_digit in dict.keys():
        num = dict[index_first_digit]
        length = len(num)
        start = index_first_digit - 1
        end = index_first_digit + length + 1
        if start < 0:
            start = index_first_digit
        if end > len(line) - 1:
            end = len(line) - 1
        for i in range(start, end):
            if upper_line[i] == '*':
                numbers = stars[line_number - 1][i]
                for j in range(len(numbers)):
                    if numbers[j] < 0:
                        stars[line_number - 1][i][j] = int(num)
                        break

            if lower_line[i] == '*':
                numbers = stars[line_number + 1][i]
                for j in range(len(numbers)):
                    if numbers[j] < 0:
                        stars[line_number + 1][i][j] = int(num)
                        break

            if line[i] == '*':
                numbers = stars[line_number][i]
                for j in range(len(numbers)):
                    if numbers[j] < 0:
                        stars[line_number][i][j] = int(num)
                        break

    return stars


def main():
    part_sum = 0
    f = open('input.txt')
    all_lines = f.readlines()
    prev_line = '.' * (len(all_lines[0]) - 1)
    i = 0
    stars = np.full((len(all_lines), len(all_lines[0]) - 1, 8), -1)
    for line in all_lines:
        line = line[:-1]
        nums_in_line = contains_nums(line)
        if nums_in_line:
            if i + 1 < len(all_lines):
                next_line = all_lines[i + 1]
            else:
                next_line = '.' * len(line)
            stars = adjacent_symbol(prev_line, line, next_line,
                                              i, nums_in_line, stars)
        prev_line = line
        i += 1
    # calculate result from stars array
    result = 0
    for i in range(len(stars)):
        for j in range(len(stars[i])):
            star = stars[i][j]
            gear_nums = []
            for num in star:
                if num >= 0:
                    gear_nums.append(num)
            if len(gear_nums) == 2:
                result += (gear_nums[0]*gear_nums[1])

    print(result)


if __name__ == '__main__':
    main()

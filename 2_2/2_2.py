# 12 red cubes, 13 green cubes, and 14 blue cubes

def game_number(line):
    parts = line.split(':')
    game_sets = parts[1].split(';')
    max_red = 0
    max_blue = 0
    max_green = 0
    for handfuls in game_sets:
        colors = handfuls.split(',')
        for color in colors:
            vals = color.split(' ')
            num = int(vals[1])
            c = vals[2]
            if c == 'red' and num > max_red:
                max_red = num
            if c == 'green' and num > max_green:
                max_green = num
            if c == 'blue' and num > max_blue:
                max_blue = num
            if c == 'red\n' and num > max_red:
                max_red = num
            if c == 'green\n' and num > max_green:
                max_green = num
            if c == 'blue\n' and num > max_blue:
                max_blue = num

    return max_blue * max_green * max_red


def main():
    f = open('input.txt')
    result = 0
    for line in f:
        result += game_number(line)

    print(result)


if __name__ == "__main__":
    main()

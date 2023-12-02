# 12 red cubes, 13 green cubes, and 14 blue cubes

def is_game_possible(line):
    line.strip("\n")
    parts = line.split(':')
    game_number = int(parts[0].split(' ')[1])
    # determine if the game is possible
    game_sets = parts[1].split(';')
    print(game_sets)
    for handfuls in game_sets:
        colors = handfuls.split(',')
        for color in colors:
            vals = color.split(' ')
            num = int(vals[1])
            c = vals[2]
            if c == 'red' and num > 12:
                return 0
            if c == 'green' and num > 13:
                return 0
            if c == 'blue' and num > 14:
                return 0
            if c == 'red\n' and num > 12:
                return 0
            if c == 'green\n' and num > 13:
                return 0
            if c == 'blue\n' and num > 14:
                return 0

    return game_number

def main():
    f = open('input.txt')
    result = 0
    for line in f:
        result += is_game_possible(line)

    print(result)


if __name__ == "__main__":
    main()

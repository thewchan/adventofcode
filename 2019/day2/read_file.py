"""Read file line by line."""


def read_input(file='./input.txt'):
    """Read input from file."""
    with open(f'{file}', 'r') as f:
        lines = f.readlines()

    return lines


if __name__ == '__main__':
    read_input()

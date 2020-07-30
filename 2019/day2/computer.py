"""Optcode computer.

On the way to your gravity assist around the Moon, your ship computer
beeps angrily about a "1202 program alarm". On the radio, an Elf is
already explaining how to handle the situation: "Don't worry, that's
perfectly norma--" The ship computer bursts into flames.

You notify the Elves that the computer's magic smoke seems to have
escaped. "That computer ran Intcode programs like the gravity assist
program it was working on; surely there are enough spare parts up there
to build a new Intcode computer!"

An Intcode program is a list of integers separated by commas (like
1,0,0,3,99). To run one, start by looking at the first integer (called
position 0). Here, you will find an opcode - either 1, 2, or 99. The
opcode indicates what to do; for example, 99 means that the program is
finished and should immediately halt. Encountering an unknown opcode
means something went wrong.

Opcode 1 adds together numbers read from two positions and stores the
result in a third position. The three integers immediately after the
opcode tell you these three positions - the first two indicate the
positions from which you should read the input values, and the third
indicates the position at which the output should be stored.

For example, if your Intcode computer encounters 1,10,20,30, it should
read the values at positions 10 and 20, add those values, and then
overwrite the value at position 30 with their sum.

Opcode 2 works exactly like opcode 1, except it multiplies the two
inputs instead of adding them. Again, the three integers after the
opcode indicate where the inputs and outputs are, not their values.

Once you're done processing an opcode, move to the next one by stepping
forward 4 positions.
"""
from read_file import read_input


def computer(input_optcodes):
    """Read optcodes and computer, return output."""
    optcodes = input_optcodes.copy()
    skip4_flag = False
    skip4_count = 0

    for i in range(len(optcodes)):
        # print(i, optcodes[i])
        # print(optcodes)
        if skip4_flag:
            if skip4_count < 3:
                # print('skipforward')
                skip4_count += 1
                continue
        if optcodes[i] == 99:
            break
        skip4_flag = False
        skip4_count = 0
        if optcodes[i] == 1:
            # print(f'Replacing position[{optcodes[i+3]}],'
            #       f' value({optcodes[optcodes[i+3]]}) by '
            #       f'position[{optcodes[i+1]}], value('
            #       f'{optcodes[optcodes[i+1]]}) + position[{optcodes[i+2]}]'
            #       f', value({optcodes[optcodes[i+2]]}) = '
            #       f'{optcodes[optcodes[i+1]] + optcodes[optcodes[i+2]]}')
            optcodes[optcodes[i + 3]] = (optcodes[optcodes[i + 1]] +
                                         optcodes[optcodes[i + 2]])
            skip4_flag = True

        elif optcodes[i] == 2:
            # print(f'Replacing position[{optcodes[i+3]}],'
            #       f'value({optcodes[optcodes[i+3]]}) by '
            #       f'position[{optcodes[i+1]}], value('
            #       f'{optcodes[optcodes[i+1]]}) * position[{optcodes[i+2]}]'
            #       f', value({optcodes[optcodes[i+2]]}) = '
            #       f'{optcodes[optcodes[i+1]] * optcodes[optcodes[i+2]]}')
            optcodes[optcodes[i + 3]] = (optcodes[optcodes[i + 1]] *
                                         optcodes[optcodes[i + 2]])
            skip4_flag = True

    return optcodes


def get_optcodes(*args, **kwargs):
    """Read input and preprocess optcodes."""
    optcodes = read_input(*args, **kwargs)
    optcodes = [i for i in map(int, optcodes[0].strip().split(','))]
    return optcodes


def main():
    """Make optcode modification, process optcodes, print optcodes."""
    optcodes = get_optcodes()
    optcodes[1], optcodes[2] = 12, 2
    print(computer(optcodes))


if __name__ == '__main__':
    main()

#!/usr/bin/env python

"""
Santa has become stranded at the edge of the Solar System while delivering
presents to other planets! To accurately calculate his position in space,
safely align his warp drive, and return to Earth in time to save Christmas, he
needs you to bring him measurements from fifty stars.

Collect stars by solving puzzles. Two puzzles will be made available on each
day in the Advent calendar; the second puzzle is unlocked when you complete
the first. Each puzzle grants one star. Good luck!

The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper.
They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass. Specifically, to
find the fuel required for a module, take its mass, divide by three, round
down, and subtract 2.

The Fuel Counter-Upper needs to know the total fuel requirement. To find it,
individually calculate the fuel needed for the mass of each module (your
puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your
spacecraft?
"""

import os


def input_gen():
    dir_name = os.path.dirname(os.path.realpath(__file__))
    input_fn = os.path.join(dir_name, "input.txt")

    with open(input_fn) as f:
        for line in f.readlines():
            yield line.strip()


def get_fuel(mass):
    """Calculate the fuel needed for a module launch given its mass.

    >>> get_fuel(12)
    2
    >>> get_fuel(14)
    2
    >>> get_fuel(1969)
    654
    >>> get_fuel(100756)
    33583
    """

    return mass // 3 - 2


def main():
    total_fuel = sum(get_fuel(int(m)) for m in input_gen())
    print(total_fuel)


if __name__ == "__main__":
    main()

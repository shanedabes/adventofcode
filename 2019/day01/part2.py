#!/usr/bin/env python

"""
During the second Go / No Go poll, the Elf in charge of the Rocket Equation
Double-Checker stops the launch sequence. Apparently, you forgot to include
additional fuel for the fuel you just added.

Fuel itself requires fuel just like a module - take its mass, divide by three,
round down, and subtract 2. However, that fuel also requires fuel, and that
fuel requires fuel, and so on. Any mass that would require negative fuel should
instead be treated as if it requires zero fuel; the remaining mass, if any, is
instead handled by wishing really hard, which has no mass and is outside the
scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then,
treat the fuel amount you just calculated as the input mass and repeat the
process, continuing until a fuel requirement is zero or negative. For example:
"""

import part1


def get_fuel_fuel(mass):
    """Calculate the fuel needed for module launch, including fuel fuel

    >>> get_fuel_fuel(14)
    2
    >>> get_fuel_fuel(1969)
    966
    >>> get_fuel_fuel(100756)
    50346
    """

    mass_fuel = part1.get_fuel(mass)
    if mass_fuel > 0:
        return mass_fuel + get_fuel_fuel(mass_fuel)
    else:
        return 0


def main():
    total_fuel = sum(get_fuel_fuel(int(m)) for m in part1.input_gen())
    print(total_fuel)


if __name__ == "__main__":
    main()

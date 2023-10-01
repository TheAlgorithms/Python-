# Created by Pronay Debnath
# Date:- 1/10/2023
# Energy-Mass Equivalence in Python

import doctest

def mass_to_energy(mass_kg):
    """
    Calculate the energy equivalent of a given mass using E=mc^2.

    :param mass_kg: Mass in kilograms.
    :return: Energy in joules.
    >>> format(mass_to_energy(1), '.15e')  # 1 kg
    '8.987551787368176e+16'
    >>> format(mass_to_energy(0.5), '.15e')  # 0.5 kg
    '4.493775893684088e+16'
    """
    speed_of_light = 299792458  # Speed of light in meters per second (m/s)
    energy_joules = mass_kg * speed_of_light**2
    return energy_joules

def is_valid_mass(mass_str):
    """
    Check if the input string represents a valid positive float for mass.

    :param mass_str: Input string.
    :return: True if valid, False otherwise.
    >>> is_valid_mass("1.5")
    True
    >>> is_valid_mass("0")
    False
    >>> is_valid_mass("abc")
    False
    """
    if mass_str == "0":
        return False
    try:
        mass = float(mass_str)
        return mass >= 0
    except ValueError:
        return False

def get_valid_mass_input():
    """
    Prompt the user for a valid positive mass input.

    :return: Valid mass as a float.
    """
    while True:
        mass_str = input("Enter the mass in kilograms (a positive number): ")
        if is_valid_mass(mass_str):
            return float(mass_str)
        else:
            print("Invalid input. Please enter a positive number for mass.")

if __name__ == "__main__":
    doctest.testmod()  # Run doctests in the docstrings
    mass = get_valid_mass_input()
    energy = mass_to_energy(mass)
    print(f"The energy equivalent of {mass} kilograms is {format(energy, '.15e')} joules.")

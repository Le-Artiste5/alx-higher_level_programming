#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_xx = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    roman_c = 0
    for a in range(len(roman_string)):
        if a > 0 and roman_xx[roman_string[a]] > roman_xx[roman_string[a - 1]]:
            roman_c += roman_xx[roman_string[a]] - 2 * \
                    roman_xx[roman_string[a - 1]]
        else:
            roman_c += roman_xx[roman_string[a]]
    return roman_xx

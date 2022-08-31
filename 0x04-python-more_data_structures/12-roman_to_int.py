#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    if(roman_string and isinstance(roman_string, str)):
        rom_deci = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
        for i in range(len(roman_string)):
            if i > 0 and rom_deci[roman_string[i]] > rom_deci[roman_string[i - 1]]:
                sum += rom_deci[roman_string[i]] - 2 * rom_deci[roman_string[i - 1]]
            else:
                sum += rom_deci[roman_string[i]]
        return sum

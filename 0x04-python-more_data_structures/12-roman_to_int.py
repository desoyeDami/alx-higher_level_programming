#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    roman_num_sum = 0
    prev_value = 0
    for char in roman_string:
        if char in roman_numerals:
            current_value = roman_numerals[char]
            if current_value > prev_value:
                roman_num_sum += current_value - 2 * prev_value
            else:
                roman_num_sum += current_value
            prev_value = current_value
        else:
            return 0
    return roman_num_sum

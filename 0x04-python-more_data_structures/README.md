# 0x04. Python - More Data Structures: Set, Dictionary

## General Information

In this project, you will work on Python programming tasks that involve sets, dictionaries, and various data manipulation operations. You'll write functions to perform operations on lists, sets, and dictionaries, as well as explore how to work with Python data structures effectively.

## Learning Objectives

Upon completing this project, you should be able to:

- Explain the advantages of Python programming.
- Understand what sets are and how to use them.
- Know the most common methods of sets and how to use them.
- Determine when to use sets versus lists.
- Iterate through a set in Python.
- Understand what dictionaries are and how to use them.
- Determine when to use dictionaries versus lists or sets.
- Define what a key is in a dictionary.
- Iterate over a dictionary in Python.
- Describe what a lambda function is.
- Explain the map, reduce, and filter functions in Python.

## Tasks

### 0. Squared Simple

Write a function that computes the square value of all integers in a matrix.

- Prototype: `def square_matrix_simple(matrix=[]):`
- `matrix` is a 2-dimensional array.
- Returns a new matrix:
  - Same size as the input matrix.
  - Each value should be the square of the value of the input.
- The initial matrix should not be modified.
- You are not allowed to import any module.

### 1. Search and Replace

Write a function that replaces all occurrences of an element by another in a new list.

- Prototype: `def search_replace(my_list, search, replace):`
- `my_list` is the initial list.
- `search` is the element to replace in the list.
- `replace` is the new element.
- You are not allowed to import any module.

### 2. Unique Addition

Write a function that adds all unique integers in a list (only once for each integer).

- Prototype: `def uniq_add(my_list=[]):`
- You are not allowed to import any module.

### 3. Present in Both

Write a function that returns a set of common elements in two sets.

- Prototype: `def common_elements(set_1, set_2):`
- You are not allowed to import any module.

### 4. Only Differents

Write a function that returns a set of all elements present in only one set.

- Prototype: `def only_diff_elements(set_1, set_2):`
- You are not allowed to import any module.

### 5. Number of Keys

Write a function that returns the number of keys in a dictionary.

- Prototype: `def number_keys(a_dictionary):`
- You are not allowed to import any module.

### 6. Print Sorted Dictionary

Write a function that prints a dictionary by ordered keys.

- Prototype: `def print_sorted_dictionary(a_dictionary):`
- You can assume that all keys are strings.
- Keys should be sorted by alphabetical order.
- Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary).
- Dictionary values can have any type.
- You are not allowed to import any module.

### 7. Update Dictionary

Write a function that replaces or adds key/value pairs in a dictionary.

- Prototype: `def update_dictionary(a_dictionary, key, value):`
- `key` argument will always be a string.
- `value` argument can be of any type.
- If a key exists in the dictionary, the value will be replaced.
- If a key doesn’t exist in the dictionary, it will be created.
- You are not allowed to import any module.

### 8. Simple Delete by Key

Write a function that deletes a key in a dictionary.

- Prototype: `def simple_delete(a_dictionary, key=""):`
- `key` argument will always be a string.
- If a key doesn’t exist, the dictionary won’t change.
- You are not allowed to import any module.

### 9. Multiply by 2

Write a function that returns a new dictionary with all values multiplied by 2.

- Prototype: `def multiply_by_2(a_dictionary):`
- You can assume that all values are only integers.
- Returns a new dictionary.
- You are not allowed to import any module.

### 10. Best Score

Write a function that returns a key with the biggest integer value.

- Prototype: `def best_score(a_dictionary):`
- You can assume that all values are only integers.
- If no score is found, return `None`.
- You can assume all students have a different score.
- You are not allowed to import any module.

### 11. Multiply by Using Map

Write a function that returns a list with all values multiplied by a number without using any loops.

- Prototype: `def multiply_list_map(my_list=[], number=0):`
- Returns a new list.
- Same length as the input list.
- Each value should be multiplied by the given number.
- The initial list should not be modified.
- You have to use `map`.
- You are not allowed to use `for` or `while` loops.

### 12. Roman to Integer

Create a function `def roman_to_int(roman_string):` that converts a Roman numeral to an integer.

- You can assume the number will be between 1 to 3999.
- `roman_to_int(roman_string)` must return an integer.
- If the `roman_string` is not a string or `None`, return `0`.

### 13. Weighted Average!

Write a function that returns the weighted average of all integers in a tuple of the form `<score>, <weight>`.

- Prototype: `def weight_average(my_list=[]):`
- Returns `0` if the list is

 empty.
- You are not allowed to use `sum()`.

### 14. Squared to List

Write a function that converts a list of integers into a list of their squares.

- Prototype: `def square_matrix_map(matrix=[]):`
- `matrix` is a 2-dimensional array.
- Returns a new list:
  - Same size as the input matrix.
  - Each value should be the square of the value of the input.
- The initial matrix should not be modified.
- You are not allowed to use `for` or `while` loops.
- You have to use `map`.

### 15. Delete by Value

Write a function that deletes all integers with a value in a list.

- Prototype: `def delete_by_value(my_list, x):`
- `my_list` is the list.
- `x` is the integer to remove from the list.
- You are not allowed to use `remove()`.

### 16. CPython #1: PyBytesObject

Create two C functions that print some basic info about Python lists and Python bytes objects.

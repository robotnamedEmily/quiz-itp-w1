"""Intro to Python - Week 1 - Quiz."""


# Question 3
def remove_Es(a_string):
    """Implement the code required to make this function work.

    Write a function `remove_Es` that receives a string and removes all
    the characters `'e'` or `'E'`. Example:

    remove_Es('remoter')  # 'rmotr'
    remove_Es('eEe')      # ''
    remove_Es('abc')      # 'abc'
    """
    # Write your code here
    for char in a_string:
        new_string = ''
        if char == 'e' or char == 'E':
            newstring = a_string.replace('E', "") or a_string.replace('e', "")
        return new_string
            
            

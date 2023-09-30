#number_range_analysis.py

'''
Implement Number Analysis Functions

- Function to calculate the sum of numbers within the range.
- Function to find the smallest number within the range.
- Function to find the largest number within the range.
- Function to count the number of even numbers within the range.
- Function to count the number of odd numbers within the range.

'''
# TODO: IN A COMMENT WITHIN EACH DEF, WRITE PSEUDOCODE FOR EACH SOLUTION

def calculate_sum(start, end):
    """
    Calculate the sum of numbers within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The sum of numbers within the range.
    """
    # TODO: Implement the logic to calculate the sum of numbers within the range.
    sum = 0
    for num in range(start, end + 1):
        sum += num

    return sum
        
        


    # TODO: Return the calculated sum.

def find_smallest_number(start, end):

    smallest_number = 100000000
    for num in range(start, end + 1):
        if num < smallest_number:
            smallest_number = num

    return smallest_number

    """
    Find the smallest number within the specified 
    range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The smallest number within the range.
    """
    # TODO: Implement the logic to find the smallest number within the range.
    # TODO: Return the found smallest number.

def find_largest_number(start, end):

    largest_number = -10000000
    for num in range(start, end + 1):
        if num > largest_number:
            largest_number = num

    return largest_number

    """
    Find the largest number within the specified range.

    Args:
        start (int): The starting number of the range ( inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The largest number within the range.
    """
    # TODO: Implement the logic to find the largest number within the range.
    # TODO: Return the found largest number.

def count_even_numbers(start, end):

    count = 0

    for num in range(start, end + 1):
        # if number is even count + 1
        
        if num % 2 == 0:
            count += 1 

        
    return count

    """
    Count the number of even numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of even numbers within the range.
    """
    # TODO: Implement the logic to count even numbers within the range.
    # TODO: Return the count of even numbers.

def count_odd_numbers(start, end):
    count = 0

    for num in range(start, end + 1):
        # if number is odd count + 1
        
        if num % 2 != 0:
            count += 1 

        
    return count
    """
    Count the number of odd numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of odd numbers within the range.
    """
    # TODO: Implement the logic to count odd numbers within the range.
    # TODO: Return the count of odd numbers.
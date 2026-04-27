# Mathematical Operations Module - Complete Math Functionality
# This module provides comprehensive mathematical operations from basic to advanced

import math
from typing import List, Tuple

# ===== BASIC MATHEMATICAL OPERATIONS =====

def add(a, b):
    """
    Add two numbers together
    Parameters:
        a (int/float): First number
        b (int/float): Second number
    Returns:
        int/float: Sum of a and b
    """
    return a + b

def subtract(a, b):
    """
    Subtract second number from first number
    Parameters:
        a (int/float): First number
        b (int/float): Second number to subtract
    Returns:
        int/float: Difference of a and b
    """
    return a - b

def multiply(a, b):
    """
    Multiply two numbers together
    Parameters:
        a (int/float): First number
        b (int/float): Second number
    Returns:
        int/float: Product of a and b
    """
    return a * b

def divide(a, b):
    """
    Divide first number by second number
    Parameters:
        a (int/float): Numerator
        b (int/float): Denominator
    Returns:
        int/float: Quotient of a divided by b
    Raises:
        ValueError: If denominator is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    """
    Calculate a raised to the power of b
    Parameters:
        a (int/float): Base number
        b (int/float): Exponent
    Returns:
        int/float: a to the power of b
    """
    return a ** b

def factorial(n):
    """
    Calculate factorial of a non-negative integer
    Parameters:
        n (int): Non-negative integer
    Returns:
        int: Factorial of n
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    """
    Generate Fibonacci sequence up to n terms
    Parameters:
        n (int): Number of terms to generate
    Returns:
        list: Fibonacci sequence with n terms
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# ===== ADVANCED MATHEMATICAL FUNCTIONS =====

def is_prime(n: int) -> bool:
    """
    Check if a number is prime
    Parameters:
        n (int): Number to check
    Returns:
        bool: True if prime, False otherwise
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def gcd(a: int, b: int) -> int:
    """
    Calculate greatest common divisor using Euclidean algorithm
    Parameters:
        a (int): First number
        b (int): Second number
    Returns:
        int: Greatest common divisor
    """
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """
    Calculate least common multiple
    Parameters:
        a (int): First number
        b (int): Second number
    Returns:
        int: Least common multiple
    """
    return abs(a * b) // gcd(a, b)

def is_perfect_square(n: int) -> bool:
    """
    Check if a number is a perfect square
    Parameters:
        n (int): Number to check
    Returns:
        bool: True if perfect square, False otherwise
    """
    if n < 0:
        return False
    root = int(math.sqrt(n))
    return root * root == n

def sum_of_digits(n: int) -> int:
    """
    Calculate sum of digits of a number
    Parameters:
        n (int): Number to process
    Returns:
        int: Sum of digits
    """
    return sum(int(digit) for digit in str(abs(n)))

def reverse_number(n: int) -> int:
    """
    Reverse the digits of a number
    Parameters:
        n (int): Number to reverse
    Returns:
        int: Reversed number
    """
    sign = -1 if n < 0 else 1
    reversed_str = str(abs(n))[::-1]
    return sign * int(reversed_str)

def is_armstrong_number(n: int) -> bool:
    """
    Check if a number is an Armstrong number
    Parameters:
        n (int): Number to check
    Returns:
        bool: True if Armstrong number, False otherwise
    """
    if n < 0:
        return False
    
    digits = [int(d) for d in str(n)]
    power = len(digits)
    armstrong_sum = sum(d ** power for d in digits)
    
    return armstrong_sum == n

def find_factors(n: int) -> List[int]:
    """
    Find all factors of a number
    Parameters:
        n (int): Number to find factors of
    Returns:
        List[int]: List of factors
    """
    if n <= 0:
        return []
    
    factors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    
    return sorted(list(factors))

# ===== ALGORITHMIC FUNCTIONS =====

def binary_search(arr: list, target: int) -> int:
    """
    Perform binary search on a sorted list
    Parameters:
        arr (list): Sorted list of elements
        target (int): Value to search for
    Returns:
        int: Index of target if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def bubble_sort(arr: list) -> list:
    """
    Sort a list using bubble sort algorithm
    Parameters:
        arr (list): List of elements to sort
    Returns:
        list: Sorted list
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def linear_search(arr: list, target: int) -> int:
    """
    Perform linear search on a list
    Parameters:
        arr (list): List of elements
        target (int): Value to search for
    Returns:
        int: Index of target if found, -1 otherwise
    """
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

def find_max(arr: list) -> int:
    """
    Find maximum value in a list
    Parameters:
        arr (list): List of numbers
    Returns:
        int: Maximum value
    """
    if not arr:
        raise ValueError("List is empty")
    
    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    return max_val

def find_min(arr: list) -> int:
    """
    Find minimum value in a list
    Parameters:
        arr (list): List of numbers
    Returns:
        int: Minimum value
    """
    if not arr:
        raise ValueError("List is empty")
    
    min_val = arr[0]
    for num in arr[1:]:
        if num < min_val:
            min_val = num
    return min_val

# ===== DEMONSTRATION FUNCTIONS =====

def demo_basic_operations():
    """Demonstrate basic mathematical operations"""
    print("=== Basic Math Operations Demo ===")
    print("Add 5 + 3:", add(5, 3))
    print("Subtract 10 - 4:", subtract(10, 4))
    print("Multiply 6 * 7:", multiply(6, 7))
    print("Divide 15 / 3:", divide(15, 3))
    print("Power 2^5:", power(2, 5))
    print("Factorial 5:", factorial(5))
    print("Fibonacci 10 terms:", fibonacci(10))

def demo_advanced_math():
    """Demonstrate advanced mathematical functions"""
    print("\n=== Advanced Math Functions Demo ===")
    test_numbers = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 25, 29, 31, 36, 49, 64, 81, 100]
    
    print("Prime numbers:", [n for n in test_numbers if is_prime(n)])
    print("Perfect squares:", [n for n in test_numbers if is_perfect_square(n)])
    print("Armstrong numbers:", [n for n in range(1, 1000) if is_armstrong_number(n)])
    print("GCD of 48 and 18:", gcd(48, 18))
    print("LCM of 12 and 15:", lcm(12, 15))
    print("Sum of digits of 12345:", sum_of_digits(12345))
    print("Reverse of 12345:", reverse_number(12345))
    print("Factors of 36:", find_factors(36))

def demo_algorithms():
    """Demonstrate algorithmic functions"""
    print("\n=== Algorithm Functions Demo ===")
    test_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = bubble_sort(test_list.copy())
    
    print("Original list:", test_list)
    print("Sorted list:", sorted_list)
    print("Binary search for 22:", binary_search(sorted_list, 22))
    print("Linear search for 25:", linear_search(test_list, 25))
    print("Maximum value:", find_max(test_list))
    print("Minimum value:", find_min(test_list))

if __name__ == "__main__":
    demo_basic_operations()
    demo_advanced_math()
    demo_algorithms()

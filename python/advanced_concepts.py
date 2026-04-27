# Advanced Concepts Module - Complete Advanced Python Functionality
# This module provides comprehensive advanced Python concepts including algorithms, iterators, generators, and decorators

import time
import sys
from typing import List, Dict, Any, Iterator, Callable

# ===== ALGORITHMS =====

class CustomIterator:
    """
    Custom iterator class that demonstrates iterator protocol
    """
    
    def __init__(self, *args):
        """
        Initialize iterator with elements
        Parameters:
            *args: Variable number of elements to iterate over
        """
        self.eleman = args
        self.index = -1
    
    def __iter__(self):
        """
        Return iterator object (self)
        Returns:
            CustomIterator: Iterator object
        """
        return self
    
    def __next__(self):
        """
        Return next element in iteration
        Returns:
            Next element
        Raises:
            StopIteration: When iteration is complete
        """
        if self.index + 1 < len(self.eleman):
            self.index += 1
            return self.eleman[self.index]
        else:
            self.index = -1  # Reset for next iteration
            raise StopIteration("Iterator has reached the last element")

# ===== GENERATORS =====

def number_generator():
    """
    Generator function that yields numbers
    Yields:
        int: Sequential numbers
    """
    for i in range(100):
        yield i

def generator_with_list():
    """
    Generator that appends to a list (demonstrates side effects)
    """
    a = []
    for i in range(100):
        a.append(i)
        yield i

def fibonacci_generator(n: int) -> Iterator[int]:
    """
    Generator that yields Fibonacci numbers
    Parameters:
        n (int): Number of Fibonacci numbers to generate
    Yields:
        int: Fibonacci numbers
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def prime_generator(limit: int) -> Iterator[int]:
    """
    Generator that yields prime numbers up to limit
    Parameters:
        limit (int): Upper limit for prime numbers
    Yields:
        int: Prime numbers
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num

# ===== DECORATORS =====

def timer_decorator(func: Callable) -> Callable:
    """
    Decorator to measure function execution time
    Parameters:
        func: Function to measure
    Returns:
        Callable: Wrapped function with timing
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} fonksiyonu {end_time - start_time:.4f} saniye sürdü")
        return result
    
    return wrapper

def cache_decorator(func: Callable) -> Callable:
    """
    Decorator to cache function results
    Parameters:
        func: Function to cache
    Returns:
        Callable: Wrapped function with caching
    """
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            print(f"Cache hit for {func.__name__}{args}")
            return cache[args]
        
        result = func(*args)
        cache[args] = result
        print(f"Cache miss for {func.__name__}{args} - cached result")
        return result
    
    return wrapper

def retry_decorator(max_retries: int = 3, delay: float = 1.0):
    """
    Decorator to retry function execution
    Parameters:
        max_retries (int): Maximum number of retries
        delay (float): Delay between retries
    Returns:
        Callable: Wrapped function with retry logic
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

def validate_types(**type_hints):
    """
    Decorator to validate function parameter types
    Parameters:
        **type_hints: Type hints for parameters
    Returns:
        Callable: Wrapped function with type validation
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            # Get function parameter names
            import inspect
            sig = inspect.signature(func)
            param_names = list(sig.parameters.keys())
            
            # Validate positional arguments
            for i, (arg, expected_type) in enumerate(zip(args, type_hints.values())):
                if i < len(param_names) and not isinstance(arg, expected_type):
                    raise TypeError(f"Parameter '{param_names[i]}' must be {expected_type.__name__}, got {type(arg).__name__}")
            
            # Validate keyword arguments
            for param_name, expected_type in type_hints.items():
                if param_name in kwargs and not isinstance(kwargs[param_name], expected_type):
                    raise TypeError(f"Parameter '{param_name}' must be {expected_type.__name__}, got {type(kwargs[param_name]).__name__}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

# ===== CLOSURES AND HIGHER-ORDER FUNCTIONS =====

def create_multiplier(factor: int) -> Callable[[int], int]:
    """
    Create a multiplier function using closure
    Parameters:
        factor (int): Multiplication factor
    Returns:
        Callable: Function that multiplies by factor
    """
    def multiplier(number: int) -> int:
        return number * factor
    return multiplier

def create_accumulator() -> Callable[[int], int]:
    """
    Create an accumulator function using closure
    Returns:
        Callable: Function that accumulates values
    """
    total = 0
    
    def accumulator(value: int) -> int:
        nonlocal total
        total += value
        return total
    
    return accumulator

def compose_functions(*funcs: Callable) -> Callable:
    """
    Compose multiple functions
    Parameters:
        *funcs: Functions to compose
    Returns:
        Callable: Composed function
    """
    def composed(x):
        result = x
        for func in reversed(funcs):
            result = func(result)
        return result
    return composed

# ===== ADVANCED ALGORITHMS =====

def quick_sort(arr: List[int]) -> List[int]:
    """
    Quick sort algorithm
    Parameters:
        arr (List[int]): List to sort
    Returns:
        List[int]: Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge sort algorithm
    Parameters:
        arr (List[int]): List to sort
    Returns:
        List[int]: Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merge two sorted lists
    Parameters:
        left (List[int]): First sorted list
        right (List[int]): Second sorted list
    Returns:
        List[int]: Merged sorted list
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ===== FUNCTIONAL PROGRAMMING =====

def map_filter_reduce(data: List[int], 
                     map_func: Callable[[int], int],
                     filter_func: Callable[[int], bool],
                     reduce_func: Callable[[int, int], int]) -> int:
    """
    Implement map-filter-reduce pattern
    Parameters:
        data (List[int]): Input data
        map_func (Callable): Mapping function
        filter_func (Callable): Filtering function
        reduce_func (Callable): Reducing function
    Returns:
        int: Reduced result
    """
    # Map
    mapped = [map_func(x) for x in data]
    
    # Filter
    filtered = [x for x in mapped if filter_func(x)]
    
    # Reduce
    if not filtered:
        return 0
    
    result = filtered[0]
    for x in filtered[1:]:
        result = reduce_func(result, x)
    
    return result

def curry_function(func: Callable) -> Callable:
    """
    Curry a function
    Parameters:
        func (Callable): Function to curry
    Returns:
        Callable: Curried function
    """
    import functools
    
    @functools.wraps(func)
    def curried(*args, **kwargs):
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            return func(*args, **kwargs)
        return lambda *more_args, **more_kwargs: curried(*(args + more_args), **{**kwargs, **more_kwargs})
    
    return curried

# ===== METAPROGRAMMING =====

class MethodLogger:
    """
    Metaclass that logs method calls
    """
    
    def __new__(cls, name, bases, attrs):
        for key, value in attrs.items():
            if callable(value):
                attrs[key] = cls.log_method(value)
        return super().__new__(cls, name, bases, attrs)
    
    @staticmethod
    def log_method(func: Callable) -> Callable:
        """
        Wrap method with logging
        Parameters:
            func (Callable): Method to wrap
        Returns:
            Callable: Wrapped method
        """
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned {result}")
            return result
        return wrapper

# ===== DECORATED FUNCTIONS =====

@timer_decorator
@cache_decorator
def fibonacci_recursive(n: int) -> int:
    """
    Recursive Fibonacci function with decorators
    Parameters:
        n (int): Fibonacci number to calculate
    Returns:
        int: Fibonacci number
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

@retry_decorator(max_retries=3, delay=0.5)
@validate_types(x=int, y=int)
def divide_with_retry(x: int, y: int) -> float:
    """
    Division function with retry and type validation
    Parameters:
        x (int): Numerator
        y (int): Denominator
    Returns:
        float: Division result
    """
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

# ===== DEMONSTRATION FUNCTIONS =====

def demo_iterators():
    """Demonstrate iterator functionality"""
    print("=== Iterator Demo ===")
    
    custom_iter = CustomIterator(1, 2, 3, 4, 5)
    
    print("For loop iteration:")
    for i in custom_iter:
        print(f"  Element: {i}")
    
    print("\nManual iteration:")
    A = iter(custom_iter)
    try:
        while True:
            element = next(A)
            print(f"  Element: {element}")
    except StopIteration as e:
        print(f"  Iteration stopped: {e}")

def demo_generators():
    """Demonstrate generator functionality"""
    print("\n=== Generator Demo ===")
    
    # Basic generator
    print("Number generator:")
    gen = number_generator()
    for i in range(5):
        print(f"  {next(gen)}")
    
    # Fibonacci generator
    print("\nFibonacci generator:")
    for num in fibonacci_generator(10):
        print(f"  {num}")
    
    # Prime generator
    print("\nPrime generator:")
    for prime in prime_generator(20):
        print(f"  {prime}")

def demo_decorators():
    """Demonstrate decorator functionality"""
    print("\n=== Decorator Demo ===")
    
    # Timer and cache decorators
    print("Fibonacci with timing and caching:")
    print(f"Fibonacci(10): {fibonacci_recursive(10)}")
    print(f"Fibonacci(10) again: {fibonacci_recursive(10)}")
    
    # Retry and validation decorators
    print("\nDivision with retry and validation:")
    try:
        result = divide_with_retry(10, 2)
        print(f"10 / 2 = {result}")
        
        result = divide_with_retry(10, 0)  # This will retry and fail
    except Exception as e:
        print(f"Final error: {e}")

def demo_closures():
    """Demonstrate closure functionality"""
    print("\n=== Closure Demo ===")
    
    # Multiplier closure
    double = create_multiplier(2)
    triple = create_multiplier(3)
    
    print(f"Double 5: {double(5)}")
    print(f"Triple 5: {triple(5)}")
    
    # Accumulator closure
    acc = create_accumulator()
    print(f"Accumulator: {acc(5)}")
    print(f"Accumulator: {acc(10)}")
    print(f"Accumulator: {acc(15)}")

def demo_functional_programming():
    """Demonstrate functional programming concepts"""
    print("\n=== Functional Programming Demo ===")
    
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Map-filter-reduce
    result = map_filter_reduce(
        data,
        lambda x: x ** 2,  # Square each number
        lambda x: x % 2 == 0,  # Keep even numbers
        lambda x, y: x + y  # Sum all numbers
    )
    
    print(f"Map-filter-reduce result: {result}")
    
    # Function composition
    add_one = lambda x: x + 1
    multiply_by_two = lambda x: x * 2
    composed = compose_functions(multiply_by_two, add_one)
    
    print(f"Composed function (add one then multiply by two): {composed(5)}")

def demo_advanced_algorithms():
    """Demonstrate advanced algorithms"""
    print("\n=== Advanced Algorithms Demo ===")
    
    data = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]
    
    print(f"Original data: {data}")
    print(f"Quick sort: {quick_sort(data)}")
    print(f"Merge sort: {merge_sort(data)}")

if __name__ == "__main__":
    demo_iterators()
    demo_generators()
    demo_decorators()
    demo_closures()
    demo_functional_programming()
    demo_advanced_algorithms()
    
    print("\n=== Key Concepts Summary ===")
    print("1. Iterators implement __iter__() and __next__() methods")
    print("2. Generators use 'yield' keyword for lazy evaluation")
    print("3. Decorators modify function behavior without changing code")
    print("4. Closures capture variables from enclosing scope")
    print("5. Functional programming emphasizes immutability and pure functions")
    print("6. Advanced algorithms include efficient sorting and searching")
    print("7. Metaprogramming allows code to manipulate other code")

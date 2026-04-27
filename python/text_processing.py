# Text Processing Module - Complete Text Functionality
# This module provides comprehensive text processing including string utilities and validation

import re
from typing import List, Dict

# ===== STRING UTILITIES =====

def reverse_string(s: str) -> str:
    """
    Reverse a string
    Parameters:
        s (str): String to reverse
    Returns:
        str: Reversed string
    """
    return s[::-1]

def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome
    Parameters:
        s (str): String to check
    Returns:
        bool: True if palindrome, False otherwise
    """
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    return cleaned == cleaned[::-1]

def count_vowels(s: str) -> int:
    """
    Count vowels in a string
    Parameters:
        s (str): String to analyze
    Returns:
        int: Number of vowels
    """
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def count_consonants(s: str) -> int:
    """
    Count consonants in a string
    Parameters:
        s (str): String to analyze
    Returns:
        int: Number of consonants
    """
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char.isalpha() and char not in vowels)

def capitalize_words(s: str) -> str:
    """
    Capitalize first letter of each word
    Parameters:
        s (str): String to capitalize
    Returns:
        str: Capitalized string
    """
    return ' '.join(word.capitalize() for word in s.split())

def remove_duplicates(s: str) -> str:
    """
    Remove duplicate characters from string
    Parameters:
        s (str): String to process
    Returns:
        str: String with duplicates removed
    """
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

def find_all_substrings(s: str) -> List[str]:
    """
    Find all possible substrings
    Parameters:
        s (str): String to analyze
    Returns:
        List[str]: List of all substrings
    """
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

def word_frequency(s: str) -> dict:
    """
    Count frequency of each word
    Parameters:
        s (str): Text to analyze
    Returns:
        dict: Word frequency dictionary
    """
    words = s.lower().split()
    frequency = {}
    for word in words:
        word = re.sub(r'[^a-zA-Z0-9]', '', word)
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    return frequency

def find_email_addresses(text: str) -> List[str]:
    """
    Find all email addresses in text
    Parameters:
        text (str): Text to search
    Returns:
        List[str]: List of email addresses
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

def find_phone_numbers(text: str) -> List[str]:
    """
    Find all phone numbers in text
    Parameters:
        text (str): Text to search
    Returns:
        List[str]: List of phone numbers
    """
    pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    return re.findall(pattern, text)

def extract_urls(text: str) -> List[str]:
    """
    Extract all URLs from text
    Parameters:
        text (str): Text to search
    Returns:
        List[str]: List of URLs
    """
    pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    return re.findall(pattern, text)

def format_bytes(bytes_count: int) -> str:
    """
    Format bytes into human readable format
    Parameters:
        bytes_count (int): Number of bytes
    Returns:
        str: Formatted string
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_count < 1024:
            return f"{bytes_count:.2f} {unit}"
        bytes_count /= 1024
    return f"{bytes_count:.2f} PB"

# ===== VALIDATION FUNCTIONS =====

def is_email(email: str) -> bool:
    """
    Validate email address format
    Parameters:
        email (str): Email address to validate
    Returns:
        bool: True if valid email format, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_phone_number(phone: str) -> bool:
    """
    Validate phone number format (basic validation)
    Parameters:
        phone (str): Phone number to validate
    Returns:
        bool: True if valid phone format, False otherwise
    """
    pattern = r'^\+?[\d\s-]{10,}$'
    return re.match(pattern, phone) is not None

def is_url(url: str) -> bool:
    """
    Validate URL format
    Parameters:
        url (str): URL to validate
    Returns:
        bool: True if valid URL format, False otherwise
    """
    pattern = r'^(https?://)?([\da-z\.-]+)\.([a-z\.]{2,6})([/\w \.-]*)*/?$'
    return re.match(pattern, url) is not None

def is_strong_password(password: str) -> bool:
    """
    Validate password strength
    Parameters:
        password (str): Password to validate
    Returns:
        bool: True if password meets strength requirements
    """
    if len(password) < 8:
        return False
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password)
    
    return has_upper and has_lower and has_digit and has_special

def is_positive_number(value) -> bool:
    """
    Check if value is a positive number
    Parameters:
        value: Value to check
    Returns:
        bool: True if positive number, False otherwise
    """
    try:
        num = float(value)
        return num > 0
    except (ValueError, TypeError):
        return False

def is_valid_age(age: str) -> bool:
    """
    Validate age (must be between 0 and 120)
    Parameters:
        age (str): Age to validate
    Returns:
        bool: True if valid age, False otherwise
    """
    try:
        age_int = int(age)
        return 0 <= age_int <= 120
    except (ValueError, TypeError):
        return False

def validate_credit_card(card_number: str) -> bool:
    """
    Validate credit card number using Luhn algorithm
    Parameters:
        card_number (str): Credit card number to validate
    Returns:
        bool: True if valid credit card number, False otherwise
    """
    digits = [int(d) for d in card_number.replace(' ', '') if d.isdigit()]
    if len(digits) not in [13, 14, 15, 16, 19]:
        return False
    
    checksum = 0
    for i, digit in enumerate(reversed(digits)):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    
    return checksum % 10 == 0

# ===== ADVANCED TEXT PROCESSING =====

def clean_text(text: str) -> str:
    """
    Clean text by removing extra whitespace and special characters
    Parameters:
        text (str): Text to clean
    Returns:
        str: Cleaned text
    """
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove special characters except basic punctuation
    text = re.sub(r'[^\w\s.,!?;:]', '', text)
    
    # Strip leading/trailing whitespace
    return text.strip()

def extract_keywords(text: str, min_length: int = 3) -> List[str]:
    """
    Extract keywords from text
    Parameters:
        text (str): Text to analyze
        min_length (int): Minimum keyword length
    Returns:
        List[str]: List of keywords
    """
    # Common stop words
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they'}
    
    words = re.findall(r'\b\w+\b', text.lower())
    keywords = [word for word in words if word not in stop_words and len(word) >= min_length]
    
    # Return unique keywords
    return list(set(keywords))

def calculate_readability_score(text: str) -> float:
    """
    Calculate basic readability score
    Parameters:
        text (str): Text to analyze
    Returns:
        float: Readability score (0-100, higher is easier)
    """
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    words = re.findall(r'\b\w+\b', text)
    
    if not sentences or not words:
        return 0.0
    
    avg_sentence_length = len(words) / len(sentences)
    avg_word_length = sum(len(word) for word in words) / len(words)
    
    # Simple readability formula (higher score = easier to read)
    readability = 100 - (avg_sentence_length * 1.5) - (avg_word_length * 2)
    
    return max(0, min(100, readability))

def text_similarity(text1: str, text2: str) -> float:
    """
    Calculate similarity between two texts using Jaccard similarity
    Parameters:
        text1 (str): First text
        text2 (str): Second text
    Returns:
        float: Similarity score (0-1)
    """
    words1 = set(re.findall(r'\b\w+\b', text1.lower()))
    words2 = set(re.findall(r'\b\w+\b', text2.lower()))
    
    intersection = words1.intersection(words2)
    union = words1.union(words2)
    
    if not union:
        return 0.0
    
    return len(intersection) / len(union)

# ===== DEMONSTRATION FUNCTIONS =====

def demo_string_utilities():
    """Demonstrate string utility functions"""
    print("=== String Utilities Demo ===")
    test_string = "Hello World! This is a test string with 123 numbers."
    
    print("Original:", test_string)
    print("Reversed:", reverse_string(test_string))
    print("Is palindrome:", is_palindrome(test_string))
    print("Vowel count:", count_vowels(test_string))
    print("Consonant count:", count_consonants(test_string))
    print("Capitalized:", capitalize_words(test_string))
    print("Word frequency:", word_frequency(test_string))

def demo_text_extraction():
    """Demonstrate text extraction functions"""
    print("\n=== Text Extraction Demo ===")
    sample_text = """
    Contact us at info@example.com or support@company.org
    Call us at 555-123-4567 or +1 800 555 0199
    Visit our website at https://www.example.com or http://test.org
    """
    
    print("Sample text:", sample_text.strip())
    print("Email addresses:", find_email_addresses(sample_text))
    print("Phone numbers:", find_phone_numbers(sample_text))
    print("URLs:", extract_urls(sample_text))

def demo_validation():
    """Demonstrate validation functions"""
    print("\n=== Validation Functions Demo ===")
    print("Email validation:", is_email("test@example.com"))
    print("Phone validation:", is_phone_number("+90 555 123 4567"))
    print("URL validation:", is_url("https://www.example.com"))
    print("Password strength:", is_strong_password("StrongPass123!"))
    print("Positive number:", is_positive_number("42.5"))
    print("Age validation:", is_valid_age("25"))
    print("Credit card validation:", validate_credit_card("4532 1234 5678 9012"))

def demo_advanced_processing():
    """Demonstrate advanced text processing"""
    print("\n=== Advanced Text Processing Demo ===")
    
    text1 = "This is a sample text for processing. It contains various words and sentences."
    text2 = "This is another sample text with some similar words but different content."
    
    print("Text 1:", text1)
    print("Text 2:", text2)
    print("Cleaned text 1:", clean_text(text1))
    print("Keywords from text 1:", extract_keywords(text1))
    print("Readability score:", calculate_readability_score(text1))
    print("Text similarity:", text_similarity(text1, text2))

if __name__ == "__main__":
    demo_string_utilities()
    demo_text_extraction()
    demo_validation()
    demo_advanced_processing()

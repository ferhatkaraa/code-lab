# Date Time Utils Module - Date and Time Manipulation Functions
# This module provides utilities for working with dates and times

from datetime import datetime, timedelta, date
import time

def get_current_datetime() -> datetime:
    """
    Get current date and time
    Returns:
        datetime: Current datetime object
    """
    return datetime.now()

def format_datetime(dt: datetime, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Format datetime as string
    Parameters:
        dt (datetime): Datetime object to format
        format_str (str): Format string (default: "%Y-%m-%d %H:%M:%S")
    Returns:
        str: Formatted datetime string
    """
    return dt.strftime(format_str)

def parse_datetime(date_str: str, format_str: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """
    Parse string to datetime object
    Parameters:
        date_str (str): Date string to parse
        format_str (str): Format string (default: "%Y-%m-%d %H:%M:%S")
    Returns:
        datetime: Parsed datetime object
    """
    return datetime.strptime(date_str, format_str)

def add_days(dt: datetime, days: int) -> datetime:
    """
    Add days to datetime
    Parameters:
        dt (datetime): Original datetime
        days (int): Number of days to add
    Returns:
        datetime: New datetime with days added
    """
    return dt + timedelta(days=days)

def days_between(date1: datetime, date2: datetime) -> int:
    """
    Calculate days between two dates
    Parameters:
        date1 (datetime): First date
        date2 (datetime): Second date
    Returns:
        int: Number of days between dates
    """
    return abs((date2 - date1).days)

def is_weekend(dt: datetime) -> bool:
    """
    Check if date is weekend (Saturday or Sunday)
    Parameters:
        dt (datetime): Date to check
    Returns:
        bool: True if weekend, False otherwise
    """
    return dt.weekday() in [5, 6]

def get_age(birth_date: date) -> int:
    """
    Calculate age from birth date
    Parameters:
        birth_date (date): Birth date
    Returns:
        int: Age in years
    """
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

def get_month_name(month: int) -> str:
    """
    Get month name from month number
    Parameters:
        month (int): Month number (1-12)
    Returns:
        str: Month name
    """
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    if 1 <= month <= 12:
        return months[month - 1]
    raise ValueError("Month must be between 1 and 12")

def get_day_of_week(dt: datetime) -> str:
    """
    Get day of week name
    Parameters:
        dt (datetime): Date to get day for
    Returns:
        str: Day of week name
    """
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[dt.weekday()]

def is_leap_year(year: int) -> bool:
    """
    Check if year is leap year
    Parameters:
        year (int): Year to check
    Returns:
        bool: True if leap year, False otherwise
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_quarter(dt: datetime) -> int:
    """
    Get quarter of the year
    Parameters:
        dt (datetime): Date to get quarter for
    Returns:
        int: Quarter number (1-4)
    """
    month = dt.month
    if month <= 3:
        return 1
    elif month <= 6:
        return 2
    elif month <= 9:
        return 3
    else:
        return 4

# Demonstration of date time utility functions
if __name__ == "__main__":
    print("=== Date Time Utils Demo ===")
    
    current = get_current_datetime()
    print("Current datetime:", current)
    print("Formatted datetime:", format_datetime(current))
    print("Month name:", get_month_name(current.month))
    print("Day of week:", get_day_of_week(current))
    print("Quarter:", get_quarter(current))
    print("Is weekend:", is_weekend(current))
    print("Is leap year:", is_leap_year(current.year))
    
    future_date = add_days(current, 30)
    print("Date 30 days from now:", format_datetime(future_date))
    print("Days between current and future date:", days_between(current, future_date))
    
    birth_date = date(1990, 5, 15)
    print("Age for birth date 1990-05-15:", get_age(birth_date))

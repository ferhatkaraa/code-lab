# Data Management Module - Complete Data Functionality
# This module provides comprehensive data management including file operations and data processing

import json
import csv
import os
from pathlib import Path
from typing import List, Dict, Any, Optional
import hashlib

# ===== DATA PROCESSOR CLASS =====

class DataProcessor:
    """
    A comprehensive class for processing various data formats
    Supports JSON and CSV files with filtering, sorting, and analysis capabilities
    """
    
    def __init__(self):
        """Initialize DataProcessor with empty data list"""
        self.data = []
    
    def load_json(self, file_path: str) -> List[Dict]:
        """
        Load data from JSON file into the data list
        Parameters:
            file_path (str): Path to the JSON file
        Returns:
            List[Dict]: Loaded data as list of dictionaries
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
                return self.data
        except FileNotFoundError:
            print(f"File {file_path} not found")
            return []
        except json.JSONDecodeError:
            print(f"Invalid JSON format in {file_path}")
            return []
    
    def load_csv(self, file_path: str) -> List[Dict]:
        """
        Load data from CSV file into the data list
        Parameters:
            file_path (str): Path to the CSV file
        Returns:
            List[Dict]: Loaded data as list of dictionaries
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.data = list(reader)
                return self.data
        except FileNotFoundError:
            print(f"File {file_path} not found")
            return []
    
    def filter_data(self, key: str, value: Any) -> List[Dict]:
        """
        Filter data by key and value
        Parameters:
            key (str): Key to filter by
            value (Any): Value to match
        Returns:
            List[Dict]: Filtered data
        """
        return [item for item in self.data if item.get(key) == value]
    
    def get_unique_values(self, key: str) -> List[Any]:
        """
        Get unique values for a specific key
        Parameters:
            key (str): Key to analyze
        Returns:
            List[Any]: List of unique values
        """
        return list(set(item.get(key) for item in self.data if key in item))
    
    def sort_data(self, key: str, reverse: bool = False) -> List[Dict]:
        """
        Sort data by key
        Parameters:
            key (str): Key to sort by
            reverse (bool): Sort order (default: False)
        Returns:
            List[Dict]: Sorted data
        """
        return sorted(self.data, key=lambda x: x.get(key, ''), reverse=reverse)
    
    def get_statistics(self, numeric_key: str) -> Dict[str, float]:
        """
        Get basic statistics for numeric data
        Parameters:
            numeric_key (str): Key with numeric values
        Returns:
            Dict[str, float]: Statistics dictionary
        """
        numeric_values = [float(item.get(numeric_key, 0)) for item in self.data 
                         if str(item.get(numeric_key, '')).replace('.', '').isdigit()]
        
        if not numeric_values:
            return {}
        
        return {
            'count': len(numeric_values),
            'mean': sum(numeric_values) / len(numeric_values),
            'max': max(numeric_values),
            'min': min(numeric_values)
        }
    
    def export_to_json(self, file_path: str) -> bool:
        """
        Export data to JSON file
        Parameters:
            file_path (str): Output file path
        Returns:
            bool: True if successful
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(self.data, file, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error exporting to JSON: {e}")
            return False

# ===== FILE MANAGER CLASS =====

class FileManager:
    """
    A class for managing file operations
    """
    
    def __init__(self, base_path: str = "."):
        """
        Initialize FileManager with base path
        Parameters:
            base_path (str): Base directory path
        """
        self.base_path = Path(base_path)
    
    def create_directory(self, dir_name: str) -> bool:
        """
        Create a new directory
        Parameters:
            dir_name (str): Directory name
        Returns:
            bool: True if successful
        """
        try:
            dir_path = self.base_path / dir_name
            dir_path.mkdir(exist_ok=True)
            return True
        except Exception as e:
            print(f"Error creating directory: {e}")
            return False
    
    def create_file(self, file_name: str, content: str = "") -> bool:
        """
        Create a new file with content
        Parameters:
            file_name (str): File name
            content (str): File content
        Returns:
            bool: True if successful
        """
        try:
            file_path = self.base_path / file_name
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            return True
        except Exception as e:
            print(f"Error creating file: {e}")
            return False
    
    def read_file(self, file_name: str) -> Optional[str]:
        """
        Read content from a file
        Parameters:
            file_name (str): File name
        Returns:
            Optional[str]: File content or None
        """
        try:
            file_path = self.base_path / file_name
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            return None
    
    def delete_file(self, file_name: str) -> bool:
        """
        Delete a file
        Parameters:
            file_name (str): File name
        Returns:
            bool: True if successful
        """
        try:
            file_path = self.base_path / file_name
            if file_path.exists():
                file_path.unlink()
                return True
            return False
        except Exception as e:
            print(f"Error deleting file: {e}")
            return False
    
    def copy_file(self, source: str, destination: str) -> bool:
        """
        Copy a file to destination
        Parameters:
            source (str): Source file name
            destination (str): Destination file name
        Returns:
            bool: True if successful
        """
        try:
            source_path = self.base_path / source
            dest_path = self.base_path / destination
            import shutil
            shutil.copy2(source_path, dest_path)
            return True
        except Exception as e:
            print(f"Error copying file: {e}")
            return False
    
    def move_file(self, source: str, destination: str) -> bool:
        """
        Move a file to destination
        Parameters:
            source (str): Source file name
            destination (str): Destination file name
        Returns:
            bool: True if successful
        """
        try:
            source_path = self.base_path / source
            dest_path = self.base_path / destination
            import shutil
            shutil.move(source_path, dest_path)
            return True
        except Exception as e:
            print(f"Error moving file: {e}")
            return False
    
    def list_files(self, extension: Optional[str] = None) -> List[str]:
        """
        List all files in directory
        Parameters:
            extension (Optional[str]): File extension filter
        Returns:
            List[str]: List of file names
        """
        files = []
        try:
            for item in self.base_path.iterdir():
                if item.is_file():
                    if extension is None or item.suffix == extension:
                        files.append(item.name)
            return sorted(files)
        except Exception as e:
            print(f"Error listing files: {e}")
            return []
    
    def get_file_size(self, file_name: str) -> Optional[int]:
        """
        Get file size in bytes
        Parameters:
            file_name (str): File name
        Returns:
            Optional[int]: File size or None
        """
        try:
            file_path = self.base_path / file_name
            if file_path.exists():
                return file_path.stat().st_size
            return None
        except Exception as e:
            print(f"Error getting file size: {e}")
            return None
    
    def get_file_hash(self, file_name: str, algorithm: str = 'md5') -> Optional[str]:
        """
        Get hash of file content
        Parameters:
            file_name (str): File name
            algorithm (str): Hash algorithm
        Returns:
            Optional[str]: File hash or None
        """
        try:
            file_path = self.base_path / file_name
            if not file_path.exists():
                return None
            
            hash_func = hashlib.new(algorithm)
            with open(file_path, 'rb') as file:
                for chunk in iter(lambda: file.read(4096), b""):
                    hash_func.update(chunk)
            return hash_func.hexdigest()
        except Exception as e:
            print(f"Error calculating file hash: {e}")
            return None
    
    def search_in_files(self, pattern: str, extension: Optional[str] = None) -> List[str]:
        """
        Search for pattern in files
        Parameters:
            pattern (str): Search pattern
            extension (Optional[str]): File extension filter
        Returns:
            List[str]: List of matching files
        """
        matching_files = []
        files = self.list_files(extension)
        
        for file_name in files:
            content = self.read_file(file_name)
            if content and pattern in content:
                matching_files.append(file_name)
        
        return matching_files

# ===== DATA ANALYSIS UTILITIES =====

def analyze_data_structure(data: List[Dict]) -> Dict[str, Any]:
    """
    Analyze the structure of data
    Parameters:
        data (List[Dict]): Data to analyze
    Returns:
        Dict[str, Any]: Structure analysis
    """
    if not data:
        return {"total_records": 0, "fields": [], "field_types": {}}
    
    all_fields = set()
    field_types = {}
    
    for record in data:
        for key, value in record.items():
            all_fields.add(key)
            if key not in field_types:
                field_types[key] = set()
            field_types[key].add(type(value).__name__)
    
    return {
        "total_records": len(data),
        "fields": sorted(list(all_fields)),
        "field_types": {k: sorted(list(v)) for k, v in field_types.items()}
    }

def clean_data(data: List[Dict], rules: Dict[str, Any]) -> List[Dict]:
    """
    Clean data based on rules
    Parameters:
        data (List[Dict]): Data to clean
        rules (Dict[str, Any]): Cleaning rules
    Returns:
        List[Dict]: Cleaned data
    """
    cleaned_data = []
    
    for record in data:
        cleaned_record = {}
        
        for field, value in record.items():
            # Apply cleaning rules
            if field in rules:
                rule = rules[field]
                
                # Remove empty values
                if rule.get("remove_empty") and not value:
                    continue
                
                # Convert to lowercase
                if rule.get("lowercase") and isinstance(value, str):
                    value = value.lower()
                
                # Strip whitespace
                if rule.get("strip") and isinstance(value, str):
                    value = value.strip()
                
                # Replace None with default
                if rule.get("replace_none") and value is None:
                    value = rule.get("default_value", "")
            
            cleaned_record[field] = value
        
        cleaned_data.append(cleaned_record)
    
    return cleaned_data

def merge_data_sources(data1: List[Dict], data2: List[Dict], key_field: str) -> List[Dict]:
    """
    Merge two data sources on a key field
    Parameters:
        data1 (List[Dict]): First data source
        data2 (List[Dict]): Second data source
        key_field (str): Field to merge on
    Returns:
        List[Dict]: Merged data
    """
    merged_data = {}
    
    # Add first data source
    for record in data1:
        if key_field in record:
            merged_data[record[key_field]] = record.copy()
    
    # Merge second data source
    for record in data2:
        if key_field in record and record[key_field] in merged_data:
            merged_data[record[key_field]].update(record)
        else:
            merged_data[record[key_field]] = record.copy()
    
    return list(merged_data.values())

# ===== DEMONSTRATION FUNCTIONS =====

def demo_data_processor():
    """Demonstrate DataProcessor functionality"""
    print("=== DataProcessor Demo ===")
    
    # Create sample data
    sample_data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"},
        {"name": "Charlie", "age": 35, "city": "Chicago"}
    ]
    
    processor = DataProcessor()
    processor.data = sample_data
    
    print("Original data:", processor.data)
    print("Filter by city 'New York':", processor.filter_data("city", "New York"))
    print("Unique cities:", processor.get_unique_values("city"))
    print("Sort by age:", processor.sort_data("age"))
    print("Age statistics:", processor.get_statistics("age"))

def demo_file_manager():
    """Demonstrate FileManager functionality"""
    print("\n=== FileManager Demo ===")
    
    fm = FileManager()
    
    # Create test file
    fm.create_file("test.txt", "This is a test file")
    print("Created test.txt")
    
    # List files
    print("Files:", fm.list_files())
    
    # Read file
    content = fm.read_file("test.txt")
    print("File content:", content)
    
    # Get file info
    print("File size:", fm.get_file_size("test.txt"))
    print("File hash:", fm.get_file_hash("test.txt"))
    
    # Clean up
    fm.delete_file("test.txt")
    print("Deleted test.txt")

def demo_data_analysis():
    """Demonstrate data analysis functionality"""
    print("\n=== Data Analysis Demo ===")
    
    sample_data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"},
        {"name": "Charlie", "age": 35, "city": "Chicago"}
    ]
    
    # Analyze structure
    structure = analyze_data_structure(sample_data)
    print("Data structure:", structure)
    
    # Clean data
    cleaning_rules = {
        "name": {"lowercase": True, "strip": True},
        "city": {"lowercase": True, "strip": True}
    }
    cleaned = clean_data(sample_data, cleaning_rules)
    print("Cleaned data:", cleaned)

if __name__ == "__main__":
    demo_data_processor()
    demo_file_manager()
    demo_data_analysis()

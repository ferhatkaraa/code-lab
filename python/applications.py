# Applications Module - Complete Specialized Applications
# This module provides comprehensive specialized applications including web automation, device management, OCR, and grading

import pywin32_bootstrap
import pygame
import bluetooth
from selenium import webdriver
import tesseract
from PIL import Image
import cv2
import os
import time

# ===== WEB AUTOMATION =====

class WebAutomation:
    """
    Web automation class using Selenium WebDriver
    """
    
    def __init__(self, browser_type="edge"):
        """
        Initialize web automation
        Parameters:
            browser_type (str): Type of browser (default: "edge")
        """
        self.driver = None
        self.browser_type = browser_type
    
    def create_webdriver(self):
        """
        Create and return a WebDriver instance
        Returns:
            WebDriver: WebDriver instance
        """
        if self.browser_type.lower() == "edge":
            self.driver = webdriver.Edge()
        elif self.browser_type.lower() == "chrome":
            self.driver = webdriver.Chrome()
        elif self.browser_type.lower() == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser type: {self.browser_type}")
        
        return self.driver
    
    def navigate_to_url(self, url):
        """
        Navigate to a specific URL
        Parameters:
            url (str): URL to navigate to
        """
        if not self.driver:
            self.create_webdriver()
        
        self.driver.get(url)
        self.driver.implicitly_wait(5)
    
    def display_page_info(self):
        """
        Display page title and separator
        """
        if not self.driver:
            return
        
        print("--------------------------------------------")
        print(self.driver.title)
        print("--------------------------------------------")
    
    def keep_browser_open(self):
        """
        Keep browser open until user decides to close
        """
        if not self.driver:
            return
        
        while True:
            user_input = input("Programı kapatmak için 'q' tuşuna basın: ")
            if user_input.lower() == "q":
                self.driver.quit()
                print("Programınız kapatılıyor...")
                break
            else:
                continue
    
    def close_browser(self):
        """
        Close the browser
        """
        if self.driver:
            self.driver.quit()
            self.driver = None

# ===== BLUETOOTH SCREEN INTEGRATION =====

class BluetoothScreenManager:
    """
    Bluetooth device discovery and screen display manager
    """
    
    def __init__(self):
        """Initialize Bluetooth screen manager"""
        self.sock = None
        self.screen = None
    
    def discover_bluetooth_devices(self):
        """
        Discover nearby Bluetooth devices
        Returns:
            list: List of discovered Bluetooth devices
        """
        print("Bluetooth cihazları aranıyor...")
        nearby_devices = bluetooth.discover_devices()
        return nearby_devices
    
    def list_bluetooth_devices(self, devices):
        """
        List discovered Bluetooth devices with indices
        Parameters:
            devices (list): List of Bluetooth device addresses
        """
        print("Bulunan Bluetooth Cihazları:")
        for i, device in enumerate(devices):
            print(f"{i}: {device}")
    
    def select_bluetooth_device(self, devices):
        """
        Allow user to select a Bluetooth device
        Parameters:
            devices (list): List of Bluetooth device addresses
        Returns:
            str: Selected device address
        """
        try:
            selected_device = int(input("Lütfen bağlanmak istediğiniz cihazın numarasını girin: "))
            if 0 <= selected_device < len(devices):
                return devices[selected_device]
            else:
                raise ValueError("Geçersiz cihaz numarası")
        except ValueError as e:
            print(f"Hata: {e}")
            return None
    
    def connect_bluetooth(self, address):
        """
        Connect to Bluetooth device
        Parameters:
            address (str): Bluetooth device address
        Returns:
            BluetoothSocket: Connected socket or None if failed
        """
        try:
            self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.sock.connect((address, 1))
            print(f"Bluetooth cihazına bağlandı: {address}")
            return self.sock
        except Exception as e:
            print(f"Bluetooth bağlantı hatası: {e}")
            return None
    
    def initialize_screen(self):
        """
        Initialize Pygame screen in fullscreen mode
        Returns:
            pygame.Surface: Screen surface
        """
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Bluetooth Ekran Gösterimi")
        return self.screen
    
    def display_bluetooth_data(self):
        """
        Display Bluetooth data on screen
        Returns:
            bool: True to continue, False to exit
        """
        if not self.sock or not self.screen:
            return False
        
        try:
            # Receive Bluetooth data
            data = self.sock.recv(1024)
            
            # Create image from data (assuming RGB format, 640x480)
            image = pygame.image.fromstring(data, (640, 480), "RGB")
            
            # Display image on screen
            self.screen.blit(image, (0, 0))
            pygame.display.flip()
            
            return True
        except Exception as e:
            print(f"Veri gösterim hatası: {e}")
            return False
    
    def check_exit_events(self):
        """
        Check for exit events (ESC key)
        Returns:
            bool: True if should exit, False otherwise
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return True
        return False
    
    def run_bluetooth_screen_app(self):
        """
        Run the complete Bluetooth screen application
        """
        # Discover and list Bluetooth devices
        devices = self.discover_bluetooth_devices()
        if not devices:
            print("Hiç Bluetooth cihazı bulunamadı.")
            return
        
        self.list_bluetooth_devices(devices)
        
        # Select and connect to device
        address = self.select_bluetooth_device(devices)
        if not address:
            return
        
        if not self.connect_bluetooth(address):
            return
        
        # Initialize screen
        self.initialize_screen()
        
        # Main loop
        running = True
        while running:
            # Check for exit events
            if self.check_exit_events():
                running = False
            
            # Display Bluetooth data
            if not self.display_bluetooth_data():
                running = False
        
        # Cleanup
        if self.sock:
            self.sock.close()
        pygame.quit()
        print("Program sonlandırıldı.")

# ===== OCR IMAGE PROCESSOR =====

class OCRImageProcessor:
    """
    OCR image processing class
    """
    
    def __init__(self, tesseract_path=None):
        """
        Initialize OCR processor
        Parameters:
            tesseract_path (str): Path to Tesseract OCR installation
        """
        self.tesseract_path = tesseract_path
        if tesseract_path:
            self.configure_tesseract(tesseract_path)
    
    def configure_tesseract(self, tesseract_path):
        """
        Configure Tesseract OCR path
        Parameters:
            tesseract_path (str): Path to Tesseract OCR installation
        """
        try:
            tesseract.config(tesseract_path)
            print("Tesseract OCR configured successfully")
        except Exception as e:
            print(f"Error configuring Tesseract: {e}")
    
    def extract_text_from_pil_image(self, image_path, language='tur'):
        """
        Extract text from image using PIL
        Parameters:
            image_path (str): Path to image file
            language (str): Language for OCR (default: 'tur' for Turkish)
        Returns:
            str: Extracted text
        """
        try:
            # Load image using PIL
            img = Image.open(image_path)
            
            # Perform OCR
            text = tesseract.image_to_string(img, lang=language)
            
            # Close image
            img.close()
            
            return text
        except FileNotFoundError:
            print(f"Image file not found: {image_path}")
            return ""
        except Exception as e:
            print(f"Error processing PIL image: {e}")
            return ""
    
    def extract_text_from_opencv_image(self, image_path, language='tur'):
        """
        Extract text from image using OpenCV
        Parameters:
            image_path (str): Path to image file
            language (str): Language for OCR (default: 'tur' for Turkish)
        Returns:
            str: Extracted text
        """
        try:
            # Load image using OpenCV
            img = cv2.imread(image_path)
            
            if img is None:
                print(f"Could not load image: {image_path}")
                return ""
            
            # Perform OCR
            text = tesseract.image_to_string(img, lang=language)
            
            return text
        except Exception as e:
            print(f"Error processing OpenCV image: {e}")
            return ""
    
    def preprocess_image(self, image_path):
        """
        Preprocess image for better OCR results
        Parameters:
            image_path (str): Path to image file
        Returns:
            numpy.ndarray: Preprocessed image
        """
        try:
            # Load image
            img = cv2.imread(image_path)
            
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Apply threshold to get binary image
            _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            
            # Remove noise
            denoised = cv2.medianBlur(binary, 5)
            
            return denoised
        except Exception as e:
            print(f"Error preprocessing image: {e}")
            return None
    
    def extract_text_with_preprocessing(self, image_path, language='tur'):
        """
        Extract text from image with preprocessing
        Parameters:
            image_path (str): Path to image file
            language (str): Language for OCR (default: 'tur' for Turkish)
        Returns:
            str: Extracted text
        """
        try:
            # Preprocess image
            processed_img = self.preprocess_image(image_path)
            
            if processed_img is None:
                return ""
            
            # Perform OCR on preprocessed image
            text = tesseract.image_to_string(processed_img, lang=language)
            
            return text
        except Exception as e:
            print(f"Error in OCR with preprocessing: {e}")
            return ""
    
    def batch_ocr_processing(self, image_folder, output_folder, language='tur'):
        """
        Process multiple images in a folder
        Parameters:
            image_folder (str): Folder containing images
            output_folder (str): Folder to save extracted text
            language (str): Language for OCR
        """
        try:
            # Create output folder if it doesn't exist
            os.makedirs(output_folder, exist_ok=True)
            
            # Get all image files
            image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
            image_files = []
            
            for file in os.listdir(image_folder):
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    image_files.append(file)
            
            print(f"Found {len(image_files)} images to process")
            
            # Process each image
            for image_file in image_files:
                image_path = os.path.join(image_folder, image_file)
                
                # Extract text using different methods
                text_pil = self.extract_text_from_pil_image(image_path, language)
                text_cv2 = self.extract_text_from_opencv_image(image_path, language)
                text_preprocessed = self.extract_text_with_preprocessing(image_path, language)
                
                # Save results
                base_name = os.path.splitext(image_file)[0]
                output_path = os.path.join(output_folder, f"{base_name}_extracted_text.txt")
                
                combined_text = f"=== PIL Extraction ===\n{text_pil}\n\n"
                combined_text += f"=== OpenCV Extraction ===\n{text_cv2}\n\n"
                combined_text += f"=== Preprocessed Extraction ===\n{text_preprocessed}\n"
                
                with open(output_path, 'w', encoding='utf-8') as file:
                    file.write(combined_text)
                
                print(f"Processed {image_file} -> {output_path}")
                
        except Exception as e:
            print(f"Error in batch processing: {e}")

# ===== GRADE CALCULATOR =====

class GradeCalculator:
    """
    Grade calculation and management system
    """
    
    def __init__(self):
        """Initialize grade calculator"""
        self.letter_grades = ["FD", "FD", "DD", "CD", "CC", "BC", "BB", "BA", "AA", "AA", "AA"]
    
    def convert_numeric_to_letter_grade(self, score):
        """
        Convert numeric score to letter grade
        Parameters:
            score (int): Numeric score (0-100)
        Returns:
            str: Letter grade
        """
        if 50 <= score <= 100:
            grade_index = (score // 5) - 10
            return self.letter_grades[grade_index]
        else:
            return "FF"
    
    def calculate_gpa(self, letter_grade):
        """
        Convert letter grade to GPA points
        Parameters:
            letter_grade (str): Letter grade
        Returns:
            float: GPA points
        """
        gpa_mapping = {
            "AA": 4.0,
            "BA": 3.5,
            "BB": 3.0,
            "BC": 2.5,
            "CC": 2.0,
            "CD": 1.5,
            "DD": 1.0,
            "FD": 0.5,
            "FF": 0.0
        }
        
        return gpa_mapping.get(letter_grade, 0.0)
    
    def grade_statistics(self, grades):
        """
        Calculate grade statistics
        Parameters:
            grades (list): List of numeric grades
        Returns:
            dict: Statistics dictionary
        """
        if not grades:
            return {}
        
        stats = {
            "average": sum(grades) / len(grades),
            "highest": max(grades),
            "lowest": min(grades),
            "count": len(grades)
        }
        
        return stats
    
    def batch_grade_conversion(self, scores):
        """
        Convert multiple scores to letter grades
        Parameters:
            scores (list): List of numeric scores
        Returns:
            list: List of (score, letter_grade) tuples
        """
        results = []
        for score in scores:
            if 0 <= score <= 100:
                letter_grade = self.convert_numeric_to_letter_grade(score)
                results.append((score, letter_grade))
            else:
                results.append((score, "Invalid"))
        
        return results
    
    def grade_distribution(self, grades):
        """
        Calculate grade distribution
        Parameters:
            grades (list): List of letter grades
        Returns:
            dict: Grade counts
        """
        distribution = {}
        for grade in grades:
            distribution[grade] = distribution.get(grade, 0) + 1
        
        return distribution

# ===== DEVICE CLASS =====

class Device:
    """
    Device class with various magic methods implemented
    Represents a device with ID, speed, channels, and version
    """
    
    def __init__(self, ID, hız, kanal, versiyon, güç=50):
        """
        Initialize device with parameters
        Parameters:
            ID: Device identifier
            hız: Device speed
            kanal: Device channels
            versiyon: Device version
            güç: Device power (default: 50)
        """
        self.ıd = ID
        self.hız = hız
        self.index = -1
        self.kanal = kanal
        self.versiyon = versiyon
        self.güç = güç
        self.değer = kanal  # Initialize değer for iteration
    
    def __repr__(self):
        """
        Return official string representation of device
        Returns:
            str: Official representation
        """
        return f"Device(ID={self.ıd}, hız={self.hız}, versiyon={self.versiyon})"
    
    def __str__(self):
        """
        Return user-friendly string representation
        Returns:
            str: Device ID as string
        """
        return str(self.ıd)
    
    def __bytes__(self):
        """
        Return bytes representation of device
        Returns:
            bytes: Bytes representation
        """
        return str(self.ıd).encode('utf-8')
    
    def __iter__(self):
        """
        Return iterator object (self)
        Returns:
            Device: Iterator object
        """
        return self
    
    def __next__(self):
        """
        Return next value in iteration
        Returns:
            Next channel value
        Raises:
            StopIteration: When iteration is complete
        """
        self.index += 1
        if self.index >= len(self.değer):
            self.index = 0
            raise StopIteration("Class has arrived at the last argument of iterator")
        return self.değer[self.index]
    
    def __len__(self):
        """
        Return length of device channels
        Returns:
            int: Number of channels
        """
        return len(self.kanal)
    
    def __getitem__(self, key):
        """
        Get item using indexing
        Parameters:
            key: Index key
        Returns:
            Channel value at index
        """
        return self.kanal[key]
    
    def __setitem__(self, key, value):
        """
        Set item using indexing
        Parameters:
            key: Index key
            value: Value to set
        """
        self.kanal[key] = value
    
    def get_device_info(self):
        """
        Get comprehensive device information
        Returns:
            dict: Device information dictionary
        """
        return {
            'ID': self.ıd,
            'hız': self.hız,
            'kanal': self.kanal,
            'versiyon': self.versiyon,
            'güç': self.güç
        }

# ===== DEMONSTRATION FUNCTIONS =====

def demo_web_automation():
    """Demonstrate web automation functionality"""
    print("=== Web Automation Demo ===")
    
    web_auto = WebAutomation("edge")
    web_auto.create_webdriver()
    web_auto.navigate_to_url("https://dashboard.twitch.tv/u/threetmedya/stream-manager")
    web_auto.display_page_info()
    
    print("Web automation started. Press 'q' to close...")
    # Note: In real usage, you might want to add more automation tasks
    
    web_auto.close_browser()

def demo_bluetooth_screen():
    """Demonstrate Bluetooth screen functionality"""
    print("\n=== Bluetooth Screen Demo ===")
    
    bt_manager = BluetoothScreenManager()
    # Note: This requires actual Bluetooth devices to work properly
    print("Bluetooth screen manager initialized.")
    print("Run bt_manager.run_bluetooth_screen_app() to start the application.")

def demo_ocr_processor():
    """Demonstrate OCR functionality"""
    print("\n=== OCR Processor Demo ===")
    
    # Initialize OCR processor
    tesseract_path = "C:/Users/FERHAT KARA/AppData/Local/Programs/Tesseract-OCR"
    ocr = OCRImageProcessor(tesseract_path)
    
    # Example image path (update as needed)
    image_path = 'resim.jpg'
    
    if os.path.exists(image_path):
        print(f"Processing image: {image_path}")
        
        # Extract text using different methods
        text_pil = ocr.extract_text_from_pil_image(image_path)
        text_cv2 = ocr.extract_text_from_opencv_image(image_path)
        text_preprocessed = ocr.extract_text_with_preprocessing(image_path)
        
        print(f"PIL extraction: {repr(text_pil[:100])}...")
        print(f"OpenCV extraction: {repr(text_cv2[:100])}...")
        print(f"Preprocessed extraction: {repr(text_preprocessed[:100])}...")
    else:
        print(f"Image file not found: {image_path}")

def demo_grade_calculator():
    """Demonstrate grade calculator functionality"""
    print("\n=== Grade Calculator Demo ===")
    
    calculator = GradeCalculator()
    
    # Single grade conversion
    score = 85
    letter_grade = calculator.convert_numeric_to_letter_grade(score)
    gpa = calculator.calculate_gpa(letter_grade)
    print(f"Score: {score} -> Grade: {letter_grade} (GPA: {gpa})")
    
    # Batch conversion
    sample_scores = [85, 72, 58, 91, 45, 67, 78, 52, 88, 73]
    batch_results = calculator.batch_grade_conversion(sample_scores)
    
    print("\nBatch conversion results:")
    for score, grade in batch_results:
        print(f"  {score} -> {grade}")
    
    # Statistics
    valid_scores = [score for score, grade in batch_results if grade != "Invalid"]
    stats = calculator.grade_statistics(valid_scores)
    
    print(f"\nStatistics:")
    print(f"  Average: {stats['average']:.2f}")
    print(f"  Highest: {stats['highest']}")
    print(f"  Lowest: {stats['lowest']}")
    print(f"  Count: {stats['count']}")

def demo_device_class():
    """Demonstrate device class functionality"""
    print("\n=== Device Class Demo ===")
    
    # Create device instance
    device = Device(1, 2, kanal=[1, 2, 3, 4, 5], versiyon=2547)
    
    print(f"Device version: {device.versiyon}")
    print(f"Device string: {str(device)}")
    print(f"Device repr: {repr(device)}")
    print(f"Device info: {device.get_device_info()}")
    
    # Demonstrate iteration
    print("\nIterating through channels:")
    for i, channel in enumerate(device):
        print(f"Channel {i}: {channel}")
        if i >= 4:  # Prevent infinite loop for demo
            break

if __name__ == "__main__":
    demo_web_automation()
    demo_bluetooth_screen()
    demo_ocr_processor()
    demo_grade_calculator()
    demo_device_class()
    
    print("\n=== Applications Summary ===")
    print("1. Web Automation: Selenium WebDriver for browser automation")
    print("2. Bluetooth Screen: Bluetooth device discovery and screen display")
    print("3. OCR Processor: Text extraction from images using Tesseract")
    print("4. Grade Calculator: Academic grade management system")
    print("5. Device Class: Custom class with magic methods for device representation")

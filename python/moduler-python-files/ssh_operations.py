# SSH Operations Module - Complete SSH Functionality
# This module provides comprehensive SSH operations including client management and backup systems

import paramiko
import datetime
import os
from typing import Optional, Tuple, List, Dict
from os import mkdir, path, listdir
from datetime import datetime, timedelta, date
from time import sleep
import subprocess
import socket
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException

# ===== SSH CLIENT MANAGEMENT =====

class SSHManager:
    """
    SSH client manager for remote server operations
    """
    
    def __init__(self, host: str, port: int = 22, username: str = "", password: str = ""):
        """
        Initialize SSH manager
        Parameters:
            host (str): SSH server IP address
            port (int): SSH port (default: 22)
            username (str): SSH username
            password (str): SSH password
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.client = None
    
    def connect(self, timeout: float = 0.5) -> bool:
        """
        Connect to SSH server
        Parameters:
            timeout (float): Connection timeout in seconds
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(
                self.host, 
                self.port, 
                self.username, 
                self.password, 
                timeout=timeout
            )
            print(f"Connected to {self.host}:{self.port}")
            return True
        except Exception as e:
            print(f"SSH connection failed: {e}")
            return False
    
    def execute_command(self, command: str) -> Tuple[bool, str, str]:
        """
        Execute command on remote server
        Parameters:
            command (str): Command to execute
        Returns:
            Tuple[bool, str, str]: (success, stdout, stderr)
        """
        if not self.client:
            return False, "", "SSH client not connected"
        
        try:
            stdin, stdout, stderr = self.client.exec_command(command)
            
            # Read output
            stdout_data = stdout.read().decode('utf-8')
            stderr_data = stderr.read().decode('utf-8')
            
            # Check for errors
            if "err=1" in stderr_data:
                return False, stdout_data, stderr_data
            
            return True, stdout_data, stderr_data
            
        except Exception as e:
            return False, "", f"Command execution error: {e}"
    
    def save_command_output(self, command: str, filename: str) -> bool:
        """
        Execute command and save output to file
        Parameters:
            command (str): Command to execute
            filename (str): Output filename
        Returns:
            bool: True if successful, False otherwise
        """
        success, stdout, stderr = self.execute_command(command)
        
        if success:
            try:
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(stdout)
                print(f"Command output saved to {filename}")
                return True
            except Exception as e:
                print(f"Error saving output: {e}")
                return False
        else:
            print(f"Command failed: {stderr}")
            return False
    
    def disconnect(self):
        """
        Disconnect from SSH server
        """
        if self.client:
            self.client.close()
            self.client = None
            print(f"Disconnected from {self.host}")

def quick_ssh_backup(host: str, username: str, password: str, output_file: str = "config_backup.txt"):
    """
    Quick SSH backup function for single device
    Parameters:
        host (str): Device IP address
        username (str): SSH username
        password (str): SSH password
        output_file (str): Output filename
    """
    ssh_manager = SSHManager(host, 22, username, password)
    
    if ssh_manager.connect():
        ssh_manager.save_command_output("show run", output_file)
        ssh_manager.disconnect()
    else:
        print("SSH connection failed")

def test_ssh_connection():
    """
    Test SSH connection with sample credentials
    """
    print("=== SSH Connection Test ===")
    
    # Sample connection details (update as needed)
    host = "10.10.10.250"
    username = "admin"
    password = "1qaZXsw23"
    
    # Create SSH manager and connect
    ssh_manager = SSHManager(host, 22, username, password)
    
    if ssh_manager.connect():
        print("SSH connection successful!")
        
        # Test command execution
        success, stdout, stderr = ssh_manager.execute_command("show version")
        
        if success:
            print("Command executed successfully")
            print(f"Output (first 200 chars): {stdout[:200]}...")
        else:
            print(f"Command failed: {stderr}")
        
        # Test backup functionality
        ssh_manager.save_command_output("show run", "test_config_backup.txt")
        
        ssh_manager.disconnect()
    else:
        print("SSH connection failed")

# ===== SSH BACKUP SYSTEM =====

class SSHBackupSystem:
    """
    Comprehensive SSH backup system for network devices
    """
    
    def __init__(self, base_path: str, backup_frequency: str = "5"):
        """
        Initialize backup system
        Parameters:
            base_path (str): Base directory for backups
            backup_frequency (str): Backup frequency in days
        """
        self.base_path = base_path
        self.backup_frequency = int(backup_frequency)
        self.ssh_client = SSHClient()
        self.ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        
        # Network configuration
        self.ip = '10.10.10.2'
        self.port = 22
        self.username = 'ahan'
        self.password = '1qaZXsw23'
        self.command = "showrun"
        self.subnet_ip = "10.30.30"
        self.port_scan_ip = "10.200.200.2"
        
        # Device tracking
        self.active_ips = []
        self.device_versions = {}
        self.supported_devices = ['access point', 'firewall', 'switch']
    
    def create_backup_directory(self):
        """
        Create backup directory structure
        """
        backup_path = path.join(self.base_path, "allconfig_backup")
        
        if path.isdir(backup_path):
            print("Backup directory already exists")
        else:
            mkdir(backup_path)
            self._create_device_subdirectories(backup_path)
    
    def _create_device_subdirectories(self, backup_path: str):
        """
        Create subdirectories for each device type
        Parameters:
            backup_path (str): Base backup path
        """
        self._discover_device_versions()
        
        for ip, device_type in self.device_versions.items():
            if device_type == "switch":
                device_path = path.join(backup_path, f"{ip}:{self.port}")
                mkdir(device_path)
                
                # Create year subdirectory
                year_path = path.join(device_path, str(datetime.now().year))
                mkdir(year_path)
                
                # Create month subdirectories
                for month in range(datetime.now().month, 13):
                    month_path = path.join(year_path, f"{month}")
                    mkdir(month_path)
    
    def execute_ssh_command(self) -> str:
        """
        Execute SSH command on device
        Returns:
            str: Command output or error message
        """
        try:
            self.ssh_client.connect(self.ip, self.port, self.username, self.password)
            stdin, stdout, stderr = self.ssh_client.exec_command(self.command)
            return stdout.read().decode()
        except AuthenticationException:
            print("Authentication failed")
            return "hata"
        except Exception as e:
            print(f"SSH error: {e}")
            return "hata"
        finally:
            self.ssh_client.close()
    
    def scan_network(self) -> List[str]:
        """
        Scan network for active devices
        Returns:
            List[str]: List of active IP addresses
        """
        active_devices = []
        
        for i in range(1, 255):
            ip = f'{self.subnet_ip}.{i}'
            ping_output = subprocess.Popen(
                ['ping', '-c', '1', '-W', '1', ip], 
                stdout=subprocess.PIPE
            ).communicate()[0]
            
            if b'received' in ping_output:
                active_devices.append(ip)
        
        self.active_ips = active_devices
        return active_devices
    
    def scan_ports(self):
        """
        Scan ports on target IP
        """
        ip = self.port_scan_ip
        
        print(f"Scanning ports on {ip}...")
        for port in range(1, 1025):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                sock.close()
                
                if result == 0:
                    try:
                        service = socket.getservbyport(port)
                    except:
                        service = "Bilinmeyen servis"
                    print(f"\tPort {port}: Açık ({service})")
            except:
                continue
    
    def discover_device_versions(self) -> Dict[str, str]:
        """
        Discover device types and versions
        Returns:
            Dict[str, str]: IP to device type mapping
        """
        self.scan_network()
        
        for ip in self.active_ips:
            self.ip = ip
            self.command = "show version"
            
            if self.execute_ssh_command() == "hata":
                continue
            else:
                output = self.execute_ssh_command()
                for device_type in self.supported_devices:
                    if device_type in output:
                        self.device_versions[ip] = device_type
                        break
        
        return self.device_versions
    
    def perform_backup(self):
        """
        Perform automated backup process
        """
        base_date = datetime.today()
        
        while True:
            self.create_backup_directory()
            
            # Backup each device
            for device_name in listdir(path.join(self.base_path, "allconfig_backup")):
                device_path = path.join(self.base_path, "allconfig_backup", device_name)
                current_time = datetime.today()
                days_passed = (current_time - base_date).days
                
                if days_passed % self.backup_frequency == 0:
                    backup_date = datetime.now()
                    backup_filename = f"{backup_date.day}-{backup_date.month}-{backup_date.year}.txt"
                    backup_path = path.join(device_path, str(backup_date.month), backup_filename)
                    
                    try:
                        with open(backup_path, "w", encoding="utf-8") as backup_file:
                            backup_file.write(self.execute_ssh_command())
                    except Exception as e:
                        print(f"Backup error: {e}")
            
            # Wait for next backup cycle
            sleep(86400)  # 24 hours
    
    def generate_backup_report(self) -> str:
        """
        Generate backup status report
        Returns:
            str: Backup report
        """
        report = []
        report.append("=== SSH Backup System Report ===")
        report.append(f"Backup Frequency: {self.backup_frequency} days")
        report.append(f"Base Path: {self.base_path}")
        report.append(f"Active Devices: {len(self.active_ips)}")
        report.append(f"Discovered Devices: {len(self.device_versions)}")
        
        report.append("\nActive IP Addresses:")
        for ip in self.active_ips:
            report.append(f"  - {ip}")
        
        report.append("\nDevice Types:")
        for ip, device_type in self.device_versions.items():
            report.append(f"  - {ip}: {device_type}")
        
        return "\n".join(report)

# ===== UTILITY FUNCTIONS =====

def batch_ssh_operations():
    """
    Demonstrate batch SSH operations
    """
    print("\n=== Batch SSH Operations Demo ===")
    
    # List of devices to connect to
    devices = [
        {"host": "10.10.10.1", "username": "admin", "password": "password1"},
        {"host": "10.10.10.2", "username": "admin", "password": "password2"},
        {"host": "10.10.10.3", "username": "admin", "password": "password3"}
    ]
    
    commands = ["show version", "show interfaces", "show running-config"]
    
    for device in devices:
        print(f"\nConnecting to {device['host']}...")
        ssh_manager = SSHManager(
            device['host'], 
            22, 
            device['username'], 
            device['password']
        )
        
        if ssh_manager.connect():
            for command in commands:
                filename = f"{device['host']}_{command.replace(' ', '_')}.txt"
                ssh_manager.save_command_output(command, filename)
            
            ssh_manager.disconnect()
        else:
            print(f"Failed to connect to {device['host']}")

# ===== DEMONSTRATION FUNCTIONS =====

def demo_ssh_client():
    """Demonstrate SSH client functionality"""
    print("=== SSH Client Demo ===")
    test_ssh_connection()
    
    # Quick backup example
    print("\n=== Quick Backup Example ===")
    quick_ssh_backup("10.10.10.250", "admin", "1qaZXsw23", "allconfig_backup.txt")
    
    # Batch operations demo
    batch_ssh_operations()

def demo_ssh_backup_system():
    """Demonstrate SSH backup system functionality"""
    print("\n=== SSH Backup System Demo ===")
    
    # Initialize backup system
    backup_system = SSHBackupSystem(
        base_path="C:\\Users\\FERHAT KARA\\OneDrive\\Masaüstü\\all config",
        backup_frequency="5"
    )
    
    # Scan network
    print("Scanning network for active devices...")
    active_devices = backup_system.scan_network()
    print(f"Found {len(active_devices)} active devices")
    
    # Discover device types
    print("Discovering device types...")
    device_versions = backup_system.discover_device_versions()
    print(f"Discovered {len(device_versions)} devices")
    
    # Generate report
    print("\nGenerating backup report...")
    report = backup_system.generate_backup_report()
    print(report)
    
    # Port scanning demo
    print("\nStarting port scan...")
    backup_system.scan_ports()
    
    # Note: Uncomment the following line to start actual backup process
    # backup_system.perform_backup()

if __name__ == "__main__":
    demo_ssh_client()
    demo_ssh_backup_system()

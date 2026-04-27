# Email Services Module - Complete Email Functionality
# This module provides comprehensive email services including Gmail API and SMTP

import base64
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import yagmail
import google 
from google import oauth2,credentials,Credentials
from google import _auth_oauthlib,flow,InstalledAppFlow
from google import apiclient,discovery,build
from google import apiclient,errors,HttpError

# ===== GMAIL API FUNCTIONS =====

# Gmail API permissions for sending emails
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def create_gmail_message(to, subject, message_text, file_path):
    """
    Create an email message with text and image attachment using Gmail API
    Parameters:
        to (str): Recipient email address
        subject (str): Email subject
        message_text (str): Email body text
        file_path (str): Path to image file to attach
    Returns:
        dict: Raw message dictionary for Gmail API
    """
    message = MIMEMultipart()
    message['to'] = to
    message['subject'] = subject

    # Add email body text
    text = MIMEText(message_text)
    message.attach(text)

    # Add image attachment
    with open(file_path, 'rb') as f:
        img_data = f.read()
    image = MIMEImage(img_data, name='image.jpg')
    message.attach(image)

    # Convert message to MIME format for Gmail API
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message}

def send_gmail_message(service, user_id, message):
    """
    Send email message using Gmail API
    Parameters:
        service: Gmail API service object
        user_id (str): User ID (typically 'me')
        message (dict): Message dictionary
    Returns:
        dict: Sent message information or None if error
    """
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print(f'Message Id: {message["id"]}')
    except HttpError as error:
        print(f'An error occurred: {error}')
        message = None
    return message

def setup_gmail_service():
    """
    Setup Gmail API service
    Returns:
        Gmail API service object
    """
    # Authentication flow for Gmail API
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', scopes=SCOPES)
    credentials = flow.run_local_server(port=0)

    # Create Gmail API service
    service = build('gmail', 'v1', credentials=credentials)
    return service

def send_gmail_email(to, subject, body, attachment_path=None):
    """
    Send email using Gmail API
    Parameters:
        to (str): Recipient email
        subject (str): Email subject
        body (str): Email body
        attachment_path (str): Optional attachment path
    Returns:
        bool: True if successful
    """
    try:
        service = setup_gmail_service()
        
        if attachment_path:
            message = create_gmail_message(to, subject, body, attachment_path)
        else:
            message = create_gmail_message(to, subject, body, "dummy.jpg")
        
        send_gmail_message(service, 'me', message)
        print("Gmail sent successfully")
        return True
    except Exception as e:
        print(f"Gmail error: {e}")
        return False

# ===== SMTP EMAIL CLIENT =====

class EmailClient:
    """
    Email client class supporting multiple SMTP providers
    """
    
    def __init__(self, smtp_server, smtp_port, username, password):
        """
        Initialize email client with SMTP credentials
        Parameters:
            smtp_server (str): SMTP server address
            smtp_port (int): SMTP port number
            username (str): Email username
            password (str): Email password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
    
    def send_email_smtplib(self, to_address, subject, body):
        """
        Send email using smtplib
        Parameters:
            to_address (str): Recipient email address
            subject (str): Email subject
            body (str): Email body
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Create MIMEText message
            message = MIMEText(body)
            message['Subject'] = subject
            message['From'] = self.username
            message['To'] = to_address
            
            print(f"Connecting to SMTP server: {self.smtp_server}")
            
            # Connect to SMTP server
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.ehlo()
            
            # Start TLS encryption
            server.starttls()
            print("Login successful")
            
            # Login to email account
            server.login(self.username, self.password)
            
            # Send email
            server.sendmail(self.username, to_address, message.as_string())
            server.quit()
            
            print("Email sent successfully using smtplib")
            return True
            
        except Exception as e:
            print(f"Error sending email with smtplib: {e}")
            return False
    
    def send_email_yagmail(self, to_address, subject, body):
        """
        Send email using yagmail library
        Parameters:
            to_address (str): Recipient email address
            subject (str): Email subject
            body (str): Email body
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Create yagmail SMTP instance
            yag = yagmail.SMTP(
                user=self.username, 
                password=self.password, 
                host=self.smtp_server, 
                port=self.smtp_port
            )
            
            # Send email
            yag.send(to=to_address, subject=subject, contents=body)
            
            print("Email sent successfully using yagmail")
            return True
            
        except Exception as e:
            print(f"Error sending email with yagmail: {e}")
            return False

def create_yandex_client():
    """
    Create Yandex email client
    Returns:
        EmailClient: Configured Yandex email client
    """
    return EmailClient(
        smtp_server='smtp.yandex.com',
        smtp_port=465,
        username='no-reply@prosight.com.tr',
        password='1qaZXsw23'
    )

def create_gmail_smtp_client():
    """
    Create Gmail SMTP email client
    Returns:
        EmailClient: Configured Gmail email client
    """
    return EmailClient(
        smtp_server='smtp.gmail.com',
        smtp_port=587,
        username='7fkarae@gmail.com',
        password='123FERHAT'
    )

# ===== EMAIL UTILITY FUNCTIONS =====

def send_bulk_email(email_list, subject, body, client):
    """
    Send email to multiple recipients
    Parameters:
        email_list (list): List of recipient email addresses
        subject (str): Email subject
        body (str): Email body
        client (EmailClient): Email client instance
    """
    success_count = 0
    failure_count = 0
    
    for email in email_list:
        if client.send_email_smtplib(email, subject, body):
            success_count += 1
            print(f"Email sent to: {email}")
        else:
            failure_count += 1
            print(f"Failed to send to: {email}")
    
    print(f"\nBulk email summary:")
    print(f"Successful: {success_count}")
    print(f"Failed: {failure_count}")

def create_html_email(to_address, subject, html_body, smtp_client):
    """
    Create and send HTML email
    Parameters:
        to_address (str): Recipient email address
        subject (str): Email subject
        html_body (str): HTML email body
        smtp_client (EmailClient): SMTP client instance
    """
    try:
        # Create MIMEMultipart message
        message = MIMEMultipart("alternative")
        message['Subject'] = subject
        message['From'] = smtp_client.username
        message['To'] = to_address
        
        # Add HTML body
        html_part = MIMEText(html_body, "html")
        message.attach(html_part)
        
        # Send using SMTP
        server = smtplib.SMTP(smtp_client.smtp_server, smtp_client.smtp_port)
        server.ehlo()
        server.starttls()
        server.login(smtp_client.username, smtp_client.password)
        server.sendmail(smtp_client.username, to_address, message.as_string())
        server.quit()
        
        print("HTML email sent successfully")
        
    except Exception as e:
        print(f"Error sending HTML email: {e}")

# ===== DEMONSTRATION FUNCTIONS =====

def demo_gmail_api():
    """Demonstrate Gmail API functionality"""
    print("=== Gmail API Demo ===")
    
    # Example Gmail API usage
    to = "alici@example.com"
    subject = "Test Gmail API"
    body = "Bu bir Gmail API test e-postasıdır."
    
    if send_gmail_email(to, subject, body):
        print("Gmail API email sent successfully")
    else:
        print("Gmail API email failed")

def demo_smtp_clients():
    """Demonstrate SMTP client functionality"""
    print("\n=== SMTP Clients Demo ===")
    
    # Test email details
    to_address = '7fkara@gmail.com'
    subject = 'Test Email'
    body = 'Bu bir test e-postasıdır.'
    
    # Test with Yandex using smtplib
    print("\n1. Yandex - smtplib:")
    yandex_client = create_yandex_client()
    yandex_client.send_email_smtplib(to_address, subject, body)
    
    # Test with Yandex using yagmail
    print("\n2. Yandex - yagmail:")
    yandex_client.send_email_yagmail(to_address, subject, body)
    
    # Test with Gmail using smtplib
    print("\n3. Gmail - smtplib:")
    gmail_client = create_gmail_smtp_client()
    gmail_client.send_email_smtplib(to_address, subject, body)

def demo_html_email():
    """Demonstrate HTML email functionality"""
    print("\n=== HTML Email Demo ===")
    
    html_content = """
    <html>
        <body>
            <h1>Test HTML Email</h1>
            <p>This is a <strong>test</strong> HTML email with <em>formatting</em>.</p>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </body>
    </html>
    """
    
    yandex_client = create_yandex_client()
    create_html_email('7fkara@gmail.com', 'HTML Test Email', html_content, yandex_client)

def demo_bulk_email():
    """Demonstrate bulk email functionality"""
    print("\n=== Bulk Email Demo ===")
    
    recipient_list = ['recipient1@example.com', 'recipient2@example.com']
    yandex_client = create_yandex_client()
    send_bulk_email(recipient_list, 'Bulk Test', 'This is a bulk test email', yandex_client)

if __name__ == "__main__":
    demo_gmail_api()
    demo_smtp_clients()
    demo_html_email()
    demo_bulk_email()

#!/usr/bin/env python3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def create_phishing_email(target_email, phishing_url):
    """
    Create a phishing email that mimics a legitimate bank notification.
    
    Parameters:
        target_email: Email address of the target
        phishing_url: URL to the phishing page (e.g., http://127.0.0.1:5000)
    """
    
    # Email configuration (for demonstration - use local SMTP or configure properly)
    sender_email = "noreply@yourbank.com"  # Fake sender
    subject = "Action Required: Verify Your Payment Information"
    
    # Create message
    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = target_email
    message["Subject"] = subject
    
    # HTML email body (designed to look legitimate)
    html_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
            }}
            .header {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 20px;
                text-align: center;
                border-radius: 5px 5px 0 0;
            }}
            .content {{
                background: #f9f9f9;
                padding: 30px;
                border: 1px solid #ddd;
            }}
            .button {{
                display: inline-block;
                padding: 12px 30px;
                background: #667eea;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                margin: 20px 0;
            }}
            .footer {{
                background: #333;
                color: white;
                padding: 15px;
                text-align: center;
                font-size: 12px;
                border-radius: 0 0 5px 5px;
            }}
            .warning {{
                background: #fff3cd;
                border-left: 4px solid #ffc107;
                padding: 12px;
                margin: 20px 0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🔒 YourBank</h1>
                <p>Security Alert</p>
            </div>
            <div class="content">
                <h2>Action Required: Verify Your Payment Information</h2>
                <p>Dear Valued Customer,</p>
                <p>We have detected unusual activity on your account. To ensure the security of your account and prevent unauthorized access, we require you to verify your payment information immediately.</p>
                
                <div class="warning">
                    <strong>⚠️ Important:</strong> Failure to verify within 24 hours may result in temporary account suspension.
                </div>
                
                <p>Please click the button below to verify your information:</p>
                <a href="{phishing_url}" class="button">Verify Payment Information</a>
                
                <p>If the button does not work, copy and paste this link into your browser:</p>
                <p style="font-size: 12px; color: #666; word-break: break-all;">{phishing_url}</p>
                
                <p style="margin-top: 30px;">Thank you for your prompt attention to this matter.</p>
                <p>Best regards,<br>YourBank Security Team</p>
            </div>
            <div class="footer">
                <p>© 2025 YourBank. All rights reserved.</p>
                <p>This is an automated message. Please do not reply to this email.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    # Plain text version
    text_body = f"""
    YourBank Security Alert
    
    Action Required: Verify Your Payment Information
    
    Dear Valued Customer,
    
    We have detected unusual activity on your account. To ensure the security of your account, we require you to verify your payment information immediately.
    
    Please visit: {phishing_url}
    
    Thank you,
    YourBank Security Team
    """
    
    # Attach both versions
    text_part = MIMEText(text_body, "plain")
    html_part = MIMEText(html_body, "html")
    
    message.attach(text_part)
    message.attach(html_part)
    
    return message

def send_email_demo(message, smtp_server="localhost", smtp_port=1025):
    """
    Demonstrate sending the email.
    
    For local testing, you can use a local SMTP server like:
    - Python's built-in: python -m smtplib -n -c DebuggingServer localhost:1025
    - Or configure with real SMTP settings (Gmail, etc.)
    
    WARNING: Sending phishing emails is illegal. This is for educational demonstration only.
    """
    print("="*60)
    print("PHISHING EMAIL SIMULATION (Educational Purpose Only)")
    print("="*60)
    print("⚠️  WARNING: This is for educational use only!")
    print("   Sending phishing emails is illegal. Do not use for malicious purposes.")
    print("="*60)
    print("\nEmail Details:")
    print(f"From: {message['From']}")
    print(f"To: {message['To']}")
    print(f"Subject: {message['Subject']}")
    print(f"\nSMTP Server: {smtp_server}:{smtp_port}")
    print("\nTo actually send (for testing only):")
    print("1. Start a local SMTP server: python -m smtplib -n -c DebuggingServer localhost:1025")
    print("2. Uncomment the code below and run this script")
    print("="*60)
    
    # Uncomment below to actually send (only for local testing with debugging server)
    """
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.send_message(message)
            print(f"\n✓ Email sent successfully to {message['To']}")
    except Exception as e:
        print(f"\n✗ Error sending email: {e}")
        print("Make sure you have a local SMTP server running.")
    """

if __name__ == '__main__':
    # Example usage
    target = "victim@example.com"  # Replace with test email
    phishing_url = "http://127.0.0.1:5000"  # Your phishing server URL
    
    email_message = create_phishing_email(target, phishing_url)
    
    # Print email content for review
    print("\nEmail HTML Content Preview:")
    print("-" * 60)
    print(email_message.get_payload(1).get_payload())
    print("-" * 60)
    
    # Demonstrate sending (commented out for safety)
    send_email_demo(email_message)
    
    print("\n" + "="*60)
    print("EDUCATIONAL NOTES:")
    print("="*60)
    print("1. Real phishing emails often use:")
    print("   - Urgent language and deadlines")
    print("   - Legitimate-looking branding and logos")
    print("   - Spoofed sender addresses")
    print("   - Links that look legitimate but redirect to malicious sites")
    print("\n2. Red flags to look for:")
    print("   - Suspicious sender addresses")
    print("   - Urgent requests for personal information")
    print("   - Links that don't match the claimed organization")
    print("   - Poor grammar or spelling (though modern attacks are sophisticated)")
    print("   - Requests for sensitive data via email")
    print("="*60)


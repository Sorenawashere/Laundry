import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_name, sender_email, message_body):
    """
    Sends a contact form message using environment-based email credentials.
    
    Environment Variables required:
    - SMTP_SERVER (e.g. smtp.gmail.com)
    - SMTP_PORT (e.g. 465 for SSL)
    - EMAIL_USERNAME
    - EMAIL_PASSWORD
    - CONTACT_RECEIVER (destination email)
    """
    smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", "465"))
    smtp_user = os.getenv("EMAIL_USERNAME")
    smtp_password = os.getenv("EMAIL_PASSWORD")
    receiver_email = os.getenv("CONTACT_RECEIVER")

    if not all([smtp_user, smtp_password, receiver_email]):
        raise EnvironmentError(
            "Missing email configuration. Please set SMTP and email environment variables."
        )

    subject = f"New Contact Form Submission from {sender_name}"

    # Build email
    msg = MIMEMultipart()
    msg["From"] = f"{sender_name} <{sender_email}>"
    msg["To"] = receiver_email
    msg["Subject"] = subject

    text = f"""
    You have a new message from your website contact form.

    Name: {sender_name}
    Email: {sender_email}

    Message:
    {message_body}
    """
    msg.attach(MIMEText(text, "plain"))

    # Send via secure connection
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(smtp_user, smtp_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return True
    except Exception as e:
        print(f"Email sending failed: {e}")
        return False
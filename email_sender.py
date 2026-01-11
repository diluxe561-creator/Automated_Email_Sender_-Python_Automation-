import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Load secrets from a .env file (not uploaded to GitHub)
load_dotenv()

def send_automated_email(recipient, subject, body):
    email_address = os.getenv("EMAIL_USER")
    email_password = os.getenv("EMAIL_PASS")

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = email_address
    msg["To"] = recipient
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(email_address, email_password)
            server.send_message(msg)
        print(f"Email sent to {recipient}!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    send_automated_email("client@example.com", "Project Update", "Your report is ready.")


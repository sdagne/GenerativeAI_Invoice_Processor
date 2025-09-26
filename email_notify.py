
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load .env file (only in development)
load_dotenv()


def send_email(sender_email, recipient_email, subject, body):
    try:
        # ✅ Get password securely from environment
        password = os.getenv("GMAIL_APP_PASSWORD")
        if not password:
            print("❌ GMAIL_APP_PASSWORD not set in environment")
            return False

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"📧 Email error: {e}")
        return False





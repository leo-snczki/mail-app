from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv("SECRET_KEY")

def main():
    print("hello world!")

if __name__ == "__main__":
    main()
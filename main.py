import sys
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
SENHA = os.getenv("SECRET_KEY")

def enviar_email(email, assunto, mensagem):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_REMETENTE
        msg['To'] = email
        msg['Subject'] = assunto
        msg.attach(MIMEText(mensagem, 'plain'))
        with SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_REMETENTE, SENHA)
            smtp.send_message(msg)
            return True
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        return False

def main():
    try:
        destinatario = sys.argv[1]
        assunto = sys.argv[2]
        mensagem = sys.argv[3]
        if enviar_email(destinatario, assunto, mensagem):
            print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()

import sys
import json
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
PASSWORD = os.getenv("SECRET_KEY")

def enviar_email(email, assunto, mensagem):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = email
    msg['Subject'] = assunto
    msg.attach(MIMEText(mensagem, 'plain'))

    with SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_REMETENTE, PASSWORD)
        smtp.send_message(msg)

def main():
    dados_json = sys.argv[1]
    dados = json.loads(dados_json)

    enviar_email(dados['email'], dados['assunto'], dados['mensagem'])

if __name__ == "__main__":
    main()

import smtplib
from email.mime.text import MIMEText

# ----- Configurações -----
remetente = "remetente@gmail.com"
senha = "abcdefghijklmnop" # Chave de app
destinatario = "destinatario@gmail.com"

# Corpo do email
mensagem = MIMEText("Olá, Seja bem-vindo!")
mensagem["Subject"] = "Teste de e-mail com Python"
mensagem["From"] = remetente
mensagem["To"] = destinatario

# Envio

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
        servidor.login(remetente, senha)
        servidor.send_message(mensagem)
    print("✅ E-mail enviado com sucesso!")
except:
    print("Erro ao enviar o email")
finally:
    print("Obrigado por usar nosso serviço")
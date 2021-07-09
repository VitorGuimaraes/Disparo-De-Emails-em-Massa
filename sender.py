import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 465  # For SSL
smtp_server = "smtp.gmail.com"

# Read email from text file 
read_email = open('password.txt')
sender_email = read_email.readline().strip()

# Read email's password from text file 
read_password = open('your_password.txt')
password = read_password.readline().strip()

# Read file with names and emails  
read_file = open('mailist.txt')
receivers = read_file.readlines()

# Create a secure SSL context
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)

    for receiver in receivers:

        msg = MIMEMultipart()

        strip_receiver = receiver.strip() # Remove blank spaces from start and end string
        name, email = strip_receiver.split(';') # Splits name and email by ;

        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = "Email automático"

        body = '''Olá {}! Este email foi enviado automaticamente. 
                Legal né? Dá pra fazer coisas incríveis com Python! 
                Dá uma olhada no meu GitHub e me segue no LinkedIn :D
                https://github.com/VitorGuimaraes
                https://www.linkedin.com/in/vitorguimaraesteixeira/'''.format(name)

        msg.attach(MIMEText(body, 'plain'))
        
        server.send_message(msg)
        del msg

        print('Email enviado para {}'.format(name))
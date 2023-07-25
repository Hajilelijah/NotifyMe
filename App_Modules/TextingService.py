import smtplib
import ssl
from email.message import EmailMessage
import json


class Config:
    def __init__(self):
        with open("App_Configs\\TextingService.config.json", 'r') as file:
            config = json.load(file)

        self.EmailConfig = config["EmailConfig"]
        self.Server = self.EmailConfig["Server"]
        self.Port = self.EmailConfig["Port"]
        self.Username = self.EmailConfig["Username"]
        self.Password = self.EmailConfig["Password"]
        self.Sender = self.EmailConfig["Sender"]
        self.Receiver = self.EmailConfig["Receiver"]
        self.Message = config["Message"]
        self.Subject = self.Message["Subject"]
        self.Header = self.Message["Header"]
        self.Footer = self.Message["Footer"]


config = Config()


class message_formater:
    # def __init__(self, body):
    #     self.body = body
    def message(body):
        content = config.Header + body + config.Footer
        return content


class Text:
    def message(body):
        em = EmailMessage()
        em['From'] = config.Sender
        em['To'] = config.Receiver
        em['Subject'] = config.Subject
        em.set_content(
            message_formater.message(body))

        # Add SSL (layer of security)
        context = ssl.create_default_context()

        # Log in and send the email
        with smtplib.SMTP_SSL(config.Server, config.Port, context=context) as smtp:
            smtp.login(config.Username, config.Password)
            smtp.sendmail(config.Sender, config.Receiver, em.as_string())

from datetime import datetime


class GenerateEmailAndLogin:

    @staticmethod
    def generate_email():
        now = datetime.now()
        timestamp = now.strftime("%y%m%d%H%M%S")
        return f"shivam+{timestamp}@go4worldbusiness.com"

    @staticmethod
    def generate_login():
        now = datetime.now()
        timestamp = now.strftime("%y%m%d%H%M%S")
        return f"Shivam{timestamp}"

from user_manager import UserManager

class AuthUser:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.email = None
        self.user_manager = UserManager()

    def register(self):
        self.first_name = input("First name: ")
        self.last_name = input("Last name: ")

        while True:
            self.email = input("Email: ")
            verification_result = self.verify_email()

            if verification_result:
                print("This email already exists, please try another one")
            else:
                email_verified = input("Verify email again: ")
                if email_verified != self.email:
                    print("The email has to be the same")
                else:
                    print("Register Success")
                    return self.first_name, self.last_name, self.email

    def verify_email(self):
        registered_emails = []
        users_data = self.user_manager.get_user_data()

        for user in users_data:
            registered_emails.append(user['email'])

        return self.email in registered_emails
    
from user_manager import UserManager

def register():
    first_name = input("First name: ").title()
    last_name = input("Last name: ").title()

    while True:
        email_to_verify = input("Email: ")
        verification_result = verify_email(email_to_verify)

        if verification_result is True:
            print("This email already exists, please try another one")
        else:
            email_verified = input("Verify email again: ")
            if email_verified != email_to_verify:
                print("The email has to be the same")
            else:
                print("Register Success")
                return first_name, last_name, email_verified


def verify_email(email_to_verify):
    registered_emails = []
    users = UserManager()
    users_data = users.get_user_data()
    for user in users_data:
        registered_emails.append(user['email'])

    if email_to_verify in registered_emails:
        return True
    else:
        return False

user_name, user_lastname, email = register()
users = UserManager()
users.add_new_user(user_name, user_lastname, email)



    

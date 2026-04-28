from password_manager import PasswordManager

def main():
    password_manager = PasswordManager()
    answer = ''
    while answer != '0':
        print("Welcome in Password Checker")
        print('-'*25)
        password = input("Type your password > ")

        password_manager.setPassword(password)
        password_manager.checkPasswordStrength()

if __name__ == "__main__":
    main()




# Bibliography
# Micorosoft: Password policy recommendations for Microsoft 365 passwords (https://learn.microsoft.com/en-us/microsoft-365/admin/misc/password-policy-recommendations?view=o365-worldwide)
# CISA: Require Strong Passwords (https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/require-strong-passwords)
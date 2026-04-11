
import password_checker

"""
    Password Manager
"""
class PasswordManager():
        
    def __init__(self) -> None:
        self.input_password = "Il#ov@ey9Ou"
        self.password_checker = password_checker.PasswordChecker(self.input_password)

    def getPassword(self) -> str:
        return self.input_password
    
    def setPassword(self, given_password) -> str:
        self.input_password = given_password
        return "OK"

    def inputPassword(self) -> str:
        input_password = input("Inter your password > ")
        self.setPassword(input_password)

    def __str__(self) -> str:
        return "A strong password should follow the "
    

def main():
    password_manager = PasswordManager()
    print("Welcome in Password Checker")
    # password_manager.inputPassword() TODO remove comment

    password_manager.password_checker.isPasswordStrong()

if __name__ == "__main__":
    main()

# Bibliography
# Micorosoft: Password policy recommendations for Microsoft 365 passwords (https://learn.microsoft.com/en-us/microsoft-365/admin/misc/password-policy-recommendations?view=o365-worldwide)
# CISA: Require Strong Passwords (https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/require-strong-passwords)

import password_checker

"""
    Password Manager
"""
class PasswordManager():
        
    def __init__(self) -> None:
        self.input_password = ""

    def getInputPassword(self) -> str:
        return self.input_password
    
    def setIputPassword(self, given_password) -> str:
        self.input_password = given_password
        return "OK"

    def inputPassowrd(self) -> str:
        given_password = input("Inter your password > ")
        
        
        


    def __str__(self) -> str:
        return "A strong password should follow the "
    


# Micorosoft: Password policy recommendations for Microsoft 365 passwords (https://learn.microsoft.com/en-us/microsoft-365/admin/misc/password-policy-recommendations?view=o365-worldwide)
# CISA: Require Strong Passwords (https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/require-strong-passwords)
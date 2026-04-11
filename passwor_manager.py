
"""
    Password Manager
"""
class PasswordManager():

    """
        Password Checker
    """
    class PasswordChecker():
        def __init__(self) -> None:
            self.min_length = 8                     # Password's minimum length is 8, however for a strong password are reccomended at least 14 characters
            self.valid_chars = ['!$%&()?*_@#-']
            self.banned_passwords = [                # Can be a txt list
                                        "abcdefgh",
                                        "password",
                                        "monkey12",
                                        "12345678", 
                                        "87654321",
                                        "iloveyou"
                                    ]
            
        def isMinimumLength(self, password) -> bool:
            pass

        def hasInvalidChars(self) -> bool:
            pass

        def isBanned(self) -> bool:
            pass

        def hasUppercaseLetter(self) -> bool:
            pass

        def hasLowercaseLetter(self) -> bool:
            pass

        def hasNumbers(self) -> bool:
            pass

        def hasSpecialChars(self) -> bool:
            pass

        def isPasswordSecure(self) -> bool:
            pass

        
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
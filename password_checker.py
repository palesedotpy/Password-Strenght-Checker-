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
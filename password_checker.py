import re

class PasswordChecker():
    def __init__(self, given_password) -> None:
        self.min_length = 8                     # Password's minimum length is 8, however for a strong password are reccomended at least 14 characters
        self.valid_chars = '!$%&()?*_@#-'
        self.banned_passwords = [                # Can be a txt list
                                    "abcdefgh",
                                    "password",
                                    "monkey12",
                                    "12345678", 
                                    "87654321",
                                    "iloveyou"
                                ]
        self.given_password = given_password
        print(self.given_password)
        
    def isMinimumLength(self) -> bool:
        return len(self.given_password) >= self.min_length

    def hasNonAcceptedChars(self) -> bool:
        valid_chars_pattern = r"[^a-zA-Z0-9" + self.valid_chars + "]"
        return bool(re.findall(valid_chars_pattern, self.given_password))

    def isBanned(self) -> bool:
        if self.given_password.lower() in self.banned_passwords:
            return True
        return False

    def findChars(self, charsToFind: str) -> bool:
        return bool(re.search(charsToFind, self.given_password))

    def hasRequiredChars(self) -> bool:
        if self.findChars(r"[a-zA-Z0-9]"):
            valid_chars_pattern = r"[!\$%&\(\)\?\*\-_@#']"
            if self.findChars(valid_chars_pattern):
                return True
        return False

    def isPasswordStrong(self) -> bool:     
        if not self.isMinimumLength():
            return False
        if not self.isBanned():
            return False
        if self.hasRequiredChars():
            return False
        if not self.hasNonAcceptedChars():
            return False
        
        return True

        
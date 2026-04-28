from password_checker import PasswordChecker

class PasswordManager():
        
    def __init__(self) -> None:
        self.input_password = None
        self.password_checker = None

    def getPassword(self) -> str:
        return self.input_password
    
    def setPassword(self, given_password) -> str:
        if  type(given_password) != str:
            raise TypeError("Password have to be a string")
        self.input_password = given_password
        self.password_checker = PasswordChecker(self.input_password)

    def checkPasswordStrength(self: str) -> str | None:
        if self.getPassword() == None:
            raise Exception("Password is not set -> setPassword(your_password)")
        
        if self.password_checker.isPasswordStrong():
            print("Your password is strong")
        else:
            print("Your password is weak")
        

    def __str__(self) -> str:
        return "A strong password should:\n" \
                "\t- have a length greater than 8 characters\n" \
                "\t- not be in password lists\n" \
                "\t- "
    

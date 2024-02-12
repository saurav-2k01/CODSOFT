import random

class PasswordGenetator:
    def __init__(self, length:int = 8, complexity: str = "medium"):
        self.length = length
        self.complexity = complexity
        self.characters = {
            "uppercase alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "lowercase alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower(),
            "number": "0123456789",
            "special character": "!@#$%^&*()_-+?"
        }

    def check_length(self):
        if self.length < 8:
            print("The password length must be greater than or equal to 8.")
            return False
        else:
            return True

    def check_complexity(self):
        if self.complexity.lower() == "easy":
            self.string = self.characters.get("uppercase alphabet") + self.characters.get("lowercase alphabet")
            return True
        elif self.complexity.lower() == "medium":
            self.string = self.characters.get("uppercase alphabet") + self.characters.get("lowercase alphabet") + self.characters.get("number")
            return True
        elif self.complexity.lower() == "hard":
            self.string = self.characters.get("uppercase alphabet") + self.characters.get("lowercase alphabet") + self.characters.get("number") + self.characters.get("special character")
            return True
        else:
            print("Given complexity is not valid.\nValid complexities are the following:\n1. Easy\n2. Medium\n3. Hard")
            self.complexity = None
            return False

    def generate_pass(self):
        password = ""
        if self.check_length() and self.check_complexity():
            for i in range(self.length):
                password += random.choice(self.string)
            return password



if __name__ == "__main__":
    flag = True
    while flag:
        choice = input("To generate password press 'Enter' and to quit enter 'q' ==>> ")
        if choice.lower() == "q":
            print("Thank you for using password generator.")
            flag = False
        else:
            length = int(input("Length ==>> "))
            complexity = input("Complexity ==>> ")
            pg = PasswordGenetator(length, complexity)
            print("Password: ", pg.generate_pass())
            print("Complexity: ", pg.complexity)


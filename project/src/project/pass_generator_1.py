import string
import random


class PassGen:
    def __init__(self):
        self.LINE_CLEAN = '\x1b[2K'
        self.LINE_UP = '\033[1A'
        # self.pass_generator(20)
    def program_loop(self):
        while True:
            self.print_welcome_msg()
            choice = input("Enter your choice: ")
            print(choice)
            if choice == "q":
                break
            try:
                choice = int(choice)
            except:
                print("Please enter a number")
            self.go_back(11)

            if choice == 1:
                self.show_password()

            elif choice == 2:
                length, used = self.get_numer("Enter the password length: ", clear=False)
                self.show_password(length, used)

            elif choice == 3:
                number, used1 = self.get_numer("Enter the number of password you want to generate: ", clear=False)
                length, used2 = self.get_numer("Enter the password length: ", clear=False)
                self.generate_multiple_password(number, length, used1+used2)

    def get_numer(self, msg, clear=True):
        lines = 0
        while True:
            value = input(msg)
            lines += 1
            try:
                value = int(value)
            except:
                print("vai vul hoise abr den")
                lines += 1
                continue
            if value <= 0:
                print("Please thik thak number enter koorr")
                lines += 1
                continue

            if clear:
                self.go_back(lines)
            return value, lines

    def generate_multiple_password(self,number=1, length=8, used_lines=0):
        print()

        for i in range(number):

            print(f"Password {i+1}: {self.pass_generator(length)}")
        print("-------------------------------------------")

        print()

        print("Press any key to continue...")
        input()

        self.go_back(number+5+used_lines)

    def show_password(self, length=8, used_lines=0):
        print()

        print(f"Your password is: {self.pass_generator(length)}")
        print("-------------------------------------------")

        print()

        print("Press any key to continue...")
        input()

        self.go_back(6+used_lines)


    def go_back(self, lines=1):
        for i in range(lines):
            print(self.LINE_UP, end=self.LINE_CLEAN)


    def print_welcome_msg(self):

        print()
        print("Hello USER, How May I Help You Today?")
        print("--------------------------------------")

        print()

        print("1. Generate a password for me")
        print("2. Generate a password of a given length")
        print("3. Generate a multiple password")
        print()

        print("------------------------------------------")

    def pass_generator(self, length=8):
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        digit = string.digits
        symbol = "!@#$%^&*"

        up_pass = random.choice(upper)
        low_count = length  - 3
        low_pass = "".join(random.choices(lower, k=low_count))
        s_pass = random.choice(symbol)
        d_pass = random.choice(digit)

        password = up_pass + low_pass + s_pass + d_pass
        return password


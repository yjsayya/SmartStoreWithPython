from Member.LoginMain import Login
from Member.SignUpMain import SignUp

login = Login()
signUp = SignUp()

class StartMenu:

    def showStartMenu(self):
        """시작 메뉴 보여주기"""
        power = True
        while power:
            print('=' * 40)
            print("|%-38s|" % ' << Start Page >>')
            print("-" * 40)
            print("|%-38s|" % ' 1. Login')
            print("|%-38s|" % ' 2. SignUp')
            print("|%-38s|" % ' 3. Quit')
            print("=" * 40)
            index_ = input("Choose One: ")
            print(" ")
            print(" ")

            try:
                index = int(index_)
            except ValueError:
                index = 4

            if index == 1:
                login.inputLogin()
            elif index == 2:
                signUp.signUp()
            elif index == 3:
                power = False
            else:
                print(">> Invalid Input. Please try again <<")
                print(" ")
                print(" ")
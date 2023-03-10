from Member.memberDTO import MemberDTO
from function.mainMenu import MainMenu

memberDTO = MemberDTO()
mm = MainMenu()

class Login:

    @classmethod
    def inputLogin(cls):
        """1. 로그인을 위한 ID, PW 입력 받기"""
        power = True
        while power:
            print('=' * 40)
            print("|%-38s|" %' << Login Page >>')
            print("|%-38s|" %" (Press '-1' To Exit)")
            print("-" * 40)
            # 1. ID 입력 / -1 입력
            loginID_ = input("--> ID : ")
            if loginID_ == "-1":
                print("=" * 40)
                break
            # 2. PW 입력 / -1 입력
            loginPW_ = input("--> PW : ")
            print("=" * 40)
            print(" ")
            print(" ")
            if loginPW_ == '-1':
                break
            
            cls.loginCheck(loginID_, loginPW_)

            if memberDTO.get_session() is not None:
                print(f">> Hi {memberDTO.get_session()}!! <<")
                print(">> Welcome To SmartStore <<")
                print(" ")
                print(" ")
                mm.showMainMenu()
                print(f">> Good Bye {memberDTO.get_session()} <<")
                print(" ")
                print(" ")
                memberDTO.set_session(None)
                break
            else:
                print(">> Input is not correct <<")
                print(">> Please Do It Again <<")
                print(" ")
                print(">> If You're Not Member <<")
                print(">> Please Sign Up First <<")
                print(" ")
                print(" ")


    @classmethod
    def loginCheck(cls, loginID, loginPW):
        """ params - ID,PW \n
        return - none \n
        function \n
            - 입력받은 ID와 PW를 DB와 비교해서 로그인 가능한지 확인 \n
            - 확인 후에는 Main Menu로 이동 """
        for i in MemberDTO.memberList:
            if loginID == i['loginID'] and loginPW == i['loginPW']:
                memberDTO.set_session(i['loginName'])
                break
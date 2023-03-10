from Member.memberDTO import MemberDTO
from Member.signUpMethod import SignUpMethod

memberDTO = MemberDTO()
signUpMethod = SignUpMethod()

class SignUp:

    @classmethod
    def signUp(cls):
        power = True
        while power:
            print('=' * 40)
            print("|%-38s|" % ' << Sign Up Page >>')
            print("|%-38s|" % " (Press '-1' To Exit)")
            print("-" * 40)
            # ID 입력
            signUpMethod.checkIdForSignup()
            if memberDTO.get_loginID() is None:
                print(">> Sign Up Has Been Canceled <<")
                print(" ")
                print(" ")
                break
            # PW 입력
            signUpMethod.checkPwForSignup()
            if memberDTO.get_loginPW() is None:
                memberDTO.set_loginID(None)
                print(">> Sign Up Has Been Canceled <<")
                print(" ")
                print(" ")
                break
            # Name 입력
            signUpMethod.checkNameForSignup()
            if memberDTO.get_loginName() is None:
                memberDTO.set_loginID(None)
                memberDTO.set_loginPW(None)
                print(">> Sign Up Has Been Canceled <<")
                print(" ")
                print(" ")
                break
            # phone Number 입력
            signUpMethod.checkPhoneNumberForSignup()
            if memberDTO.get_phoneNumber() is None:
                memberDTO.set_loginID(None)
                memberDTO.set_loginPW(None)
                memberDTO.set_loginName(None)
                print(">> Sign Up Has Been Canceled <<")
                print(" ")
                print(" ")
                break

            print("=" * 40)
            print(">> Sign Up Is Completed  <<")
            print(" ")
            print(" ")
            dic = {
                'Serial_NO': MemberDTO.Serial_NO,
                'loginID': memberDTO.get_loginID(),
                'loginPW': memberDTO.get_loginPW(),
                'loginName': memberDTO.get_loginName(),
                'phoneNumber': memberDTO.get_phoneNumber()
            }

            MemberDTO.memberList.append(dic)
            MemberDTO.Serial_NO += 1

            # 다시 리셋
            memberDTO.set_loginID(None)
            memberDTO.set_loginPW(None)
            memberDTO.set_loginName(None)
            memberDTO.set_phoneNumber(None)
            break
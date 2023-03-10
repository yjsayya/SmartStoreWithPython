import re
from Member.memberDTO import MemberDTO

memberDTO = MemberDTO()

class SignUpMethod:

    @classmethod
    def checkIdForSignup(cls):
        p = re.compile('^[A-Za-z0-9]{4,20}$')
        while True:
            loginID = input("--> Login ID : ")
            if loginID == '-1':
                print("=" * 40)
                print(" ")
                print(" ")
                break
            elif p.match(loginID) is not None:
                memberDTO.set_loginID(loginID)
                break
            else:
                print(">> Invalid Input. Please try again <<")
                print(" ")

    @classmethod
    def checkPwForSignup(cls):
        p = re.compile('^[A-Za-z0-9]{4,8}$')
        while True:
            loginPW = input("--> Login PW : ")
            if loginPW == '-1':
                print("=" * 40)
                print(" ")
                print(" ")
                break
            elif p.match(loginPW) is not None:
                memberDTO.set_loginPW(loginPW)
                break
            else:
                print(">> Invalid Input. Please try again <<")
                print(" ")

    @classmethod
    def checkNameForSignup(cls):
        p = re.compile('^[A-Za-z]{4,8}$')
        while True:
            loginName = input("--> Login Name : ")
            if loginName == '-1':
                print("=" * 40)
                print(" ")
                print(" ")
                break
            elif p.match(loginName) is not None:
                memberDTO.set_loginName(loginName)
                break
            else:
                print(">> Invalid Input. Please try again <<")
                print(" ")

    @classmethod
    def checkPhoneNumberForSignup(cls):
        p = re.compile(r'^010-\d{4}-\d{4}$')
        while True:
            phoneNumber = input("--> Phone Number : ")
            if phoneNumber == '-1':
                print("=" * 40)
                print(" ")
                print(" ")
                break
            elif p.match(phoneNumber) is not None:
                memberDTO.set_phoneNumber(phoneNumber)
                break
            else:
                print(">> Invalid Input. Please try again <<")
                print(" ")

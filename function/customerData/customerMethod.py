from tabulate import tabulate
import re

from function.customerData.customerDTO import CustomerDTO

customerDTO = CustomerDTO()

class CustomerMethod:

    def showCustomerList(self, todo):
        if len(CustomerDTO.CustomerList) == 0:
            print("=" * 73)
            print("|%-71s|" % f" << Customer Info. {todo}>>")
            print("-" * 73)
            print("|%-71s|" %" No Customer ")
            print("=" * 73)
            return False
        else:
            # tabulate 라이브러리 이용해서 표 출력
            print("=" * 73)
            print("|%-71s|" % f" << Customer Info. {todo}>>")
            print(tabulate(CustomerDTO.CustomerList, headers=["Serial_NO", "ID                  ", "Spent Time", "Total Payment"], tablefmt='grid'))
            print("=" * 73)
            return True

 # ------------------------------------------------------------------------------------------
    # Customer Data -- 받은 userID 확인
    def checkUserId(self):
        """parmas - none \n
        return - none \n
        func \n
            - 고객 정보 중 아이디 받기 \n
            - 알파벳 소문자 + 알파벳 대문자 + 숫자 조합으로 강제"""
        p = re.compile('^[A-Za-z0-9]{4,20}$')
        while True:
            userID_ = input("--> ID : ")
            if userID_ == '-1':
                break
            elif p.match(userID_) != None:
                customerDTO.set_userID(userID_)
                break
            else:
                print(">> Invalid Input. Please try again <<")
                print(" ")

    # Customer Data - 받은 Spent Time 확인
    def checkUserSpentTime(self):
        """parmas - none \n
        return - none \n
        func - 고객 정보 중 총 이용 시간 받기"""
        while True:
            try:
                userSpentTime_ = int(input("--> Spent Time : "))
            except ValueError:
                userSpentTime_ = -2

            if userSpentTime_ == -1:
                break
            elif 0 <= userSpentTime_ <= 100_000_000:  # 100만
                customerDTO.set_userSpentTime(userSpentTime_)
                break
            else:
                print(">> Invalid Input. Please Try Again <<")
                print(" ")

    # Customer Data - 받은 Total Payment 확인
    def checkUserTotalPayment(self):
        """parmas - none \n
        return - none \n
        func - 고객 정보 중 총 지불 비용 받기"""
        while True:
            # 1. Total Payment 입력 받기
            try:
                userTotalPayment_ = int(input("--> Total Payment : "))
            except ValueError:
                userTotalPayment_ = -2
            # 2. 상황에 따라 예외처리
            if userTotalPayment_ == -1: # Exit
                break
            elif 0 <= userTotalPayment_ <= 100_000_000:  # 100만 이하의 자연수
                customerDTO.set_userTotalPayment(userTotalPayment_)
                break
            else: # 잘못된 입력값
                print(">> Invalid Input. Please Try Again <<")
                print(" ")

# ------------------------------------------------------------------------------------------
    def checkCustomerList(self, SerialNum):
        while True:
            checkOfList = None
            for i in CustomerDTO.CustomerList:
                if i[0] == f'UID-{SerialNum}':
                    checkOfList = i
                    break
            return checkOfList

    def inputAreYouSure(self):
        while True:
            yesOrNo = input("--> Are You Sure To Input Info? (y/n) : ")
            if yesOrNo.lower() == 'y' or yesOrNo.lower() == 'yes':
                return True
            elif yesOrNo.lower() == 'n' or yesOrNo.lower() == 'no':
                return False
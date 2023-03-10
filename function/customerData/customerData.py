from function.customerData.customerDTO import CustomerDTO
from function.customerData.customerMethod import CustomerMethod

customerDTO = CustomerDTO()
customerMethod = CustomerMethod()

class CustomerData:

    @classmethod
    def addCustomerData(cls):
        """parmas - none \n
        return - none \n
        func - 필요한 고객 정보를 입력 받기"""
        power = True
        while power:
            # 0. 시작하기
            print("=" * 40)
            print("|%-38s|" % " << Add Customer Data >>")
            print("|%-38s|" % "  (Press '-1' To Exit)")
            print("-" * 40)
            # 1. userID 입력 받기
            customerMethod.checkUserId()
            if customerDTO.get_userID() == '':
                print(">> Input Of Customer Info Has Been Canceled <<")
                print(" ")
                print(" ")
                break
            # 2. Spend Time 입력 받기
            customerMethod.checkUserSpentTime()
            if customerDTO.get_userSpentTime() == -1:
                customerDTO.set_userID("")
                print(">> Input Of Customer Info Has Been Canceled <<")
                print(" ")
                print(" ")
                break
            # 3. Total Payment 입력 받기
            customerMethod.checkUserTotalPayment()
            if customerDTO.get_userTotalPayment() == -1:
                customerDTO.set_userID("")
                customerDTO.set_userSpentTime(-1)
                print(">> Input Of Customer Info Has Been Canceled <<")
                print(" ")
                print(" ")
                break
            # 4. 최종 확인
            print("=" * 40)
            if customerMethod.inputAreYouSure():
                customerDTO.CustomerList.append([
                    f'UID-{CustomerDTO.num}',
                    customerDTO.get_userID(),
                    customerDTO.get_userSpentTime(),
                    customerDTO.get_userTotalPayment()
                ])
                CustomerDTO.num += 1
                power = False
                customerDTO.set_userID('')
                customerDTO.set_userSpentTime(-1)
                customerDTO.set_userTotalPayment(-1)
                print(">> Input Of Customer Info Is Completed <<")
                print(" ")
                print(" ")
            else:
                power = False
                print(">> Input Of Customer Info Has Been Canceled <<")
                print(" ")
                print(" ")

    # ------------------------------------------------------------------------------------------
    # View CustomerData
    def viewCustomerData(self):
        customerMethod.showCustomerList("")
        check = input("--> Press Any Key To Back : ")
        if check is not None:
            print(" ")
            print(" ")


    # ------------------------------------------------------------------------------------------
    # Update Customer Data

    @classmethod
    def updateCustomerData(cls):
        power = True
        while power:
            # 0. 일단 명단을 보여줘!!
            if not customerMethod.showCustomerList("For Update "):
                print(" ")
                print(">> No Customer To Update <<")
                print(" ")
                print(" ")
                break
            else:
                try:
                    SerialNumForUpdate = int(input("--> Serial_NO : UID-"))
                except TypeError:
                    SerialNumForUpdate = -1
                # 2. 고른 번호가 있는 번호있는지 없는 번호인지 검사하기
                if SerialNumForUpdate == 0:
                    print(" ")
                    print("Update Of Customer Info Has Been Canceled")
                    print(" ")
                    print(" ")
                    break
                elif SerialNumForUpdate == -1:
                    print(">> Invalid Input. Please Try Again <<")
                    print(" ")
                else:
                    if customerMethod.checkCustomerList(SerialNumForUpdate) is None:
                        print(" ")
                        print(">> There Is No Such Serial Number <<")
                        print(">> Please Do It Again <<")
                        print(" ")
                        print(" ")
                        break
                    # 명단에 있는 것이 확인 됐음
                    else:
                        cls.updateCustomerData2(customerMethod.checkCustomerList(SerialNumForUpdate))
                        power = False

    @classmethod
    def updateCustomerData2(cls, indexNumOfCustomerData):
        power = True
        while power:
            # 1. userID 입력 받기
            customerMethod.checkUserId()
            if customerDTO.get_userID() == '':
                print(">> Update Of Customer Info Has Been Canceled <<")
                print(" ")
                print(" ")
                break
            # 2. Spend Time 입력 받기
            customerMethod.checkUserSpentTime()
            if customerDTO.get_userSpentTime() == -1:
                customerDTO.set_userID('')
                print(">> Update Of Customer Info Has Been Canceled <<")
                print(" ")
                print(" ")
                break
            # 3. Total Payment 입력 받기
            customerMethod.checkUserTotalPayment()
            if customerDTO.get_userTotalPayment == -1:
                customerDTO.set_userID('')
                customerDTO.set_userSpentTime(-1)
                print(">> Update Of Customer Info Has Been Canceled <<")
                print(" ")
                print(" ")
                break

            # 4. 최종 확인
            print("=" * 40)
            if customerMethod.inputAreYouSure():
                CustomerDTO.CustomerList[CustomerDTO.CustomerList.index(indexNumOfCustomerData)][1] = customerDTO.get_userID()
                CustomerDTO.CustomerList[CustomerDTO.CustomerList.index(indexNumOfCustomerData)][2] = customerDTO.get_userSpentTime()
                CustomerDTO.CustomerList[CustomerDTO.CustomerList.index(indexNumOfCustomerData)][3] = customerDTO.get_userTotalPayment()
                customerDTO.set_userID('')
                customerDTO.set_userSpentTime(-1)
                customerDTO.set_userTotalPayment(-1)
                print(">> Input Of Customer Info Is Completed <<")
                print(" ")
                print(" ")
                break
            else:
                power = False
                print(">> Input Of Customer Info Has Been Canceled <<")
                print(" ")
                print(" ")


    # ------------------------------------------------------------------------------------------
    # Delete Customer Data
    @classmethod
    def deleteCustomerData(cls):
        power = True
        while power:
            # 1-1 명단에 아무도 없을 때
            if not customerMethod.showCustomerList("For Delete "):
                print(" ")
                print(">> No Customer To Delete <<")
                print(" ")
                print(" ")
                break
            # 1-2 명단
            else:
                # 2. 삭제할 리스트의 시리얼 넘버 고르기
                try:
                    SerialNumForDelete = int(input("--> Serial_NO : UID-"))
                except TypeError:
                    SerialNumForDelete = -1

                # 3-1) 뒤로 가기
                if SerialNumForDelete == 0:
                    print(" ")
                    print("Delete Of Customer Info Has Been Canceled")
                    print(" ")
                    print(" ")
                    power = False
                # 3-2) 유효하지 않는 번호
                elif SerialNumForDelete == -1:
                    print(" ")
                    print(">> Invalid Input. Please try again <<")
                    print(" ")
                    print(" ")
                    print(" ")
                # 3-3) 있는 번호인지 확인하고 지우기
                else:
                    if customerMethod.checkCustomerList(SerialNumForDelete) is None:
                        print(" ")
                        print(">> There Is No Such Serial Number <<")
                        print(">> Please Do It Again <<")
                        print(" ")
                        print(" ")
                        break
                    else:
                        if customerMethod.inputAreYouSure():
                            CustomerDTO.CustomerList.remove(customerMethod.checkCustomerList(SerialNumForDelete))
                            print(" ")
                            print(">> Deleting Is Completed <<")
                            print(" ")
                            print(" ")
                            power = False
                        else:
                            print(" ")
                            print(">> Deleting Has Been Canceled <<")
                            print(" ")
                            print(" ")
                            power = False

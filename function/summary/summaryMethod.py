from tabulate import tabulate

from function.customerData.customerDTO import CustomerDTO
from function.tierSetting.tierDTO import TierDTO

tierDTO = TierDTO()
customerDTO = CustomerDTO()

class SummaryMethod:
    @classmethod
    def arrangeCustomerList(cls):
        """분류하기"""
        for i in CustomerDTO.CustomerList:
            # general 리스트에 넣기
            if tierDTO.get_generalSpentTime() <= i[2] < tierDTO.get_vipSpentTime() and tierDTO.get_generalTotalPayment() <= i[3]:
                CustomerDTO.generalList.append(i)
            elif tierDTO.get_generalTotalPayment() <= i[3] < tierDTO.get_vipTotalPayment() and tierDTO.get_generalSpentTime() <= i[2]:
                CustomerDTO.generalList.append(i)
            # VIP 리스트에 넣기
            elif tierDTO.get_vipSpentTime() <= i[2] < tierDTO.get_vvipSpentTime() and tierDTO.get_vipTotalPayment() <= i[3]:
                CustomerDTO.vipList.append(i)
            elif tierDTO.get_vipTotalPayment() <= i[3] < tierDTO.get_vvipTotalPayment() and tierDTO.get_vipSpentTime() <= i[2]:
                CustomerDTO.vipList.append(i)
            # VVIP 리스트에 넣기
            elif i[2] >= tierDTO.get_vvipSpentTime() and i[3] >= tierDTO.get_vvipTotalPayment():
                CustomerDTO.vvipList.append(i)
            # other 리스트에 넣기
            else:
                CustomerDTO.othersList.append(i)

#---------------------------------------------------------------------------------
    # sort List Method
    @classmethod
    def sortVvipList(cls, SortingBy, AscOrDesc):
        if AscOrDesc == "ASC":
            if SortingBy == "UID":
                CustomerDTO.vvipList.sort(key=lambda x: x[0])
            elif SortingBy == "userID":
                CustomerDTO.vvipList.sort(key=lambda x: x[1])
            elif SortingBy == "SpentTime":
                CustomerDTO.vvipList.sort(key=lambda x: x[2])
            elif SortingBy == "TotalPayment":
                CustomerDTO.vvipList.sort(key=lambda x: x[3])
        else:
            if SortingBy == "UID":
                CustomerDTO.vvipList.sort(key=lambda x: x[0], reverse=True)
            elif SortingBy == "userID":
                CustomerDTO.vvipList.sort(key=lambda x: x[1], reverse=True)
            elif SortingBy == "SpentTime":
                CustomerDTO.vvipList.sort(key=lambda x: x[2], reverse=True)
            elif SortingBy == "TotalPayment":
                CustomerDTO.vvipList.sort(key=lambda x: x[3], reverse=True)

    @classmethod
    def sortVipList(cls, SortingBy, AscOrDesc):
        if AscOrDesc == "ASC":
            if SortingBy == "UID":
                CustomerDTO.vipList.sort(key=lambda x: x[0])
            elif SortingBy == "userID":
                CustomerDTO.vipList.sort(key=lambda x: x[1])
            elif SortingBy == "SpentTime":
                CustomerDTO.vipList.sort(key=lambda x: x[2])
            elif SortingBy == "TotalPayment":
                CustomerDTO.vipList.sort(key=lambda x: x[3])
        else:
            if SortingBy == "UID":
                CustomerDTO.vipList.sort(key=lambda x: x[0], reverse=True)
            elif SortingBy == "userID":
                CustomerDTO.vipList.sort(key=lambda x: x[1], reverse=True)
            elif SortingBy == "SpentTime":
                CustomerDTO.vipList.sort(key=lambda x: x[2], reverse=True)
            elif SortingBy == "TotalPayment":
                CustomerDTO.vipList.sort(key=lambda x: x[3], reverse=True)

    @classmethod
    def sortGeneralList(cls, SortingBy, AscOrDesc):
        if AscOrDesc == "ASC":
            if SortingBy == "UID":
                CustomerDTO.generalList.sort(key=lambda x: x[0])
            elif SortingBy == "userID":
                CustomerDTO.generalList.sort(key=lambda x: x[1])
            elif SortingBy == "SpentTime":
                CustomerDTO.generalList.sort(key=lambda x: x[2])
            elif SortingBy == "TotalPayment":
                CustomerDTO.generalList.sort(key=lambda x: x[3])
        else:
            if SortingBy == "UID":
                CustomerDTO.generalList.sort(key=lambda x: x[0], reverse=True)
            elif SortingBy == "userID":
                CustomerDTO.generalList.sort(key=lambda x: x[1], reverse=True)
            elif SortingBy == "SpentTime":
                CustomerDTO.generalList.sort(key=lambda x: x[2], reverse=True)
            elif SortingBy == "TotalPayment":
                CustomerDTO.generalList.sort(key=lambda x: x[3], reverse=True)

    @classmethod
    def sortOthersList(cls, SortingBy, AscOrDesc):
        if AscOrDesc == "ASC":
            if SortingBy == "UID":
                CustomerDTO.othersList.sort(key=lambda x: x[0])
            elif SortingBy == "userID":
                CustomerDTO.othersList.sort(key=lambda x: x[1])
            elif SortingBy == "SpentTime":
                CustomerDTO.othersList.sort(key=lambda x: x[2])
            elif SortingBy == "TotalPayment":
                CustomerDTO.othersList.sort(key=lambda x: x[3])
        else:
            if SortingBy == "UID":
                CustomerDTO.othersList.sort(key=lambda x: x[0], reverse=True)
            elif SortingBy == "userID":
                CustomerDTO.othersList.sort(key=lambda x: x[1], reverse=True)
            elif SortingBy == "SpentTime":
                CustomerDTO.othersList.sort(key=lambda x: x[2], reverse=True)
            elif SortingBy == "TotalPayment":
                CustomerDTO.othersList.sort(key=lambda x: x[3], reverse=True)

# ---------------------------------------------------------------------------------
    # show List Method
    @classmethod
    def showVvipList(cls):
        if len(CustomerDTO.vvipList) == 0:
            print("=" * 73)
            print("|%-71s|" % f" << VVIP >>")
            print("-" * 73)
            print("|%-71s|" % f" No Customer")
            print("=" * 73)
        else:
            print("=" * 73)
            print("|%-71s|" % f" << VVIP >>")
            print(tabulate(CustomerDTO.vvipList, headers=["Serial_NO", "ID                  ", "Spent Time", "Total Payment"], tablefmt='grid'))
            print("=" * 73)

    @classmethod
    def showVipList(cls):

        if len(CustomerDTO.vipList) == 0:
            print("=" * 73)
            print("|%-71s|" % f" << VIP >>")
            print("-" * 73)
            print("|%-71s|" % f" No Customer")
            print("=" * 73)
        else:
            print("=" * 73)
            print("|%-71s|" % f" << VIP >>")
            print(tabulate(CustomerDTO.vipList, headers=["Serial_NO", "ID                  ", "Spent Time", "Total Payment"], tablefmt='grid'))
            print("=" * 73)

    @classmethod
    def showGeneralList(cls):

        if len(CustomerDTO.generalList) == 0:
            print("=" * 73)
            print("|%-71s|" % f" << GENERAL >>")
            print("-" * 36)
            print("|%-34s|" % f" No Customer")
            print("=" * 73)
        else:
            print("=" * 73)
            print("|%-71s|" % f" << GENERAL >>")
            print(tabulate(CustomerDTO.generalList,
                           headers=["Serial_NO", "ID                  ", "Spent Time", "Total Payment"],
                           tablefmt='grid'))
            print("=" * 73)

    @classmethod
    def showOthersList(cls):
        if len(CustomerDTO.othersList) == 0:
            print("=" * 73)
            print("|%-71s|" % f" << others >>")
            print("-" * 73)
            print("|%-71s|" % f" No Customer")
            print("=" * 73)
        else:
            print("=" * 73)
            print("|%-71s|" % f" << others >>")
            print(tabulate(CustomerDTO.othersList, headers=["Serial_NO", "ID                  ", "Spent Time", "Total Payment"], tablefmt='grid'))
            print("=" * 73)
            print(" ")
            print(" ")

    @classmethod
    def resetAllList(cls):
        CustomerDTO.vvipList.clear()
        CustomerDTO.vipList.clear()
        CustomerDTO.generalList.clear()
        CustomerDTO.othersList.clear()


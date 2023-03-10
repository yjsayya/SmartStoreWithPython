from function.tierSetting.tierDTO import TierDTO
from function.customerData.customerDTO import CustomerDTO
from function.summary.summaryMethod import SummaryMethod

tierDTO = TierDTO()
customerDTO = CustomerDTO()
summaryMethod = SummaryMethod()

class Summary:

    @classmethod
    def summaryAll(cls):
        cls.showSortingMethod("UID")

    @classmethod
    def summaryById(cls):
        cls.showSortingMethod("userID")

    @classmethod
    def summaryBySpentTime(cls):
        cls.showSortingMethod("SpentTime")

    @classmethod
    def summaryByTotalPayment(cls):
        cls.showSortingMethod("TotalPayment")


    @classmethod
    def showSortingMethod(cls, SortingBy):
        power = True
        while power:
            print('=' * 40)
            print("|%-38s|" % ' << Summary >>')
            print("-" * 40)
            print("|%-38s|" % ' 1. Ascending')
            print("|%-38s|" % ' 2. Descending')
            print("|%-38s|" % ' 3. Back')
            print("=" * 40)
            index_ = input("Choose One: ")
            print(" ")
            print(" ")

            try:
                index = int(index_)
            except ValueError:
                index = 5

            if index == 1:
                summaryMethod.arrangeCustomerList()

                summaryMethod.sortVvipList(SortingBy, "ASC")
                summaryMethod.sortVipList(SortingBy, "ASC")
                summaryMethod.sortGeneralList(SortingBy, "ASC")
                summaryMethod.sortOthersList(SortingBy, "ASC")

                summaryMethod.showVvipList()
                summaryMethod.showVipList()
                summaryMethod.showGeneralList()
                summaryMethod.showOthersList()
                print(" ")
                print(" ")

                summaryMethod.resetAllList()
            elif index == 2:
                summaryMethod.arrangeCustomerList()

                summaryMethod.sortVvipList(SortingBy, "DESC")
                summaryMethod.sortVipList(SortingBy, "DESC")
                summaryMethod.sortGeneralList(SortingBy, "DESC")
                summaryMethod.sortOthersList(SortingBy, "DESC")

                summaryMethod.showVvipList()
                summaryMethod.showVipList()
                summaryMethod.showGeneralList()
                summaryMethod.showOthersList()
                print(" ")
                print(" ")

                summaryMethod.resetAllList()
            elif index == 3:
                power = False
            else:
                print(">> Invalid Input. Please try again <<")
                print(" ")
                print(" ")
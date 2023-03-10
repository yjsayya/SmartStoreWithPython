from function.tierSetting.tierSetting import TierSetting
from function.customerData.customerData import CustomerData
from function.summary.summary import Summary

tierSetting = TierSetting()
customerData = CustomerData()
summary = Summary()

class MainMenu:

    def showMainMenu(self):
        """params - none \n
        return - none \n
        func - Main Menu 보여주기"""
        power = True
        while power:
            print("=" * 40)
            print("|%-38s|" %' << Main Menu >>')
            print("-" * 40)
            print("|%-38s|" % ' 1. Tier Setting')
            print("|%-38s|" % ' 2. Customer Data')
            print("|%-38s|" % ' 3. Summary')
            print("|%-38s|" % ' 4. Log Out')
            print("=" * 40)
            index_ = input("Choose One: ")
            print(" ")
            print(" ")

            try:
                index = int(index_)
            except ValueError:
                index = 5

            if index == 1:
                self.showTierSettingMainMenu()
            elif index == 2:
                self.showCustomerDataMainMenu()
            elif index == 3:
                self.showSummaryMainMenu()
            elif index == 4:
                power = False
            else:
                print(">> Invalid Input. Please try again <<")
                print(" ")
                print(" ")

    # ----------------------------------------------------------------------
    # 1. Classification Parameter
    def showTierSettingMainMenu(self):
        """params - none \n
        return - none \n
        func - Classification Parameter Main Menu 보여주기"""
        power = True
        while power:
            print("=" * 40)
            print("|%-38s|" %' << Tier Setting >>')
            print("-" * 40)
            print("|%-38s|" %' 1. View Tier')
            print("|%-38s|" %' 2. Change Tier')
            print("|%-38s|" %' 3. Back')
            print("=" * 40)
            index_ = input("Choose One: ")
            print(" ")
            print(" ")

            try:
                index = int(index_)
            except ValueError:
                index = 5

            if index == 1:
                tierSetting.viewTier()
            elif index == 2:
                tierSetting.changeTier()
            elif index == 3:
                power = False
            else:
                print(">> Invalid Input. Please try again <<")
                print(" ")
                print(" ")
                print(" ")

    # ----------------------------------------------------------------------
    # 2. Custimer Data
    def showCustomerDataMainMenu(self):
        """params - none \n
                return - none \n
                func - Customer Data Main Menu 보여주기"""
        power = True
        while power:
            print("=" * 40)
            print("|%-38s|" %' << Customer Data >>')
            print("-" *40)
            print("|%-38s|" % ' 1. Add Customer Data')
            print("|%-38s|" % ' 2. View Customer Data')
            print("|%-38s|" % ' 3. Update Customer Data')
            print("|%-38s|" % ' 4. Delete Customer Data')
            print("|%-38s|" % ' 5. Back')
            print("=" * 40)
            index_ = input("Choose One: ")
            print(" ")
            print(" ")

            try:
                index = int(index_)
            except ValueError:
                index = 6

            if index == 1:
                customerData.addCustomerData()
            elif index == 2:
                customerData.viewCustomerData()
            elif index == 3:
                customerData.updateCustomerData()
            elif index == 4:
                customerData.deleteCustomerData()
            elif index == 5:
                power = False
            else:
                print(">> Invalid Input. Please try again <<")
                print(" ")
                print(" ")
                print(" ")

    # ----------------------------------------------------------------------
    # 3. Summary
    def showSummaryMainMenu(self):
        """params - none \n
                return - none \n
                func - Summary Main Menu 보여주기"""
        power = True
        while power:
            print("=" * 40)
            print("|%-38s|" %' << Summary >>')
            print("-" * 40)
            print("|%-38s|" % ' 1. Summary')
            print("|%-38s|" % ' 2. Summary (Sorted By Name)')
            print("|%-38s|" % ' 3. Summary (Sorted By Spent Time)')
            print("|%-38s|" % ' 4. Summary (Sorted By Total Payment)')
            print("|%-38s|" % ' 5. Back')
            print("=" * 40)
            index_ = input("Choose One: ")
            print(" ")
            print(" ")

            try:
                index = int(index_)
            except ValueError:
                index = 6

            if index == 1:
                summary.summaryAll()
            elif index == 2:
                summary.summaryById()
            elif index == 3:
                summary.summaryBySpentTime()
            elif index == 4:
                summary.summaryByTotalPayment()
            elif index == 5:
                power = False
            else:
                print(">> Invalid Input. Please try again <<")
                print(" ")
                print(" ")
                print(" ")
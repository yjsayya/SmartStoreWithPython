from function.tierSetting.tierMethod import TierMethod
from function.tierSetting.tierDTO import TierDTO

tierMethod = TierMethod()
tierDTO = TierDTO()

class TierSetting:

    def viewTier(self):
        """각 등급에 대한 기준 보기 - default값 설정 되어있음"""
        print("=" * 40)
        print("|%-38s|" % ' << View Tier >>')
        print("-" * 40)
        print("|%-38s|" % ' < GENERAL >')
        print("|%-38s|" % f' - Minimun Spent Time : {tierDTO.get_generalSpentTime()}(hours)')
        print("|%-38s|" % f' - Minimun Total Payment : {tierDTO.get_generalTotalPayment()}(₩)')
        print("-" * 40)
        print("|%-38s|" % ' < VIP >')
        print("|%-38s|" % f' - Minimun Spent Time : {tierDTO.get_vipSpentTime()}(hours)')
        print("|%-38s|" % f' - Minimun Total Payment : {tierDTO.get_vipTotalPayment()}(₩)')
        print("-" * 40)
        print("|%-38s|" % ' < VVIP >')
        print("|%-38s|" % f' - Minimun Spent Time : {tierDTO.get_vvipSpentTime()}(hours)')
        print("|%-38s|" % f' - Minimun Total Payment : {tierDTO.get_vvipTotalPayment()}(₩)')
        print("=" * 40)
        if input("--> Press Any Key To Back : ") is not None:
            print(" ")
            print(" ")

    # ------------------------------------------------------------------------------------------
    # Update Parameter
    def changeTier(self):
        """
        각 등급에 대한 기준 바꾸기
        - General은 Vip보다 기준이 높을 수 없고
        - Vip는 Vvip보다 기준이 높을 수 없다
        """
        power = True
        while power:
            print("=" * 40)
            print("|%-38s|" % ' << Change Tier >>')
            print("-" * 40)
            print("|%-38s|" % ' 1. GENERAL')
            print("|%-38s|" % ' 2. VIP')
            print("|%-38s|" % ' 3. VVIP')
            print("|%-38s|" % ' 4. Back')
            print("=" * 40)
            index_ = input("Choose One: ")
            print(" ")
            print(" ")

            try:
                index = int(index_)
            except ValueError:
                index = 5

            if index == 1:
                tierMethod.generalTierChanging()
            elif index == 2:
                tierMethod.vipTierChanging()
            elif index == 3:
                tierMethod.vvipTierChanging()
            elif index == 4:
                power = False
            else:
                print(">> Invalid Input. Please try again <<")
                print(" ")
                print(" ")
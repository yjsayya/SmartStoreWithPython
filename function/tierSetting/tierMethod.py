from function.tierSetting.tierDTO import TierDTO

tierDTO = TierDTO()

class TierMethod:

    def generalTierChanging(self):
        power = True
        while power:
            try:
                print("=" * 40)
                print("|%-38s|" % ' << GENERAL Tier >>')
                print("|%-38s|" % f' Present Minimum Spent Time  : {tierDTO.get_generalSpentTime()}')
                print("|%-38s|" % f' Present Minimum Total Payment : {tierDTO.get_generalTotalPayment()}')
                print("|%-38s|" % " (Press '-1' To Exit)")
                print("-" * 40)
                time_ = int(input("--> Input Minimum Spent Time : "))
                if time_ == -1:
                    print("=" * 40)
                    print(" ")
                    print(">> Changing Has Been Canceled <<")
                    print(" ")
                    print(" ")
                    power = False
                else:
                    payment_ = int(input("--> Input Minimum Payment : "))
                    if payment_ == -1:
                        print("=" * 40)
                        print(" ")
                        print(" ")
                        power = False
                    else:
                        print("=" * 40)
                        if 0 <= time_ < tierDTO.get_vipSpentTime():
                            tierDTO.set_generalSpentTime(time_)
                            tierDTO.set_generalTotalPayment(payment_)
                            print(">> Changing GENERAL Tier Is Successful <<")
                            print(" ")
                            print(" ")
                            power = False
                        else:
                            print(">> GENERAL Tier Must Be Lower Than Other Tiers <<")
                            print(">> Please Do It Again <<")
                            print(" ")
                            print(" ")
            except ValueError:
                print(">> Invalid Input. Please try again <<")
                print(" ")
                print(" ")
                print(" ")
                continue

    def vipTierChanging(self):
        power = True
        while power:
            try:
                print("=" * 40)
                print("|%-38s|" % ' << VIP Tier> >')
                print("|%-38s|" % f' Present Minimum Spent Time  : {tierDTO.get_vipSpentTime()}')
                print("|%-38s|" % f' Present Minimum Total Money : {tierDTO.get_vipTotalPayment()}')
                print("|%-38s|" % " (Press '-1' To Exit)")
                print("-" * 40)
                time_ = int(input("--> Input Minimum Spent Time : "))
                if time_ == -1:
                    print("=" * 40)
                    print(" ")
                    print(" ")
                    power = False
                else:
                    payment_ = int(input("--> Input Minimum Payment : "))
                    if payment_ == -1:
                        print("=" * 40)
                        print(" ")
                        print(">> Changing Has Been Canceled <<")
                        print(" ")
                        print(" ")
                        power = False
                    else:
                        print("=" * 40)
                        if tierDTO.get_generalSpentTime() < time_ < tierDTO.get_vvipSpentTime() \
                                or tierDTO.get_generalTotalPayment() < payment_ < tierDTO.get_vvipTotalPayment():
                            tierDTO.set_vipSpentTime(time_)
                            tierDTO.set_vipTotalPayment(payment_)
                            print(">> Changing VIP Tier Is Successful <<")
                            print(" ")
                            print(" ")
                            power = False
                        else:
                            print(">> VIP Tier Must Be Higher Than General Tier <<")
                            print(">>    &&  Must Be Lower Than VVIP Tier <<")
                            print(">> Please Do It Again <<")
                            print(" ")
                            print(" ")
            except ValueError:
                print(">> Invalid Input. Please try again <<")
                print(" ")
                print(" ")
                print(" ")
                continue

    def vvipTierChanging(self):
        power = True
        while power:
            try:
                print("=" * 40)
                print("|%-38s|" % ' << VVIP Tier >>')
                print("|%-38s|" % f' Present Minimum Spent Time  : {tierDTO.get_vvipSpentTime()}')
                print("|%-38s|" % f' Present Minimum Total Money : {tierDTO.get_vvipTotalPayment()}')
                print("|%-38s|" % " (Press '-1' To Exit)")
                print("-" * 40)
                time_ = int(input("--> Input Minimum Spent Time : "))
                if time_ == -1:
                    print("=" * 40)
                    print(" ")
                    print(">> Changing Has Been Canceled <<")
                    print(" ")
                    print(" ")
                    power = False
                else:
                    payment_ = int(input("--> Input Minimum Total Money : "))
                    if payment_ == -1:
                        print("=" * 40)
                        print(" ")
                        print(" ")
                        power = False
                    else:
                        print("=" * 40)
                        if time_ > tierDTO.get_vipSpentTime() or payment_ > tierDTO.get_vipTotalPayment():
                            tierDTO.set_vvipSpentTime(time_)
                            tierDTO.set_vvipTotalPayment(payment_)
                            print(">> Changing VVIP Tier Is Successful <<")
                            print(" ")
                            print(" ")
                            power = False
                        else:
                            print(">> VVIP Tier Must Be Higher Than Other Tiers <<")
                            print(">> Please Do It Again <<")
                            print(" ")
                            print(" ")

            except ValueError:
                print(">> Invalid Input. Please try again <<")
                print(" ")
                print(" ")
                print(" ")
                continue
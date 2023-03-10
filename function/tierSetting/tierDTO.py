class TierDTO:

    generalSpentTime = 100
    generalTotalPayment = 10_000

    vipSpentTime = 200
    vipTotalPayment = 20_000

    vvipSpentTime = 300
    vvipTotalPayment = 30_000

    @classmethod
    def set_generalSpentTime(cls, generalSpentTime):
        cls.generalSpentTime = generalSpentTime

    @classmethod
    def set_generalTotalPayment(cls, generalTotalPayment):
        cls.generalTotalPayment = generalTotalPayment

    @classmethod
    def set_vipSpentTime(cls, vipSpentTime):
        cls.vipSpentTime = vipSpentTime

    @classmethod
    def set_vipTotalPayment(cls, vipTotalPayment):
        cls.vipTotalPayment = vipTotalPayment

    @classmethod
    def set_vvipSpentTime(cls, vvipSpentTime):
        cls.vvipSpentTime = vvipSpentTime

    @classmethod
    def set_vvipTotalPayment(cls, vvipTotalPayment):
        cls.vvipTotalPayment = vvipTotalPayment


    # getter
    @classmethod
    def get_generalSpentTime(cls):
        return cls.generalSpentTime

    @classmethod
    def get_generalTotalPayment(cls):
        return cls.generalTotalPayment

    @classmethod
    def get_vipSpentTime(cls):
        return cls.vipSpentTime

    @classmethod
    def get_vipTotalPayment(cls):
        return cls.vipTotalPayment

    @classmethod
    def get_vvipSpentTime(cls):
        return cls.vvipSpentTime

    @classmethod
    def get_vvipTotalPayment(cls):
        return cls.vvipTotalPayment
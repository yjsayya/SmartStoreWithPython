class CustomerDTO:

    # newCustomerInfo = [Serial Num 0, userID 1, userSpentTime 2, userTotalMoney 3]
    CustomerList = [
        ['UID-1', 'sayya', 101, 20001],
        ['UID-2', 'jun', 201, 10001],
        ['UID-3', 'apm', 10, 30],
        ['UID-4', 'sua', 20, 20],
        ['UID-5', 'hongGunner', 301, 25000],
        ['UID-6', 'yecoming', 302, 30000],
        ['UID-7', 'heeu', 401, 40000],
        ['UID-8', 'bk', 500, 10],
        ['UID-9', 'economics', 278, 25000],
    ]

    vvipList = []
    vipList = []
    generalList = []
    othersList = []

    # __num = CustomerDTO.CustomerList[-1][0]
    num = 10
    userID = ''
    userSpentTime = -1
    userTotalPayment = -1

    # setter
    @classmethod
    def set_userID(cls, userID):
        cls.userID = userID

    @classmethod
    def set_userSpentTime(cls, userSpentTime):
        cls.userSpentTime = userSpentTime

    @classmethod
    def set_userTotalPayment(cls, userTotalPayment):
        cls.userTotalPayment = userTotalPayment


    # getter
    @classmethod
    def get_userID(cls):
        return cls.userID

    @classmethod
    def get_userSpentTime(cls):
        return cls.userSpentTime

    @classmethod
    def get_userTotalPayment(cls):
        return cls.userTotalPayment

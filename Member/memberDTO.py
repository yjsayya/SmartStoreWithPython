
class MemberDTO:

    session = None

    loginID = None
    loginPW = None
    loginName = None
    phoneNumber = None

    memberList = [
        {
            'Serial_NO': 0,
            'loginID': 'must',
            'loginPW': '1234',
            'loginName': 'sayya',
            'phoneNumber': '01012345678'
        },
    ]

    Serial_NO = 1

    # Getter
    @classmethod
    def get_session(cls):
        return cls.session

    @classmethod
    def get_loginID(cls):
        return cls.loginID

    @classmethod
    def get_loginPW(cls):
        return cls.loginPW

    @classmethod
    def get_loginName(cls):
        return cls.loginName

    @classmethod
    def get_phoneNumber(cls):
        return cls.phoneNumber

    # Setter
    @classmethod
    def set_session(cls, session):
        cls.session = session

    @classmethod
    def set_loginID(cls, loginID):
        cls.loginID = loginID

    @classmethod
    def set_loginPW(cls, loginPW):
        cls.loginPW = loginPW

    @classmethod
    def set_loginName(cls, loginName):
        cls.loginName = loginName

    @classmethod
    def set_phoneNumber(cls, phoneNumber):
        cls.phoneNumber = phoneNumber





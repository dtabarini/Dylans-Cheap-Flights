class TooManyAcessTrys(Exception):
    """Base class for other exceptions"""
    pass


class OtherError(Exception):
    """Base class for other exceptions"""

    def __init__(self, value, responce):
        ...
        self.value = value
        self.response = responce

    pass

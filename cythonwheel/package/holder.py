
import abc


class Holder(metaclass=abc.ABCMeta):

    def __init__(self, a):
        self.a = a

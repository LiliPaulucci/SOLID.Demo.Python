from abc import ABCMeta, abstractmethod


class ITranslator(object):
    """Abstract translator."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_tens(self, position): raise NotImplementedError

    @abstractmethod
    def get_units(self, position): raise NotImplementedError


class CardinalTranslator (ITranslator):

    @staticmethod
    def get_tens(position):
        tens_list = ["Zero", "Ten", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        return tens_list[position];

    @staticmethod
    def get_units(position):
        units_list = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                      "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eightteen", "Nineteen"]
        return units_list[position];

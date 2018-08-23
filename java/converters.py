import MathUtils
from abc import ABCMeta, abstractmethod


class INumeralConverter(object):
    """Abstract converter."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def convert(self, numeral): raise NotImplementedError


class ArabicToCardinalConverter(INumeralConverter):

    def __init__(self, translator):
        self.translator = translator

    def convert(self, numeral):
        number = int(numeral)

        if number < 0 or number > 99:
            return "NotSupported: Numbers should be Integers between 0 and 99."
            # raise Exception("Error: Numbers should be Integers between 0 and 99.")

        outcome_number = ""

        if MathUtils.MathUtils.is_a_ten(number):
            outcome_number = self.translator.get_tens(MathUtils.GetQuotientOfDivisionBy10(number))
        else:
            if number < 20:
                outcome_number = self.translator.get_units(number)
            else:
                ten = MathUtils.MathUtils.get_quotient_of_division_by_10(number)
                remainder = MathUtils.MathUtils.get_remainder_of_division_by_10(number)

                outcome_number = self.translator.get_tens(ten) + " " + self.translator.get_units(remainder)

        return outcome_number

class MathUtils(object):

    @staticmethod
    def is_a_ten(income_number):
        return income_number % 10 == 0;

    @staticmethod
    def get_remainder_of_division_by_10(income_number):
        return income_number % 10;

    @staticmethod
    def get_quotient_of_division_by_10(income_number):
        return income_number / 10;

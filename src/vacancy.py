class Vacancy:
    __min_payment = 40000

    def __init__(self, name, url, payment, requirements):
        self.name = name
        self.url = url
        # if self.__validate_payment(payment):
        self.payment = payment
        # else:
        #     raise ValueError
        self.requirements = requirements

    def __str__(self):
        return f'{self.name}, {self.url}, {self.payment}, {self.requirements}'

    def __repr__(self):
        return f'{self.name}, {self.url}, {self.payment}, {self.requirements}'

    @classmethod
    def __validate_payment(cls, par_payment):
        if par_payment <= cls.__min_payment:
            return False
        return True

    def __lt__(self, object_2):
        return self.payment < object_2.payment

    def __le__(self, object_2):
        return self.payment <= object_2.payment

    def __gt__(self, object_2):
        return self.payment > object_2.payment

    def __ge__(self, object_2):
        return self.payment >= object_2.payment

    def __eq__(self, object_2):
        return self.payment == object_2.payment

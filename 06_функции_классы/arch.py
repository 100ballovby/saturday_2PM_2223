class Number:
    def __init__(self, value):
        self.value = value

    def power(self, exponent):
        return self.value ** exponent

    def sqrt(self):
        return self.value ** 0.5

    def is_positive(self):
        if self.value > 0:
            return True
        else:
            return False

    def __repr__(self):
        return str(self.value)

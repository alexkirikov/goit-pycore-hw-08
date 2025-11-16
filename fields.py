class Field:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit():
            raise ValueError("Phone number must contain only digits.")
        if len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)

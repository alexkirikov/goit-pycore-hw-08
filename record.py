from fields import Name, Phone

class Record:
    def __init__(self, name: Name):
        self.name = name
        self.phones: list[Phone] = []

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def remove_phone(self, phone_value: str):
        for phone in self.phones:
            if phone.value == phone_value:
                self.phones.remove(phone)
                return True
        return False

    def edit_phone(self, old_value: str, new_value: str):
        for phone in self.phones:
            if phone.value == old_value:
                phone.value = new_value
                return True
        return False

    def __repr__(self):
        phones = ", ".join([p.value for p in self.phones])
        return f"{self.name.value}: {phones}"

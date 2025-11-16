from collections import UserDict
from record import Record

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def get(self, name: str):
        return self.data.get(name)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

    def __repr__(self):
        return "\n".join([str(record) for record in self.data.values()])

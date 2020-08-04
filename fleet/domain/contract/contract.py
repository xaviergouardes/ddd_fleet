
from fleet.domain.shared.value_object import ValueObject

class ContractId(ValueObject):

    def __init__(self, id: str):
        assert id != ""
        assert id.__len__() != 0
        self.id = id

    def sameValueAs(self, other):
        return self.id == other.id
    
    def __str__(self):
        return self.id



class ContractAggregateRoot:
    
    def __init__(self):
        self.name = "Contract"
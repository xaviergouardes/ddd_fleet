from fleet.domain.shared.value_object import ValueObject

class SubFleetId(ValueObject):
    def __init__(self, id: str):
        assert id != ""
        assert id.__len__() != 0
        self.id = id

    def sameValueAs(self, other):
        return self.id == other.id
    
    def __str__(self):
        return self.id

class FleetId(ValueObject):
   def __init__(self, id: str):
       assert id != ""
       assert id.__len__() != 0
       self.__id = id

   def id(self) -> str:
       return self.__id

   def sameValueAs(self, other):
       return self.__id == other.id
   
   def __str__(self):
       return self.__id

class ContractId(ValueObject):
   def __init__(self, id: str):
       assert id != ""
       assert id.__len__() != 0
       self.__id = id

   def id(self) -> str:
       return self.__id

   def sameValueAs(self, other):
       return self.__id == other.id
   
   def __str__(self):
       return self.__id
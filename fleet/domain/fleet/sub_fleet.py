

from fleet.domain.shared.fleet_ids import SubFleetId, FleetId

class SubFleet:
    def __init__(self, subFleetId: SubFleetId, fleetId: FleetId, name, provider, operator, origin):
        self.__subFleetId = subFleetId
        self.__fleetId = fleetId
        self.__name = name
        self.__provider = provider
        self.__operator = operator
        self.__origin = origin

    def subFleetId(self):
        return self.__subFleetId

    def fleetId(self):
        return self.__fleetId

    def name(self):
        return self.__name

    def provider(self):
        return self.__provider

    def operator(self):
        return self.__operator

    def origin(self):
        return self.__origin

    def __str__(self):
       return "uuid: {}, fleetUuid: {}, name: {}".format( self.subFleetId(),self.fleetId() ,self.name() )

class SubFleetRepository:
    def getNextId(self) -> SubFleetId:
       raise Exception("I am an Interface, please use an Implémentation")

    def store(self, SubFleet) -> SubFleetId:
       raise Exception("I am an Interface, please use an Implémentation")

    def load(self, subFleetId:SubFleetId) -> SubFleet:
      raise Exception("I am an Interface, please use an Implémentation")
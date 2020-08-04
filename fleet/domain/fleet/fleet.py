
from fleet import DOMAIN_EVENTS_MANAGER

from fleet.domain.shared.domain_events import DomainEvent
from fleet.domain.shared.fleet_ids import SubFleetId, FleetId

from fleet.domain.contract.contract import ContractId
from fleet.domain.fleet.sub_fleet import SubFleet, SubFleetRepository


class Fleet:
   def __init__(self, fleetId: FleetId, contractId: ContractId, name, provider):
       self.__fleetId = fleetId
       self.__contractId = contractId
       self.__name = name
       self.__provider = provider
 
   def fleetId(self):
       return self.__fleetId

   def contractId(self):
       return self.__contractId

   def name(self):
       return self.__name

   def provider(self):
       return self.__provider

   def __str__(self):
       return "uuid: {}, name: {}".format( self.fleetId(), self.name() )

   def addSubFleet(self, subFleetId: SubFleetId ,name, operator, origin) -> SubFleet:
       newSubFleet = SubFleet(  subFleetId, self.fleetId(), name, self.provider(), operator, origin)
       
       DOMAIN_EVENTS_MANAGER.publish(SubFleetWasAddedEvent(self.fleetId, subFleetId))

       return newSubFleet
 


class FleetRepository:
   def getNextId(self) -> FleetId:
      raise Exception("I am an Interface, please use an Implémentation")
   def load(self, fleetId:FleetId) -> Fleet:
      raise Exception("I am an Interface, please use an Implémentation")


class SubFleetWasAddedEvent(DomainEvent):

    def __init__(self, fleetId: FleetId, subFleetId: SubFleetId):
        super().__init__()
        self.__fleetId = fleetId
        self.__subFleetId = subFleetId

    def fleetId(self):
        return self.__subFleetId

    def subFleetId(self):
        return self.__subFleetId()
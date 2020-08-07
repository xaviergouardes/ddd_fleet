
from fleet.domain.shared.fleet_ids import FleetId, SubFleetId

from fleet.domain.fleet.fleet import Fleet, FleetRepository, SubFleetWasAddedEvent
from fleet.domain.fleet.sub_fleet import SubFleet, SubFleetRepository

from fleet import DOMAIN_EVENTS_MANAGER

class FleetApplicationServicesImpl:
    
    __fleetRepository = None
    __subFleetRepository = None

    def __init__(self, fleetRepository:FleetRepository, subFleetRepository:SubFleetRepository):
        self.__fleetRepository = fleetRepository
        self.__subFleetRepository = subFleetRepository

    def addSubFleet(self, fleetId: str, name:str, operator:str, origin:str) -> SubFleetId:
      
      fleet = self.fleetRepository().load( FleetId(fleetId) )

      subFleetId = self.subFleetRepository().getNextId()
      newSubFleet = fleet.addSubFleet(subFleetId, name, operator, origin)

      subFleetId = self.subFleetRepository().store(newSubFleet)
      
      print("newSubFleet.fleetId() = ", newSubFleet.fleetId(), "newSubFleet.subFleetId() = ", newSubFleet.subFleetId())
      #FIXME: j'ai été obligé de remonter le push d'event car sinon le listener fait un find sur une sous-flottre qui n'est pas encore dans la base.
      DOMAIN_EVENTS_MANAGER.publish(SubFleetWasAddedEvent(newSubFleet.fleetId(), newSubFleet.subFleetId()))

      return subFleetId


    def fleetRepository(self) -> FleetRepository:
        return self.__fleetRepository

    def subFleetRepository(self) -> SubFleetRepository:
        return self.__subFleetRepository
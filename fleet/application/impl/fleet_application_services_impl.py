
from fleet.domain.shared.fleet_ids import FleetId, SubFleetId

from fleet.domain.fleet.fleet import Fleet, FleetRepository
from fleet.domain.fleet.sub_fleet import SubFleet, SubFleetRepository


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
      
      return subFleetId


    def fleetRepository(self) -> FleetRepository:
        return self.__fleetRepository

    def subFleetRepository(self) -> SubFleetRepository:
        return self.__subFleetRepository
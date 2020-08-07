import uuid

from fleet.domain.fleet.fleet import SubFleetWasAddedEvent, FleetId, SubFleetId, FleetRepository
from fleet.domain.fleet.sub_fleet import SubFleet, SubFleetId, SubFleetRepository

from fleet.domain.shared.domain_events import Suscriber

from fleet.infrastructure.persistence.fleet_memory_repository import FleetInMemoryRepository
from fleet.infrastructure.persistence.subfleet_memory_repository import SubFleetInMemoryRepository

from fleet.infrastructure import DATA_BASE

class SubFleetAddedListener(Suscriber):
    
    def __init__(self):
        super().__init__()
        # TODO : Travailler pour faire une réelle injection, idem pour le "dataSource" DATA_BASE
        self.__fleetRepository = FleetInMemoryRepository()
        self.__subFleetRepository = SubFleetInMemoryRepository()
    
    def handleEvent(self, event: SubFleetWasAddedEvent):
        print( "SubFleetAddedListener : fleetId [{}] subFleetId [{}] \n".format(event.fleetId(), event.subFleetId()) )

        fleet = self.__fleetRepository.load(event.fleetId())
        subFleet = self.__subFleetRepository.load(event.subFleetId())

        fleetWithSubFleet = { "fleet": fleet, "subfleet": subFleet}
        DATA_BASE["TABLE_FLEET_WITH_SUB_FLEETS"][str(subFleet.subFleetId())] = fleetWithSubFleet

    def subscribedToEventType(self):
        return "SubFleetWasAddedEvent"
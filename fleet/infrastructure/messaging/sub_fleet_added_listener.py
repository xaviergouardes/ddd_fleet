import uuid

from fleet.domain.fleet.fleet import SubFleetWasAddedEvent, FleetId, SubFleetId, FleetRepository
from fleet.domain.fleet.sub_fleet import SubFleet, SubFleetId, SubFleetRepository

from fleet.domain.shared.domain_events import Suscriber

from fleet.infrastructure import DATA_BASE

class SubFleetAddedListener(Suscriber):
    
    def __init__(self, fleetRepository:FleetRepository, subFleetRepository:SubFleetRepository):
        self.__fleetRepository = fleetRepository
        self.__subFleetRepository = subFleetRepository
    
    def handleEvent(self, event: SubFleetWasAddedEvent):
        print( "SubFleetAddedListener : fleetId [{}] subFleetId [{}] \n".format(event.fleetId(), event.subFleetId()) )

        fleet = self.__fleetRepository.load(event.fleetId())
        subFleet = self.__subFleetRepository.load(event.subFleetId())

        fleetWithSubFleet = { "fleet": fleet, "subfleet": subFleet}
        DATA_BASE["TABLE_FLEET_WITH_SUB_FLEETS"][str(subFleet.subFleetId())] = fleetWithSubFleet

    def subscribedToEventType(self):
        return "SubFleetWasAddedEvent"
import uuid

from fleet.domain.fleet.fleet import SubFleetWasAddedEvent, FleetId, SubFleetId

from fleet.domain.shared.domain_events import Suscriber


class SubFleetAddedListener(Suscriber):
    
    def __init__(self):
        super().__init__()
    
    def handleEvent(self, event: SubFleetWasAddedEvent):
        print( "SubFleetAddedListener : fleetId [{}] subFleetId [{}] \n".format(event.fleetId(), event.subFleetId()) )

    def subscribedToEventType(self):
        return "SubFleetWasAddedEvent"
from fleet import DOMAIN_EVENTS_MANAGER
from fleet.infrastructure.messaging.sub_fleet_added_listener import SubFleetAddedListener

listener = SubFleetAddedListener()
DOMAIN_EVENTS_MANAGER.subscribe(listener)
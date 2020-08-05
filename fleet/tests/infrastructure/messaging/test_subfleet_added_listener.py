import unittest

from fleet.domain.shared.domain_events import DomainEventsManager
from fleet.domain.fleet.fleet import SubFleetWasAddedEvent, FleetId
from fleet.domain.fleet.sub_fleet import SubFleetId
from fleet.infrastructure.messaging.sub_fleet_added_listener import SubFleetAddedListener

class Test_SubFleetAddedEventListener(unittest.TestCase):

    def test_test(self):       
        domainEventsManager = DomainEventsManager()
        listener = SubFleetAddedListener()
        domainEventsManager.subscribe(listener)

        event = SubFleetWasAddedEvent(FleetId("12345"), SubFleetId("6789"))
        domainEventsManager.publish(event)

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
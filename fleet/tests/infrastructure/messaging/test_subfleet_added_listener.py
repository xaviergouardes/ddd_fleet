import unittest

from fleet.domain.shared.domain_events import DomainEventsManager
from fleet.domain.fleet.fleet import SubFleetWasAddedEvent, FleetId
from fleet.domain.fleet.sub_fleet import SubFleetId
from fleet.infrastructure.messaging.sub_fleet_added_listener import SubFleetAddedListener
from fleet.infrastructure.persistence.fleet_memory_repository import FleetInMemoryRepository

class Test_SubFleetAddedEventListener(unittest.TestCase):

    def test_test(self):       
        domainEventsManager = DomainEventsManager()
        #FIXME : Le test plante car l'implémentation du listener utilise en dur un repository
        # il faudrait injecter des MockRepository pour maitriser le résultat du test
        listener = SubFleetAddedListener()
        domainEventsManager.subscribe(listener)

        event = SubFleetWasAddedEvent(FleetId("12345"), SubFleetId("6789"))
        domainEventsManager.publish(event)

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
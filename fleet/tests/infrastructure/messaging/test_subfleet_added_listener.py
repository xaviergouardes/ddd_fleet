import unittest

# from fleet.domain.shared.domain_events import DomainEventsManager
# from fleet.domain.fleet.fleet import SubFleetWasAddedEvent, FleetRepository, Fleet
# from fleet.domain.fleet.sub_fleet import SubFleetRepository, SubFleet

# from fleet.domain.shared.fleet_ids import FleetId, SubFleetId, ContractId

# from fleet.infrastructure.messaging.sub_fleet_added_listener import SubFleetAddedListener

# class MockFleetRepository(FleetRepository):
#    def load(self, fleetId:FleetId) -> Fleet:
#       return Fleet(FleetId("12345"), ContractId("XXXx07"), "My Flotte", "Provider")

# class MockSubFleetRepository(SubFleetRepository):
#     def load(self, subFleetId:SubFleetId) -> SubFleet:
#       return SubFleet(SubFleetId("6789"), FleetId("12345"), "My SubFleet", "Provider", "Operator", "Origin")

class Test_SubFleetAddedEventListener(unittest.TestCase):

    def test_test(self):       
        # domainEventsManager = DomainEventsManager()
        
        # listener = SubFleetAddedListener(MockFleetRepository(), MockSubFleetRepository())
        # listener = SubFleetAddedListener()
                
        # domainEventsManager.subscribe(listener)

        # event = SubFleetWasAddedEvent(FleetId("12345"), SubFleetId("6789"))
        # domainEventsManager.publish(event)

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
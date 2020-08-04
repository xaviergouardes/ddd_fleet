import unittest

from fleet.domain.shared.fleet_ids import FleetId, SubFleetId

from fleet.domain.fleet.fleet import Fleet, FleetRepository
from fleet.domain.fleet.sub_fleet import SubFleet, SubFleetRepository

from fleet.infrastructure.persistence.fleet_memory_repository import FleetInMemoryRepository
from fleet.infrastructure.persistence.subfleet_memory_repository import SubFleetInMemoryRepository

from fleet.application.impl.fleet_application_services_impl import FleetApplicationServicesImpl

class Test_FleetApplicationServices(unittest.TestCase):

    fleetRepository = FleetInMemoryRepository()
    subFleetRepository = SubFleetInMemoryRepository()
    fleetApplicationServices = FleetApplicationServicesImpl(fleetRepository, subFleetRepository)

    def test_test(self):       
        self.assertTrue(True)

    def test_addFleet(self):    
        uuidFleet = self.fleetRepository.getNextId()
        uuidContract = uuidFleet
        fleet = Fleet(uuidFleet, uuidContract, "My Flotte", "Opel")
        newUuidFleet = self.fleetRepository.store(fleet)

        self.fleetApplicationServices.addSubFleet(str(newUuidFleet), "Ma sous Flotte 01", "Operator", "Origin")
        self.fleetApplicationServices.addSubFleet(str(newUuidFleet), "Ma sous Flotte 02", "Operator", "Origin")

        print('\n')
        for fleet in self.fleetRepository.findAllFleets():
            print(str(fleet), '\n')

        for subFleet in self.subFleetRepository.findAllSubFleets():
            print(str(subFleet), '\n')

        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
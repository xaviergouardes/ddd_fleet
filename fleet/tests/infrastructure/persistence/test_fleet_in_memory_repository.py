import unittest

from fleet.domain.shared.fleet_ids import FleetId
from fleet.domain.contract.contract import ContractId
from fleet.domain.fleet.fleet import Fleet, FleetRepository

from fleet.infrastructure.persistence.fleet_memory_repository import FleetInMemoryRepository

class Test_FleetInMemoryRepository(unittest.TestCase):

    fleetRepository = FleetInMemoryRepository()

    def test_getNextId(self):       
        uuid = self.fleetRepository.getNextId()
        self.assertIsNotNone(uuid)
#        self.assertTrue(True)

    def test_store(self):       
        uuidFleet = self.fleetRepository.getNextId()
        uuidContract = uuidFleet
        fleet = Fleet(uuidFleet, uuidContract, "My Flotte", "Opel")
        newUuidFleet = self.fleetRepository.store(fleet)

        self.assertTrue( uuidFleet.sameValueAs(newUuidFleet) )
#        self.assertTrue(True)

    def test_load(self):   

        uuidFleet = self.fleetRepository.getNextId()
        uuidContract = uuidFleet
        fleet = Fleet(uuidFleet, uuidContract, "My Flotte", "Opel")
        newUuidFleet = self.fleetRepository.store(fleet)

#        self.assertTrue( uuidFleet.sameValueAs(newUuidFleet) )

        fleetStored = self.fleetRepository.load(newUuidFleet)
        print("fleet = " + str(fleetStored))
        self.assertEqual( fleet.name() , fleetStored.name() )

#        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
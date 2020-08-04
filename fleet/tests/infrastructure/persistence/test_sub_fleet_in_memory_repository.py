import unittest

from fleet.domain.shared.fleet_ids import FleetId
from fleet.domain.fleet.sub_fleet import SubFleet, SubFleetRepository

from fleet.infrastructure.persistence.subfleet_memory_repository import SubFleetInMemoryRepository

class Test_SubFleetInMemoryRepository(unittest.TestCase):

    subFleetRepository = SubFleetInMemoryRepository()

    def test_getNextId(self):       
        uuid = self.subFleetRepository.getNextId()
        self.assertIsNotNone(uuid)
        uuid_2 = self.subFleetRepository.getNextId()
        self.assertNotEqual(uuid, uuid_2)
#        self.assertTrue(True)

    def test_store(self):       
        uuidSubFleet = self.subFleetRepository.getNextId()
        uuidFleet = uuidSubFleet
        subFleet = SubFleet(uuidSubFleet, uuidFleet, "My Flotte", "Provider", "Operator", "Origin")
        newUuidSubFleet = self.subFleetRepository.store(subFleet)

        self.assertTrue( uuidSubFleet.sameValueAs(newUuidSubFleet) )
#        self.assertTrue(True)

    def test_load(self):   

        uuidSubFleet = self.subFleetRepository.getNextId()
        uuidFleet = uuidSubFleet
        subFleet = SubFleet(uuidSubFleet, uuidFleet, "My Flotte", "Provider", "Operator", "Origin")
        newUuidSubFleet = self.subFleetRepository.store(subFleet)

#        self.assertTrue( uuidFleet.sameValueAs(newUuidFleet) )

        subFleetStored = self.subFleetRepository.load(newUuidSubFleet)
        print("subFleet = " + str(subFleetStored))
        self.assertEqual( subFleet.name() , subFleetStored.name() )

#        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
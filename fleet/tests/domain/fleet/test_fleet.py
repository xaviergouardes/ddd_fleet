import unittest

from fleet.domain.fleet.fleet import Fleet, FleetId
from fleet.domain.contract.contract import ContractId

class Test_Fleet(unittest.TestCase):

    def test_constructor(self):

        fleetId = FleetId("0986")
        contractId = ContractId("1234")

        newFleet = Fleet(fleetId, contractId, "Ma Flotte", "Opel")

        self.assertTrue(str(newFleet.fleetId()) == "0986")
        self.assertTrue(newFleet.fleetId().sameValueAs(fleetId))

        self.assertTrue(str(newFleet.contractId()) == "1234")
        self.assertTrue(newFleet.contractId().sameValueAs(contractId))

        self.assertTrue(newFleet.name() == "Ma Flotte")
        self.assertTrue(newFleet.provider() == "Opel")
 
if __name__ == '__main__':
    unittest.main()
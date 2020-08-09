import unittest
import json
from json import JSONEncoder
from bson.objectid import ObjectId
import uuid

from pymongo import MongoClient
from fleet.domain.fleet.fleet import Fleet
from fleet.domain.shared.fleet_ids import FleetId, ContractId

from fleet.infrastructure.persistence.fleet_mongodb_repository import FleetMongoDbRepository

from fleet.infrastructure.persistence.mapper.fleet_mapper import FleetMapper

class Test_FleetMongoDbRepository(unittest.TestCase):

    fleetRepository = FleetMongoDbRepository()

    def test_connection_mongodb(self):  

        client = MongoClient("mongodb+srv://admin:admin@cluster0-t531z.mongodb.net/fleet?retryWrites=true&w=majority")
        listBases = client.list_database_names()

        fleet = Fleet(FleetId("1234"), FleetId("4567"), "My Flotte", "Provider")

        data = eval( json.dumps(fleet, default=lambda o: o.__dict__, sort_keys=True, indent=4) )

        db = client.fleet
        db.fleets.insert_one( data )
        
        self.assertTrue(listBases.__contains__("fleet"))

    def test_fleet_store(self):  
        idFleet = self.fleetRepository.getNextId()
        idContract =  ContractId(str(uuid.uuid4()))
        print(str(idFleet))

        fleet = Fleet(idFleet, idContract, "My Flotte 2 avec Mapper", "Provider")

        self.fleetRepository.store( fleet )

        self.assertTrue(True)

    def test_fleet_load(self):  
        idFleet = FleetId("71af28a3-1227-45fe-b937-2999be88f800")

        fleet = self.fleetRepository.load( idFleet )
        print("Fleet : ", fleet)
        print("fleet.fleetId() : ", fleet.fleetId())

        self.assertTrue(True)

    def test_fleet_load_direct(self):  
        client = MongoClient("mongodb+srv://admin:admin@cluster0-t531z.mongodb.net/fleet?retryWrites=true&w=majority")
        db = client.fleet
        fleet = db.fleets.find_one( {"_Fleet__fleetId": { "_FleetId__id": "71af28a3-1227-45fe-b937-2999be88f800" } })
        dicoFleet = dict(fleet)
        print("Fleet Find - dicoFleet : ", dicoFleet)
        
        name = dicoFleet["_Fleet__name"]
        idFleet = dicoFleet["_Fleet__fleetId"]["_FleetId__id"]
        print("name : ", name, " idFleet :", idFleet)

        self.assertTrue(True)

    def test_dict(self):  

        # idFleet = self.fleetRepository.getNextId()
        # data = json.dumps(idFleet.__dict__)
        # print("dictionnaire = ", data)

        idFleet = self.fleetRepository.getNextId()
        idContract = self.fleetRepository.getNextId()
        print(str(idFleet))

        fleet = Fleet(idFleet, idContract, "My Flotte", "Provider")
        # data = json.dumps(fleet.__dict__)
        # print("dictionnaire = ", data)

        data = json.dumps(fleet, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        print("dictionnaire = ", data)


        class FleetEncoder(JSONEncoder):
          def default(self, o):
            return o.__dict__

        print("data - encoder", FleetEncoder().encode(fleet))

        data = json.dumps(fleet, default=lambda o: o.__dict__, sort_keys=True)
        print("dictionnaire = ", data)      

        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
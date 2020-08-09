import uuid

from pymongo import MongoClient

from fleet.domain.shared.fleet_ids import FleetId
from fleet.domain.fleet.fleet import FleetRepository, Fleet

from fleet.infrastructure.persistence.mapper.fleet_mapper import FleetMapper, FleetIdMapper

class FleetMongoDbRepository(FleetRepository):
    
    def __init__(self):
        #FIXME: Voir comment faire pour externaliser et partager la connection, peut-etre via le pattern uow
        client = MongoClient("mongodb+srv://admin:admin@cluster0-t531z.mongodb.net/fleet?retryWrites=true&w=majority")
        self.__db = client.fleet
    
    def store(self, fleet: Fleet) -> FleetId:
        #data = eval( json.dumps(fleet, default=lambda o: o.__dict__, sort_keys=True, indent=4) )
        data = FleetMapper().toMongoDb(fleet)
        self.__db.fleets.insert_one(data)
        return fleet.fleetId()

    def load(self, fleetId: FleetId) -> Fleet:
       #print("load for " + fleetId.idString()) 
       fleetIdMongo = FleetIdMapper().toMongoDb(fleetId)
       fleetMongo = self.__db.fleets.find_one(fleetIdMongo)
       #FIXME : Encapsuler la tranformation vers le dict
       dico = dict(fleetMongo)
       fleet = FleetMapper().toFleet(dico)
       return  fleet


    def loadWithSubIds(self, fleetId: FleetId) -> Fleet:
       # si le SGBD le permet faire une requete en jointant 
       # si le SGBD ne le permet pas il faut faire un aggregate readModel et l'alimenter avec des evts.
       # le readModel dénormalise la données en regroupant les données de chaque flotte avec ses sous-flottes
       # Ainsi on peut présenter la liste de flotte - chaque flotte contiendra ses id vers les sous-flottes
       None

       return self.fleets[str(fleetId)]

    def findAllFleets(self) -> [Fleet]:
        return self.fleets.values()

    def getNextId(self) -> FleetId:
       return FleetId(str(uuid.uuid4()))
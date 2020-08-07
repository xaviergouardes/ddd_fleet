import uuid

from fleet.infrastructure import DATA_BASE 

from fleet.domain.shared.fleet_ids import FleetId
from fleet.domain.fleet.fleet import FleetRepository, Fleet

class FleetInMemoryRepository(FleetRepository):
    
    def __init__(self):
        self.fleets = DATA_BASE["TABLE_FLEETS"]
        #self.fleets = {}
    
    def store(self, fleet: Fleet) -> FleetId:
        self.fleets[str(fleet.fleetId())] = fleet
        return fleet.fleetId()

    def load(self, fleetId: FleetId) -> Fleet:
       #print("load for " + fleetId.idString()) 
       return self.fleets[str(fleetId)]

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
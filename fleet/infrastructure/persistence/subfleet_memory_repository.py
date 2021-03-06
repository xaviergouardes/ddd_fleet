import uuid

from fleet.domain.fleet.sub_fleet import SubFleetRepository, SubFleet, SubFleetId

class SubFleetInMemoryRepository(SubFleetRepository):
    
    def __init__(self):
        self.subFleets = {}
    
    def store(self, subFleet: SubFleet) -> SubFleetId:
        self.subFleets[str(subFleet.subFleetId())] = subFleet
        return subFleet.fleetId()

    def load(self, subFleetId: SubFleetId) -> SubFleet:
       #print("load for " + fleetId.idString()) 
       return self.subFleets[str(subFleetId)]

    def findAllSubFleets(self) -> [SubFleet]:
        return self.subFleets.values()

    def getNextId(self) -> SubFleetId:
       return SubFleetId(str(uuid.uuid4()))
import json

from fleet.domain.shared.fleet_ids import FleetId, ContractId
from fleet.domain.fleet.fleet import Fleet


class FleetMapper:

    def toFleet(self, fleetMongoDb:dict) -> Fleet :
        fleetId = FleetId(fleetMongoDb["_Fleet__fleetId"]["_FleetId__id"])
        contractId = ContractId(fleetMongoDb["_Fleet__contractId"]["_ContractId__id"])
        name = fleetMongoDb["_Fleet__name"]
        provider = fleetMongoDb["_Fleet__provider"]
        fleet = Fleet(fleetId, contractId, name, provider)
        return fleet

    def toMongoDb(self, fleet:Fleet) -> dict :
        return eval( json.dumps(fleet, default=lambda o: o.__dict__, sort_keys=True, indent=4) )

class FleetIdMapper:

    def toMongoDb(self, fleetId:FleetId) -> dict :
        return  {"_Fleet__fleetId": { "_FleetId__id": str(fleetId) } }

from  fleet.infrastructure import DATA_BASE

class FleetQueryServicesImpl:

    def __init__(self, dataSource:DataSource):
        super().__init__()
        self.__dataSource = dataSource

    def listAllSubFleetFleetTuple(self):
         return DATA_BASE["TABLE_FLEET_WITH_SUB_FLEETS"]
       
DATA_BASE = {}

TABLE_FLEETS = {}
TABLE_SUB_FLEETS = {}
TABLE_FLEET_WITH_SUB_FLEETS = {}

DATA_BASE["TABLE_FLEETS"] = TABLE_FLEETS
DATA_BASE["TABLE_SUB_FLEETS"] = TABLE_SUB_FLEETS
DATA_BASE["TABLE_FLEET_WITH_SUB_FLEETS"] = TABLE_FLEET_WITH_SUB_FLEETS

# class Table_Fleets:
    
#     def __init__(self, name):
#         super().__init__()   
#         self_lignes = {}     
    
#     def insert(self, fleetId:str, contractId:str, name:str, provider:str):
#         ligne = {}
#         ligne["fleetId"] = fleetId
#         ligne["contractId"] = contractId
#         ligne["name"] = name
#         ligne["provider"] = provider

#         lignes[fleetId] = ligne


#     def select(self, fleetId:str):
#         return self.__lignes[fleetId]

# class DataBase:

#     def __init__(self):
#         super().__init__()
#         self.__database = {}

#     def createTable(self, name:str):
#         self.__database[name] = Table(name)

#     def fromTable(self, name:str):
#         return self.__database[name]

# DATABASE = DataBase()
# DATABASE.createTable("FLEETS")




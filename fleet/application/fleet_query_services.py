# from fleet.domain.fleet.fleet import Fleet
# from fleet.domain.fleet.sub_fleet import SubFleet

# class SubFleetFleetTuple:

#     def __init__(self, fleet:Fleet, subFleet:SubFleet):
#         super().__init__()
#         self.__fleet = fleet
#         self.__subFleet = subFleet

#     def fleet(self) -> Fleet:
#         return self.fleet

#     def subFleet(self) -> SubFleet:
#         return self.__subFleet


# TODO : Peut etre faut-il typer les données retournées ?
class FleetQueryServices:
    def listAllFleetWithSubFleet(self):
       raise Exception("I am an Interface, please use an Implémentation")
from datetime import datetime

## Domain Event ##
class DomainEvent:

    def __init__(self):
        super().__init__()
        self.__eventVersion = 1
        self.__occurredOn = datetime.now()
    
    def eventVersion(self):
        return self.__eventVersion

    def occurredOn(self):
        return self.__occurredOn


## Suscriber ##
class Suscriber:

    def handleEvent(self, event: DomainEvent):
        raise Exception("I am an Interface, please use an Implémentation")

    def subscribedToEventType(self):
        raise Exception("I am an Interface, please use an Implémentation")

## DomainEventsManager ##
class DomainEventsManager:

    __suscriber = {}

    def publish(self, event: DomainEvent):
        print("domain events :  publish : ", event.__class__.__name__)
        for suscriber in self.__suscriber.values():
           if suscriber.subscribedToEventType() == event.__class__.__name__:
               print("domain events :  handleEvent : ", event.__class__.__name__, " on : ",  suscriber.__class__.__name__)
               suscriber.handleEvent(event)

    def subscribe(self, suscriber: Suscriber):
        self.__suscriber[suscriber.subscribedToEventType()] = suscriber
        print("domain events : suscribe ", suscriber.__class__.__name__)

    def reset(self):
        self.__suscriber = []


import unittest

from fleet.domain.shared.domain_events import DomainEventsManager, DomainEvent,  Suscriber

class SayHelloEvent(DomainEvent):
    def __init__(self):
        super().__init__()
        self.__message = "Say Hello Event !"

    def message(self):
        return self.__message

class SayHelloListener(Suscriber):
    
    def __init__(self):
        super().__init__()

    def handleEvent(self, event: SayHelloEvent):
        print("Listener say : ", event.message())

    def subscribedToEventType(self):
        #print("\n", "type(obj) = ", SayHelloEvent().__class__.__name__ )
        return SayHelloEvent().__class__.__name__

class Test_DomainEventsManager(unittest.TestCase):

    def test_test(self):
        self.assertTrue(1 == 1)

    def test_publish_suscribe(self):
        domainEventsManager = DomainEventsManager()

        domainEventsManager.subscribe( SayHelloListener() )

        domainEventsManager.publish( SayHelloEvent() )
        domainEventsManager.publish( SayHelloEvent() )
        domainEventsManager.publish( SayHelloEvent() )

        self.assertTrue(1 == 1) 

if __name__ == '__main__':
    unittest.main()
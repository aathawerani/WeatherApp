from abc import ABC, abstractmethod

from django.db import models

# Create your models here.
Grade = [
    ('excellent', 1),
    ('average, 0'),
    ('bad', -1)
]

class DRFPost(models.model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    uploaded = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices=Grade, default='average', max_length=50)

    class Meta:
        ordering = ['uploaded']

    def __str__(self):
        return self.name
    

class Observer(ABC):
    @abstractmethod
    def update(self, observable: Observable):
        pass

class Observable(ABC):
    _observers: list[Observer] = []

    @abstractmethod
    def addObserver(self, observer:Observer):
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    @abstractmethod
    def notifyObservers(self):
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

class TemperatureSensor(Observable):
    @abstractmethod
    def read(self):
        pass

class TemperatureObserver(Observer):
    def update(self, observable: Observable):
        pass

class MonitoringScreen():
    __tempObserver: TemperatureObserver

    def __init__(self):
        pass

    def displayTemp(self, temperature:float):
        pass

    def displayPressure(self, pressure:float):
        pass

class StreamingOutput(MonitoringScreen):
    pass

class Nimbus1_0TemperatureSensor(TemperatureSensor):
    pass

class Nimbus2_0TemperatureSensor(TemperatureSensor):
    pass

class TestTemperatureSensor(TemperatureSensor):
    def randomState(self):
        self.notifyObservers()
    pass

    

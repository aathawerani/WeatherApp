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
    

class Observable(ABC):
    @abstractmethod
    def addObserver(self, observer:Observer):
        pass
    @abstractmethod
    def notifyObservers(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, observable: Observable):
        pass

class TemperatureSensor(Observable):
    @abstractmethod
    def read(self):
        pass

class Nimbus1_0TemperatureSensor(TemperatureSensor):
    pass

class Nimbus2_0TemperatureSensor(TemperatureSensor):
    pass

class TestTemperatureSensor(TemperatureSensor):
    pass

class MonitoringScreen():
    def displayTemp(self, temperature:float):
        pass

    def displayPressure(self, pressure:float):
        pass

class StreamingOutput(MonitoringScreen):
    pass

class TemperatureObserver():
    def Update(self):
        pass

    

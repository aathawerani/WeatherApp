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

class AlarmListener(ABC):
    @abstractmethod
    def wakeup(self):
        pass

class AlarmClock:
    def wakeEvery(self, interval:int, alarmListener:AlarmListener):
        pass

class TemperatureSensor(Observable):
    class TemperatureAlarm(AlarmListener):
        def wakeup(self):
            self.read()
            pass

    __clock: AlarmClock
    __alarm: TemperatureAlarm
    __tempSensorImp: TemperatureSensorImp

    def __init__(self):
        self.__clock.wakeEvery(2, self.__alarm)
        pass

    @abstractmethod
    def read(self):
        pass

class PressureSensor(Observable):
    class PressureAlarm(AlarmListener):
        def wakeup(self):
            self.read()
            pass

    __clock: AlarmClock
    __alarm: PressureAlarm

    def __init__(self):
        self.__clock.wakeEvery(2, self.__alarm)
        pass

    @abstractmethod
    def read(self):
        pass

class TemperatureObserver(Observer):
    def update(self, observable: Observable):
        pass

class PressureObserver(Observer):
    def update(self, observable: Observable):
        pass

class MonitoringScreen():
    __tempObserver: TemperatureObserver
    __presObserver: PressureObserver

    def __init__(self):
        pass

    def displayTemp(self, temperature:float):
        pass

    def displayPressure(self, pressure:float):
        pass

class StreamingOutput(MonitoringScreen):
    pass

class TemperatureSensorImp(TemperatureSensor):
    pass

class PressureSensorImp(TemperatureSensor):
    pass

class Nimbus1_0TemperatureSensor(TemperatureSensorImp):
    pass

class Nimbus2_0TemperatureSensor(TemperatureSensorImp):
    pass

class TestTemperatureSensor(TemperatureSensorImp):
    def randomState(self):
        self.notifyObservers()
    pass

class Nimbus1_0PressureSensor(PressureSensorImp):
    pass

class Nimbus2_0PressureSensor(PressureSensorImp):
    pass

class TestPressureSensor(PressureSensorImp):
    def randomState(self):
        self.notifyObservers()
    pass
    

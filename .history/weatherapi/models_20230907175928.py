from abc import ABC, abstractmethod

from django.db import models

# Create your models here.
Grade = [
    ('excellent', 1),
    ('average, 0'),
    ('bad', -1)
]

#main
class DRFPost(models.model):

    def __init__(self):
        nimbusToolkitTest = NimbusToolkitTest
        weatherStation = WeatherStation(nimbusToolkitTest)        
        monScreen = MonitoringScreen(weatherStation)

class WeatherStationComponent(ABC):
    @abstractmethod
    def addTempObserver(self):
        pass
    @abstractmethod
    def addBPObserver(self):
        pass

class WeatherStation(WeatherStationComponent):
    def addBPObserver(self):
        pass
    def addTempObserver(self):
        pass

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

    def read(self):
        self.__tempSensorImp.read()

class PressureSensor(Observable):
    class PressureAlarm(AlarmListener):
        def wakeup(self):
            self.read()
            pass

    __clock: AlarmClock
    __alarm: PressureAlarm
    __presSensorImp: PressureSensorImp

    def __init__(self):
        self.__clock.wakeEvery(2, self.__alarm)
        pass

    def read(self):
        self.__presSensorImp.read()

class TemperatureObserver(Observer):
    def update(self, observable: Observable):
        pass

class PressureObserver(Observer):
    def update(self, observable: Observable):
        pass

class MonitoringScreen():
    __tempObserver: TemperatureObserver
    __presObserver: PressureObserver

    def __init__(self, weatherComponent: WeatherStationComponent):
        self.__tempObserver = weatherComponent.addTempObserver()
        self.__presObserver = weatherComponent.addBPObserver()

    def displayTemp(self, temperature:float):
        pass

    def displayPressure(self, pressure:float):
        pass

class StreamingOutput(MonitoringScreen):
    pass

class TemperatureSensorImp(TemperatureSensor):
    @abstractmethod
    def read(self):
        pass

class PressureSensorImp(TemperatureSensor):
    @abstractmethod
    def read(self):
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
    
class StationToolkit(ABC):
    @abstractmethod
    def makeTemperature():
        pass

    @abstractmethod
    def makePressure():
        pass

class NimbusToolkitTest(StationToolkit):
    def makeTemperature():
        return TestTemperatureSensor()
    def makePressure():
        return TestPressureSensor()
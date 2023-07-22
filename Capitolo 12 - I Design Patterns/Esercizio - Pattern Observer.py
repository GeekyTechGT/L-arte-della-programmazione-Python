# Classe Subject (soggetto osservato)
class WeatherStation:
    def __init__(self):
        self.observers = []
        self.temperature = None

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature)

# Classe Observer (osservatore)
class TemperatureDisplay:
    def update(self, temperature):
        print(f"La temperatura è {temperature} gradi Celsius.")

# Utilizzo
weather_station = WeatherStation()
temperature_display = TemperatureDisplay()
weather_station.add_observer(temperature_display)

weather_station.set_temperature(25)
weather_station.set_temperature(30)
weather_station.remove_observer(temperature_display)
weather_station.set_temperature(27)

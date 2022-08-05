# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Room:
    def get_name(self):
        return 42


class Street:
    def get_room(self) -> Room:
        return Room()


class City:
    def get_street(self) -> Street:
        return Street()

    def population(self):
        return 100500


class Country:
    def get_city(self) -> City:
        return City()


class Planet:
    def get_contry(self) -> Country:
        return Country()


class Person:
    def __init__(self, room: Room, city: City):
        self._room = room
        self._city = city

    def get_person_room(self):
        return self._room.get_name()

    def get_city_population(self):
        return self._city.population()


room = Room()
city = City()

person = Person(room, city)

number_room = person.get_person_room()
population_of_city = city.population()

print(f"{number_room}\n{population_of_city}\n")

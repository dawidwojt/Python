# % pip install geopy
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from dataclasses import dataclass


@dataclass
class Coordinates:
    latitude: float
    longitude: float

    def coordinates(self):
        return self.latitude, self.longitude


def get_coordinates(address: str) -> Coordinates | None:
    geolocator = Nominatim(user_agent= 'distance_calculator')
    location = geolocator.geocode(address)

    if location:
        return Coordinates(latitude=location.latitude, longitude=location.longitude)


def calculate_distance_km(address_1: ConnectionResetError, address_2: Coordinates) -> float | None:
    if address_1 and address_2:
        distance: float = geodesic(address_1.coordinates(), address_2.coordinates()).kilometers
        return distance


def get_distance_km(address_1: str, address_2: str) -> float | None:
    home_coordinates: Coordinates = get_coordinates(address_1)
    target_coordinates: Coordinates = get_coordinates(address_2)

    if distance := calculate_distance_km(home_coordinates, target_coordinates):
        print(f'{address_1} -> {address_2}')
        print(f'{distance:.2f} kilometers')
    else:
        print('Failed to calculate the distance.')


def main():
    print('Hi, to calculate distance between two places, please provide addresses \n'
          'Convention: \n'
          'Street Name & Number, Postcode & City, Country \n'
          'Example (my old dormitory address)\n'
          'Zamenhofa 10a, 00-187 Warszawa, Polska\n'
          'or just a city like:\n'
          ' London\n'
          'then it will take a point in the middle of the city.')
    print('\x1B[3m' + '* Please note that this is a distance measured in a straight line, ' + '\x1B[3m')
    in_address_1: str = input('\033[1m' + 'Enter first address:  ' + '\033[1m')
    in_address_2: str = input('\033[1m' + 'Enter second address:' + '\033[1m')
    get_distance_km(in_address_1, in_address_2)


if __name__ == "__main__":
    main()
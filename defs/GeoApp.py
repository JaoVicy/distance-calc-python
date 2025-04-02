from defs.GeoPoint import GeoPoint
from defs.DistanceCalculator import DistanceCalculator

class GeoDistanceApp:
    def __init__(self):
        self.unit = "km"  # Default unit is kilometers

    def run(self):
        self.choose_unit()
        reference_point = self.get_point_from_user("Enter the reference point")
        calculator = DistanceCalculator()

        while True:
            add_point = input("Do you want to add a point to calculate distance? (yes/no): ").strip().lower()
            if add_point == 'yes':
                point = self.get_point_from_user("Enter the point")
                calculator.add_point(point)
            else:
                break

        distances = calculator.calculate_distances(reference_point)
        for index, distance in enumerate(distances):
            distance = self.convert_distance(distance)
            print(f"Distance from reference point to point {index + 1} is {distance:.2f} {self.unit}")

    def choose_unit(self):
        while True:
            unit = input("Do you want the distances in kilometers or meters? (km/m): ").strip().lower()
            if unit in ["km", "m"]:
                self.unit = unit
                break
            else:
                print("Invalid input. Please enter 'km' for kilometers or 'm' for meters.")

    def convert_distance(self, distance):
        if self.unit == "m":
            return distance * 1000  # Convert kilometers to meters
        return distance

    def get_point_from_user(self, prompt):
        while True:
            try:
                latitude = float(input(f"{prompt} - Latitude: "))
                longitude = float(input(f"{prompt} - Longitude: "))
                return GeoPoint(latitude, longitude)
            except ValueError:
                print("Invalid input. Please enter numeric values for latitude and longitude.")
from defs.GeoPoint import GeoPoint
from defs.DistanceCalculator import DistanceCalculator
from defs.DatabaseManager import DatabaseManager

class GeoDistanceApp:
    def __init__(self):
        self.unit = "km"  # Default unit is kilometers
        self.db_manager = DatabaseManager()  # Assuming you have a DatabaseManager class to handle database operations

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
            point = calculator.points[index]
            # Salva o ponto no banco de dados com a distância
            self.db_manager.insert_point(point.latitude, point.longitude, distance)
            print(f"Distance from reference point to point {index + 1} is {distance:.2f} {self.unit}")

        self.show_saved_points()

    def show_saved_points(self):
        print("\nSaved Points in Database:")
        points = self.db_manager.fetch_all_points()
        if not points:
            print("No points found in the database.")
            return
        for point in points:
            print(f"ID: {point[0]}, Latitude: {point[1]}, Longitude: {point[2]}, Distance: {point[3]:.2f} {self.unit}")


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
from geopy.distance import geodesic
from defs.GeoPoint import GeoPoint

class DistanceCalculator:
    def __init__(self):
        self.points = []

    def add_point(self, point):
        self.points.append(point)

    def calculate_distances(self, rPoint):
        distances = []
        for point in self.points:
            distance = self.calculate_distance(rPoint, point)
            distances.append(distance)
        return distances

    @staticmethod
    def calculate_distance(point1, point2):
        return geodesic(point1.get_coordinate(), point2.get_coordinate()).kilometers
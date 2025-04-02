class GeoPoint: # class to store the latitude and longitude of a point
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_coordinate(self):
        return self.latitude, self.longitude
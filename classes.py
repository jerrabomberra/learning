class Locations:
    def __init__(self, lat, lon, chance) -> None:
        self.lat = int(lat)
        self.lon = int(lon)
        self.chance = str(chance)
        self.output = f"This is the location {self.lat}, {self.lon}, {self.chance}"
        print(self.output)

loc = Locations(100, 500, "good")

#homework5
from math import sqrt
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, x, y, radius):
        self.center = Point(x, y)
        self.radius = radius

    def contains(self, point):
        distance_squared = (point.x - self.center.x) ** 2 + (point.y - self.center.y) ** 2
        return distance_squared <= self.radius ** 2

def stats_by_city(genre):
    music_stats = {
        'HipHop': {'Dnepr': 1500, 'Lviv': 1200, 'Odesa': 1800},
        'Rock': {'Dnepr': 2500, 'Lviv': 2200, 'Odesa': 2000},
        'Pop': {'Dnepr': 2000, 'Lviv': 1800, 'Odesa': 2100}
    }

    if genre in music_stats:
        city_stats = music_stats[genre]
        most_popular_city = max(city_stats, key=city_stats.get)
        return f"The city where {genre} is most popular is {most_popular_city}"
    else:
        return f"No data available for the genre {genre}"

circle = Circle(0, 0, 5)
point_inside = Point(3, 4)
point_outside = Point(6, 6)

print(circle.contains(point_inside))
print(circle.contains(point_outside))

print(stats_by_city('Rock'))
print(stats_by_city('Country'))
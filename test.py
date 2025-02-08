class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"The Point coordinates are: ({self.x}, {self.y})"


# Create a Point object
point = Point(3, 5)
print(point)
# print(f"Point coordinates: ({point.x}, {point.y})")  # Output: Point coordinates: (3, 5)
print(f"Point coordinates: {point}")





class ImmutablePoint:
    def __new__(cls, x, y):
        instance = super(ImmutablePoint, cls).__new__(cls)
        instance.x = x
        instance.y = y
        return instance


point = ImmutablePoint(3, 4)

from pprint import pprint

pprint(globals())
print(point.x, point.y)

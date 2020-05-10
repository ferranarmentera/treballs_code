import math


def volume(r):
    """Returns the volume of a sphere with radious r."""
    v = (4.0/3.0)*math.pi*r**3
    return v


print(volume(2))

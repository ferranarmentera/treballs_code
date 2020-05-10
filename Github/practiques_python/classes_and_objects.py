"""class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)"""

# r1 = Robot()
# r1.name = "Tom"
# r1.color = "red"
# r1.weight = 30
#
# r2 = Robot()
# r2.name = "Jerry"
# r2.color = "blue"
# r2.weight = 40

"""r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

r1.introduce_self()
r2.introduce_self()"""


def cm(feet=0, inches=0):
    """convert a length from feed and inches to centimeters"""
    inches_to_cm = inches*2.54
    feet_to_cm = feet*12*2.54
    inches_to_cm + feet_to_cm


print(cm(feet=44))

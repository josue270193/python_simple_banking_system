# our class Ship
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self, destination):
        return f"The {self.name} has sailed for {destination}!"


black_pearl = Ship("Black Pearl", 800)
destination_ship = input()
print(black_pearl.sail(destination_ship))

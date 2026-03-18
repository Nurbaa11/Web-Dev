from Animal import Animal

class Elephant(Animal):
    def __init__(self, name, age, color, trunk_length):
        super().__init__(name, age, color)
        self.trunk_length = trunk_length 

    def speak(self):
        return f"{self.name} trumpets: Pawoooo!"

    def spray_water(self):
        return f"{self.name} is using their {self.trunk_length}cm trunk to spray water!"

    def __str__(self):
        return f"Elephant(name={self.name}, age={self.age}, color={self.color}, trunk_length={self.trunk_length})"
from Animal import Animal

class Elephant(Animal):
    def __init__(self, name, age, color, trunk_length):
        # Call the parent constructor (name, age, color)
        super().__init__(name, age, color)
        # Unique attribute for an elephant
        self.trunk_length = trunk_length 

    def speak(self):
        # Overriding the speak method
        return f"{self.name} trumpets: Pawoooo!"

    def spray_water(self):
        # A unique method instead of climbing
        return f"{self.name} is using their {self.trunk_length}cm trunk to spray water!"

    def __str__(self):
        # Fixed the string representation to reflect the correct class
        return f"Elephant(name={self.name}, age={self.age}, color={self.color}, trunk_length={self.trunk_length})"
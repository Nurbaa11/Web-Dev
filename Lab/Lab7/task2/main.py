from Dog import Dog
from Elephant import Elephant
from Animal import Animal

def main():
    animal = Animal("Generic Animal", 5, "Gray")
    dog = Dog("Buddy", 3, "Brown", "Labrador")
    elephant = Elephant("Dumbo", 10, "Gray", 120)

    # 2. Store in a list for Polymorphism
    # We can treat them all as 'Animal' objects in this loop
    animals = [animal, dog, elephant]

    for a in animals:
        print(a)           # Calls __str__ (Unique to each)
        print(a.speak())   # Calls speak() (Polymorphism: "Woof" vs "Pawoooo")
        print(a.eat())     # Calls base Animal method
        print("-" * 30)

    print(dog.fetch())
    print(elephant.spray_water())


if __name__ == "__main__":
    main()
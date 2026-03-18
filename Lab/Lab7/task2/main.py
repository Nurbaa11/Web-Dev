from Dog import Dog
from Elephant import Elephant
from Animal import Animal

def main():
    animal = Animal("Generic Animal", 5, "Gray")
    dog = Dog("KBTU", 3, "Konyr", "Aktos")
    elephant = Elephant("Kaban", 10, "Gray", 120)

    animals = [animal, dog, elephant]

    for a in animals:
        print(a)           
        print(a.speak())   
        print(a.eat())     
        print("-" * 30)

    print(dog.fetch())
    print(elephant.spray_water())


if __name__ == "__main__":
    main()
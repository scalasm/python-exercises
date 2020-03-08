class Animal:
    def __init__(self,name):
        self.name = name
    def say(self, something ):
        print( f"Name {self.name}: {something}" )
    def walk(self):
        print( f"{self.name} is walking!" )

class Elephant(Animal):
    def walk(self):
        print( f"{self.name} is stomping everything!" )

class Man(Animal):
    pass

class AnimalFactory:
    def __init__(self):
        self.animals = {}
        self.animals["man"] = Man("Noname")
        self.animals["elephant"] = Elephant("Pinky")
    
    def get(self, name):
        return self.animals[name]

    def who_can_walk(self):
        names = []
        for name in self.animals:
            names.append(name)
        return names            

    def make_them_walk(self):
        for animal in self.animals.values():
            animal.walk()

animal = Elephant("Elephant")
animal.say("Eeeerrrk!!!")
animal.walk()

man = Man("Mario")
man.walk()

print( "With animal factory" )
factory = AnimalFactory()
factory.get("elephant").walk()

factory.make_them_walk()

print( "Who can walk?" + str(factory.who_can_walk()) )

class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        info = ''
        if species == "mammal":
            info = "Mammals in " + self.name + ': ' + ", ".join(self.mammals) + "\n"
        elif species == "fish":
            info = "Fishes in " + self.name + ': ' + ", ".join(self.fishes) + "\n"
        elif species == "bird":
            info = "Birds in " + self.name + ': ' + ", ".join(self.birds) + "\n"

        return info + f"Total animals: {self.__animals}"

zoo_name = input()
zoo = Zoo(zoo_name)
animals = int(input())

for _ in range(animals):
    species, name = input().split(" ")
    zoo.add_animal(species, name)

species = input()
print(zoo.get_info(species))
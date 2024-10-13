#Création de la classe Animal
class Animal:
    def __init__(self, name: str, type: str) -> None:  #Constructeur de la classe
        self.name = name
        self.type = type
        
    def talk(self):
        print(f'My name is, {self.name} ,and my type is {self.type}') #Utilisation de f-string

#Héritage Chien
class Dog(Animal):
    def __init__(self, name: str, type: str, age: int) -> None:
        super().__init__(name, type)
        self.age = age

    def talk(self):
        print('Woof')

tiny = Dog('Tiny', 'Chiba', 10)
tiny.talk()
bob = Animal('Bob', 'Turtle')
bob.talk()

class Dog:
    def __init__(self, name, breed, size): # the init method runs when you first create an object of this class
        self.name = name
        self.breed = breed
        self.size = size # 'small', 'medium', or 'large'
    
    def bark(self):
        if 'Husky' in self.breed:
            print('harrooooooo!')
        elif self.size == 'small':
            print('yip')
        elif self.size == 'medium':
            print('woof')
        elif self.size == 'large':
            print('ROOAAARRRR!!!')
        

    def bio(self):
        print(f'{self.name} is a {self.size} {self.breed}.')
        self.bark()
    
    def __str__(self):
        return self.name

    def __eq__(self, other_dog):
        if self.size == other_dog.size:
            return True
        # else:# this is unecessary, the return in the previous clause will exit out of the method
        return False

    


if __name__ == '__main__':

    scooby = Dog('Scooby Doo', 'Great Dane', 'large') # scooby is being instantiated here
    scooby.name = 'Scooby Dooby Doo'

    print(scooby) # before __str__ method was implemented: <__main__.Dog object at 0x10ec31820>
    # after __str__ method was implemented: Scooby Doo
    print(scooby.name)
    print(scooby.breed)
    scooby.bark()
    print(type(scooby)) # <class '__main__.Dog'>

    # instantiating 3 student dogs:
    dandi = Dog('Dandi', 'Cairn Terrier', 'small')

    axel = Dog('Axel', 'Husky Mix', 'large')

    zoo = Dog('Zoo', 'Pit Mix', 'medium')

    dogs = [scooby, dandi, axel, zoo]

    for dog in dogs:
        print()
        print(type(dog))
        dog.bio()
        # dog.bark()


    print(dandi == axel) # False
    print(scooby == axel) # True
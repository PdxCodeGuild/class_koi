class Cat:
    def __init__(self, name, lives=9): # __init__ methods initializes an instance of the class Cat
        self.name = name # sets the name as an attribute
        self.lives = lives # sets the lives as an attribute
    
    def meow(self): # every class method takes in self as the first parameter
        print('meow')
    
    def speak(self):
        print(f'My name is {self.name}. I am a cat.  I have {self.lives} lives.')

    def jump(self, height):
        print(f'{self.name} is attempting a jump of {height} meters')
        if height < 10:
            print(f'{self.name} jumped successfully')
        else:
            print('ouch')
            self.lives -= 1
            print(f'{self.name} did not jump successfully and lost one life.  {self.lives} lives remaining.')
        if self.lives <= 0:
            print(f'{self.name} is out of lives.  RIP')
    
    def fight(self, cat):
        from random import random
        if random() > 0.5:
            print(f'{self} won the fight')
            cat.lives -= 1
            print(f'{cat} lost the fight and has {cat.lives} remaining')
        else:
            print(f'{cat} won the fight')
            self.lives -= 1
            print(f'{self} lost the fight and has {self.lives} remaining')

    def __str__(self):
        return self.name


print(__name__, 'cat.py') # this was cat cat.py when class_example.py ran
if __name__ == '__main__': # this only runs if you run py cat.py
    # instantiation
    garfield = Cat('Garfield', 9) # making an instance of the Cat class called 'Garfield' with 9 lives
    garfield.meow() # meow
    garfield.speak() # My name is Garfield. I am a cat.  I have 9 lives.
    print(garfield) # Garfield

    # from random import randint
    # from time import sleep
    # for _ in range(5):
    #     garfield.jump(randint(5, 15))
    #     sleep(4)


    heathcliff = Cat('Heathcliff', 5) # an instannce of the Cat class called 'Heathcliff' with 5 lives
    heathcliff.meow() # meow
    heathcliff.speak() # My name is Heathcliff. I am a cat.  I have 5 lives.
    print(heathcliff) # Heathcliff

    from time import sleep

    for i in range(10):
        if i % 2 == 0:
            cat1 = garfield
            cat2 = heathcliff
        else:
            cat1 = heathcliff
            cat2 = garfield
        cat1.fight(cat2)
        sleep(3)

    # example of class inheritance from Django
    # from django.db import models

    # class Cat(models.Model):
    #     name = models.CharField()
    #     lives = models.IntegerField(default=9)


    # print(garfield) # <__main__.Cat object at 0x1070cffd0> note: this was before adding the __str__ method
    # print(garfield.name) # Garfield
    # print(garfield.lives) # 9

    # garfield_dict = {'name': 'Garfield', 'lives': 9}
    # print(garfield_dict) # {'name': 'Garfield', 'lives': 9}
    # print(garfield_dict['name']) # Garfield
    # print(garfield_dict['lives']) # 9

    # print(garfield.favorite_food)
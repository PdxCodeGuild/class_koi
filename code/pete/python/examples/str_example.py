class Parrot:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def __str__(self):
        return f'{self.name} the {self.color} parrot'

    def __repr__(self):
        return f"Parrot('{self.name}', '{self.color}')"
        return f"'{self.name} the {self.color} parrot'"


polly = Parrot('Polly', 'green')
steve = Parrot('Steve', 'red')
felix = Parrot('Felix', 'black and white')

sentence = f'{polly} likes swear words'
print(sentence)

parrots = [polly, steve, felix]

print(parrots)
from cat import Cat

print(__name__, 'class_example.py') # this is __main__ class_example.py when class_example.py ran

henry = Cat('Henry', 3)

henry.meow()
henry.speak()

dog = Cat('Dog')
dog.meow()
dog.speak()
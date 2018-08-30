# Problem 6
# 20/20 points (graded)
# Consider the following hierarchy of classes:

# class Person(object):     
#     def __init__(self, name):         
#         self.name = name     
#     def say(self, stuff):         
#         return self.name + ' says: ' + stuff     
#     def __str__(self):         
#         return self.name  
# 
# class Lecturer(Person):     
#     def lecture(self, stuff):         
#         return 'I believe that ' + Person.say(self, stuff)  
# 
# class Professor(Lecturer): 
#     def say(self, stuff): 
#         return self.name + ' says: ' + self.lecture(stuff)
# 
# class ArrogantProfessor(Professor): 
#     def say(self, stuff): 
#         return 'It is obvious that ' + self.say(stuff)

# As written, this code leads to an infinite loop when using the Arrogant Professor class.

# Change the definition of ArrogantProfessor so that the following behavior is achieved:

# e = Person('eric') 
# le = Lecturer('eric') 
# pe = Professor('eric') 
# ae = ArrogantProfessor('eric')
# 
# >>> e.say('the sky is blue')
# eric says: the sky is blue
# 
# >>> le.say('the sky is blue')
# eric says: the sky is blue
# 
# >>> le.lecture('the sky is blue')
# I believe that eric says: the sky is blue
# 
# >>> pe.say('the sky is blue')
# eric says: I believe that eric says: the sky is blue
# 
# >>> pe.lecture('the sky is blue')
# I believe that eric says: the sky is blue
# 
# >>> ae.say('the sky is blue')
# eric says: It is obvious that eric says: the sky is blue
# 
# >>> ae.lecture('the sky is blue')
# It is obvious that eric says: the sky is blue

class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff):
        return self.name + ' says: ' + Lecturer.lecture(self, stuff)

class ArrogantProfessor(Professor):
    def lecture(self, stuff):
        return 'It is obvious that ' + Person.say(self, stuff)

    def say(self, stuff):
        return self.name + ' says: ' + self.lecture(stuff)

e = Person('eric')
le = Lecturer('eric')
pe = Professor('eric')
ae = ArrogantProfessor('eric')

print(ae.say('the sky is blue'))
print('\n')
print(e.say('the sky is blue'))
print('\n')
print(le.say('the sky is blue'))
print('\n')
print(le.lecture('the sky is blue'))
print('\n')
print(pe.say('the sky is blue'))
print('\n')
print(pe.lecture('the sky is blue'))
print('\n')
print(ae.say('the sky is blue'))
print('\n')
print(ae.lecture('the sky is blue'))

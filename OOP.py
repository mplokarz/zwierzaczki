class Critter(object):
    # Zwierzak z atrybutem
    # Demonstruje tworzenie atrybutów obiektu i uzyskiwanie do nich dostępu

    def __init__(self, name):
        print("Urodził się nowy zwierzak!")     # specjalna metoda (konstruktor) wywoływana automatycznie zaraz po utworzeniu nowego obiektu klasy Critter
        self.name = name

    def __str__(self):
        rep = "Obiekt klasy Critter\n"
        rep += "name: " + self.name + "\n"
        return rep

    def talk(self):                             # ta metoda ma tylko jeden parametr (niezbędny), ktorego akurat nie używa, dostarcza metodzie sposób odwołąnai się do samego obiektu
        print("Cześć! Jestem " + self.name + "\n")

# część główna
crit1 = Critter("Reksio")        #konkretyzacja obiektu
crit1.talk()                     #wywołanie metody talk()

crit2 = Critter("Bobek")
crit2.talk()

print("Wyświetlenie obiektu crit1:")
print(crit1)
print("Bezpośrednie wyświetlenie wartości atrybutu crit1.name:")
print(crit1.name)


#input("\n\nAby zakończyć program, naciśnij klawisz Enter.")





#########################################################################



















'''
class Example:
    def __init__(self, var1, var2):
        self.first_var = var1
        self.second_var = var2
        
    def print_variables(self):
        print('{} {}'.format(self.first_var, self.second_var))

    def __str__(self):
        return 'Person: {}'.format(self.first_var)
        
e = Example('abc', 123)
#e.print_variables()
print(e)


class Mammal:
    def walk(self):
        print('walk')
class Dog(Mammal):
    def bark(self):
        print('bark')
dog = Dog()
dog.walk() # inherited from Mammal
dog.bark() # defined in Dog 
'''
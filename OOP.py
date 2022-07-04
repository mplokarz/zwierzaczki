class Critter(object):
    #Zwierzak z atrybutem
    #Demonstruje tworzenie atrybutów obiektu i uzyskiwanie do nich dostępu
    total = 0

    @staticmethod          #wbudowany dekorator do tworzenia metod statycznych klasy
    def status():          #tworzymy metodę statyczną, związaną z klasą Critter i wykorzystującą atrybut klasy: total. Ponieważ jest to metoda klasy, nie dajemy parametru self,
        print("\n Ogólna liczba zwierzaków wynosi", Critter.total)        #który niezbędny jest tylko dla metod obiektu
    

    def __init__(self, name):
        print("Urodził się nowy zwierzak!")     #specjalna metoda (konstruktor) wywoływana automatycznie zaraz po utworzeniu nowego obiektu klasy Critter
        self.name = name
        Critter.total += 1


    def __str__(self):
        rep = "Obiekt klasy Critter\n"
        rep += "name: " + self.name + "\n"
        return rep


    def talk(self):                             #ta metoda ma tylko jeden parametr (niezbędny), ktorego akurat nie używa, dostarcza metodzie sposób odwołąnia się do samego obiektu
        print(f"Cześć! Jestem {self.name}.")


# część główna
print("Uzyskanie dostępu do atrybutu klasy Critter.total:", end=" ")
print(Critter.total)

print("\nTworzenie zwieczaków.")
crit1 = Critter("zwierzak 1")
crit2 = Critter("zwierzak 2")
crit3 = Critter("zwierzak 3")
crit4 = Critter("zwierzak 4")
crit5 = Critter("zwierzak 5")

Critter.status()

print("\nUzyskanie dostępu do atrybutu klasy poprzez obiekt:", end=" ")
print(crit1.total)


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
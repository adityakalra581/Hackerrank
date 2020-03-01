
'''
An abstract class can be considered as a blueprint for other classes,
allows you to create a set of methods that must be created within
any child classes built from your abstract class.

ABSTRACT CLASS:
A class which contains one or abstract methods is called an abstract class.


ABSTRACT METHOD:
An abstract method is a method that has declaration but not has any
implementation.

'''






from abc import ABC    ## ABC Stands for Abstract Base Classes.
class Polygon(ABC):
    # Abstract Class containing one or more abstract methods.
    def noofsides(self):
    # Abstract Method: Declaration is done but no Implementation.
        pass

class Triangle(Polygon):
    # Child Class of Parent Polygon
    def noofsides(self):
        ## Implementation of Abstract method is done in child class.
        print("No. of sides = 3" )

Triangle().noofsides()        

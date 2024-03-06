from enum import Enum # se pari e imprtojme librarin enum qe kemi me kriju enums

class Foods(Enum):  # e krijojem klasen Foods qe do te trashegohet nga klasa Enum
    PIZZA="pizza" # enums i shkruajme me shkronja te medha dhe ja u japin nje vlere te tyre, njejt si konstante me key value pairs
    CHEESE="cheese"
    LASAGNA="lasagna"
    BEEF="beef"
    
print(Foods.BEEF) # e kthejme si rezultat veq Foods.Beef
print(Foods.CHEESE.name) # e kthejme si rezultate emrin e enum qe dmth CHEESE
print(Foods.LASAGNA.value) # e kthejme si rezultat vleren e enum LASAGNA te qasshme ne klasen Foods
print(type(Foods.PIZZA))  # si rezultat ka me kthy se qfar data type eshte dmth enum klasa Foods
print(repr(Foods.CHEESE)) # kjo ka me reprezentu si string format: Foods.Cheese cheese
print(list(Foods)) # ka me kthy krejt ni liste te vlerave te enums [<Foods.PIZZA: 'pizza'>, <Foods.CHEESE: 'cheese'>, <Foods.LASAGNA: 'lasagna'>, <Foods.BEEF: 'beef'>]
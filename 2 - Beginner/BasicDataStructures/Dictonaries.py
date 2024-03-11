#Dictonaries

person1= {"name" : "Lekë", "lName" : "Kelmendi", "age" : 21}

print(person1.values()) # just printing the values of the dict

print(person1) # printing the whole dict

print(person1.keys()) # printing the keys

person1.update({"college": "UBT"}) # updating the dictonary

print(person1)

person1.pop("age") # removing the element with key \"age\"

print(person1)

person1.popitem() #removing the last element on the dictionary
print(person1)


print("--------------")
print ("\n")

person1["age"]=21


person = person1.copy()

print(person)

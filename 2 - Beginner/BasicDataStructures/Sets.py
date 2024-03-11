# Sets

cars = {"BMW", "Toyota", "Fiat", "Jaguar", "Mercedes Benz","Tesla"}

cars1= {"BMW","Volswagen","Tiguan"}

intersect = cars & cars1 # checking are the elements the same with the other set

print(intersect)

mod = cars | cars1 # checking all the elements
print(mod)

lessthan  = cars < cars1 # a boolean value comparing elemenents
print(lessthan)

greaterthan= cars > cars1 # same 
print(greaterthan)

print(list(cars)+list(cars1)) # returning all of set

print(cars)



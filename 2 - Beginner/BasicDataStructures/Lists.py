#Lists
animalbreeds=["Pitbull","Marley","Blue Stafford",5]

print(animalbreeds) # just printing the result

print(animalbreeds[2]) # just showing the result of the list in index 2, 3rd place


print(animalbreeds[-3]) # just showing the result of the list in index -3, so the indexing goes from -1 from the right to the left

animalbreeds[1]="Beagle" # we just updated the result of the 2nd index, so at the index 1

print(animalbreeds[:3]) # printed the updated result, and also sliced from the 1st index to the index 2, without including index 3

animalbreeds.append("Labrador Retriever") # added an item to list

print(animalbreeds)

animalbreeds.pop() # it just removes the element on the last index

print(animalbreeds)

animalbreeds.extend([8,"Marley"]) # just like the append method we are trying to add more than one elements on the list

print(animalbreeds) 

animalbreeds.remove(5) # just llike the pop method, but it does removing the specific item on a list, b specifying the name of the element

print(animalbreeds)

animalbreeds.insert(1, "Golden Retriever") # with the method insert, im trying to insert an item to the index 1, with name golden retriever

print(animalbreeds)

print("Pitbull" in animalbreeds) # we are jsut checking 

print(len(animalbreeds)) # checking the length of the list animalbreeds
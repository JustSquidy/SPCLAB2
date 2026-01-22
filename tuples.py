# sets

cats = set()

cats.add("Lion")
cats.add("Tiger")
print(cats)

birds = {"Parrot", "Eagle", "Penguin"}
print(birds)
birds.add("Sparrow")
print(birds)
birds.remove("Eagle")
print(birds)

for bird in birds: # loops through all the birds
    print(bird)

bird_list = ["Parrot", "Eagle", "Penguin", "Parrot", "Eagle"]
bird_list_no_duplicates = list(set(bird_list))
print(bird_list_no_duplicates) # displays list without duplicates and turns it back to a list
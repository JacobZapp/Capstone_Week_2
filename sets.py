# NO DUPLICATES IN SETS
# Sets go in alphabetical order automatically


cats = set() # creates empty set

# add method adds elements to the set
cats.add('Tiger')
cats.add('Lion')
print(cats)
cats.add('Leopard')
cats.add('Cheetah')
cats.add('Panther')
print(cats)

# Creating a set with initial values
birds = {'Sparrow', 'Eagle', 'Parrot', 'Penguin', 'Owl'}
print(birds)
birds.add('Sparrow') # this will not error, but will not add duplicate either, so make sure to not add duplicates
print(birds)
# Removing items from a set
birds.remove('Penguin')
print(birds)

for bird in birds:
    print(bird)

bird_list = ['Sparrow', 'Eagle', 'Parrot', 'Penguin', 'Owl', 'Eagle', 'Parrot', 'Sparrow']
print(bird_list)

# This is converting the bird_list list to a set to remove duplicates, then back to a list in the same line
bird_list_no_duplicates = list(set(bird_list)) # this does not preserve order
print(bird_list_no_duplicates)
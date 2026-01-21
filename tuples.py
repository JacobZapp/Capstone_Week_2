# The pairs here are what tuples are. Number of items you can fit into a tuple is infinite, but usually they are small in size.
city_state = [('Minneapolis', 'MN'), ('Baraboo', 'WI'), ('New York', 'NY'), ('Los Angeles', 'CA'), ('Miami', 'FL')]
print(len(city_state))

# Getting first tuple from the list
first_pair = city_state[0]
print(first_pair)

# Tuple Unpacking
print(first_pair[0])  # Accessing first element of the tuple
print(first_pair[1])  # Accessing second element of the tuple 

city, state = first_pair  # Unpacking the tuple into two variables
print(city) # Accessing city
print(state) # Accessing state
print(city, state) # Printing both city and state

# Example of more than 2 items in a tuple being unpacked
animals = [('lion', 'tiger', 'cougar'), ('black bear', 'grizzly bear', 'polar bear'), ('eagle', 'hawk', 'falcon')]


lion, tiger, cougar = animals[0]  # Unpacking the first tuple in the list
print(lion)
print(tiger)
print(cougar)

# Getting Distance Function
def get_distance():
    miles = 1000
    km = miles * 1.6
    return miles, km  # Returning a tuple with two values

distances = get_distance()  # Receiving the tuple
print(distances)  # Printing the tuple

miles, km = get_distance()  # Unpacking the returned tuple into two variables
print(miles)  # Printing miles
print(km)     # Printing kilometers
 
try:
    print(distances[2])  # This will raise an IndexError since there are only two items in the tuple
except:
    print('Oops, that does not exist')

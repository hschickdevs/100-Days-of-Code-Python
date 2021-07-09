states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
                     "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
                     "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont",
                     "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
                     "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
                     "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota",
                     "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho",
                     "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[49])

num_of_states = len(states_of_america)

# IndexError
# print(states_of_america[50])
# print(states_of_america[num_of_states])

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes",
               "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

print(dirty_dozen)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

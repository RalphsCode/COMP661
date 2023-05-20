# PART 1
###########

# The code displays an average temperature for each day in the data dictionary.
# The for statment loops through each element in the data dictionary.


# PART 2
###########

from collections import Counter 
text = "Peter Piper picked a peck of pickled peppers A peck of pickled peppers Peter Piper picked if Peter Piper picked a peck of pickled peppers Where is the peck of pickled peppers Peter Piper picked"
arr = text.lower().split()                                                                  # ALL LETTERS TO LOWER CASE, AND CONVERT TO ARRAY
counter = Counter(arr)                                                                      # USE THE PYTHON COUNTER FUNCTION TO COUNT INSTANCES
sorted_dict = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))               # SORT BY FREQUENCY, AND PUT INTO DICTIONARY
print('\n WORD      Count\n')
for word, count in sorted_dict.items():                                                     # LOOP THROUGH THE WORDS
    print(f'{word:<10}  {count:>2}' )                                                       # DISPLAY THE RESULT
print()


# PART 3
############

# Objects that can be stored in a Dictionary:
# (1) AUTOMOBILE: MODEL, YEAR, VIN, COLOR, STYLE
# (2) CUSTOMER: NAME, SKUs PURCHASED, YEAR INITIATED
# (3) SHIPPING CONTAINER: ID, MATERIAL, SIZE, YEAR MANUFACTURED


# PART 4
###########

# dictionaries and lists - MUTABLE - You can change, add, or remove elements from a list or dictionary after it is created.
# strings and tuples - IMMUTABLE - Once created one cannot change its elements nor characters.
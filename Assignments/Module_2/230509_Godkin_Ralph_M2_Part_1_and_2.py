# PART 1
################################################################################
# REVERSE
# To sort a list in descending order, call list method sort with the optional keyword argument REVERSE set to True.

# PART 2
################################################################################

import random
import string

ranLetters = []
# Generate 10 random letters
for i in range(10):
    random_letter = random.choice(string.ascii_letters).lower()
    ranLetters.append(random_letter)
print(f'\n\t> Original list: {ranLetters}')
ranLetters.sort()
print(f'\n\ta. Sorted ASCEND: {ranLetters}')
ranLetters.sort(reverse=True)
print(f'\n\tb. Sorted DESCEND: {ranLetters}')
ranLettersSet = sorted(set(ranLetters))
print(f'\n\tc. Set sorted: {ranLettersSet}\n')

# PART 3
################################################################################

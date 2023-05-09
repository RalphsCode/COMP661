import time

probSize = [1000000, 3000000, 9000000, 27000000]
work = 1
print('\nProblem Size     Run Time')
for f in probSize:
    start_time = time.time()
    for x in range (f) :
            work += 5
            work -= 5
    end_time = time.time()
    print(f"{f:>10,}\t{(end_time - start_time):.3f} seconds")
print('')

# OUTPUT:
#
#    Problem Size     Run Time
#     1,000,000      0.091 seconds
#     3,000,000      0.264 seconds
#     9,000,000      0.785 seconds
#     27,000,000      2.419 seconds
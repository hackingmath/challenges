"""Birthday Problem"""

import random

NUM = 43 #number of people in the room
TRIALS = 10000
successes = 0

def repeat(room):
    for n in room:
        if room.count(n) > 1:
            return True
    return False

for i in range(TRIALS):
    room = [random.randint(1,365) for i in range(NUM)]
    if repeat(room):
        successes += 1

print("Probability:",successes / TRIALS)
    


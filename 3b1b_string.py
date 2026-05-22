"""
There is a set of strings of size n. Each string begins
with 2 ends. Out of the entire set, 2 ends are chosen at random,
regardless of size. The two chosen ends are attached. If the
two ends belonged to the same string, they are attached,
making a loop with no ends. If they belonged to different strings
the two strings form one longer string. This is repeated until
no ends remain.

The system begins with 2n ends. At each step, 2 ends are removed
from the system, therefore, the trial ends after n steps.
"""


import random

def average_100000(func):
    def wrapper(*args, **kwargs):
        total = 0
        for i in range(100000):
            total += func(*args, **kwargs)
        return total / 100000
    return wrapper

@average_100000
def trial(n: int):
    """
    Runs equivelent simulation of picking 2 ends of strings
    from initial set of size n.
    """
    total = 0
    for i in range(n, 0, -1):
        if random.randint(1,i) == 1:
            total += 1

    return total

print(trial(100))


total = 0
for i in range(1,101):
    total += 1/i

print(total)

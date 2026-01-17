"""
A simple script to solve the problem presented by 3Blue1Brown in this video
youtube.com/shorts/t3jZ2xGOvYg

Shows that the distribution is uniform for integers [1,11]
"""

import random
import matplotlib.pyplot as plt

class Clock():
    """
    Clock object. As described in the video, an agent starts on 12,
    and randomly moves clockwise or counterclockwise by 1 hour around
    the clock. The goal is to find the probability distribution of the
    last hour to be visited

    The Clock object keeps track of this using a current state,
    representing where the agent is, and a visited dictionary,
    which keeps a boolean value for each hour
    """
    def __init__(self):
        self.current_state = 12
        self.visited = {12: True} | {i: False for i in range(1,12)}

    def step(self):
        if random.choice([True, False]):
            self.current_state = self.current_state % 12 + 1
        else:
            self.current_state = (self.current_state - 2) % 12 + 1

        self.visited[self.current_state] = True

    def simulate(self):
        """
        Uses step() until the all hours have been visited.
        Returns the current state, which will be the last
        hour visited
        """
        while not all(self.visited.values()):
            self.step()
        return self.current_state


last_hours = []
for i in range(50000):
    clock = Clock()
    last_hours.append(clock.simulate())

plt.hist(last_hours, bins = [i - 0.5 for i in range(1,13)])
plt.xticks(range(1,13))
plt.show()

import numpy as np
import random

DIE = [1, 2, 3, 4, 5, 6]


def calculateExpectedPayout(ep, rolls_left):
    reroll = []
    if ep[rolls_left] == 0:
        for value in DIE:
            if value > calculateExpectedPayout(ep, rolls_left - 1):
                reroll.append(value)
        ep[rolls_left] = (len(reroll) / 6) * (np.mean(reroll)) + (1 - len(reroll) / 6) * ep[rolls_left - 1]
        return ep[rolls_left]

    return ep[rolls_left]


def simulateRolls(diceRolls, rolls_left):
    for roll in range(rolls_left):
        diceRolls.append(random.choice(DIE))

def calculateExpectedNewAverage(diceRolls, rolls):
    return (sum(diceRolls) + ep[-rolls]) / (rolls + 1)



if __name__ == "__main__":
    EP_array = np.zeros(50)
    EP_array[0] = 3.5
    diceRolls = []
    rolls_left = 50
    calculateExpectedPayout(EP_array, rolls_left - 1)
    simulateRolls(diceRolls, rolls_left)
    print(diceRolls)
    print(EP_array)
import numpy as np
import random

np.set_printoptions(legacy='1.25')

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


def rollDice(ep, roll, diceRolls, current_average, expected_new_average):
    diceRolls.append(random.choice(DIE))
    expected_new_average.append(calculateExpectedNewAverage(diceRolls, roll, ep))
    current_average.append(sum(diceRolls) / (roll + 1))

def calculateExpectedNewAverage(diceRolls, roll, ep):
    return (sum(diceRolls) + ep[roll + 1]) / (roll + 2)



if __name__ == "__main__":
    EP_array = np.zeros(50)
    EP_array[0] = 3.5
    diceRolls = []
    current_average = []
    expected_new_average = []
    rolls_left = 50
    calculateExpectedPayout(EP_array, rolls_left - 1)
    for roll in range(rolls_left - 1):
        rollDice(EP_array, roll, diceRolls, current_average, expected_new_average)
        if current_average[roll - 1] > expected_new_average[roll - 1]:
            print(f"{current_average}\n")
            print(expected_new_average)
            break
            
    print(f"{EP_array}\n")
    print(f"{diceRolls}\n")
    print(f"{current_average}\n")
    print(expected_new_average)
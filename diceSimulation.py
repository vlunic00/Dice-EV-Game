import numpy as np
import random
import matplotlib.pyplot as plt

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

def updateGlobalAverages(global_average, expected_global_average, n, roll, current_average, expected_new_average):
    global_average[roll] = (global_average[roll] * (n - 1) + current_average[roll]) / n
    expected_global_average[roll] = (expected_global_average[roll] * (n - 1) + expected_new_average[roll]) / n


def runSimulation(global_average, expected_global_average, n, tresholds):
    EP_array = np.zeros(50)
    EP_array[0] = 3.5
    diceRolls = []
    current_average = []
    expected_new_average = []
    rolls_left = 50
    calculateExpectedPayout(EP_array, rolls_left - 1)
    for roll in range(rolls_left - 1):
        rollDice(EP_array, roll, diceRolls, current_average, expected_new_average)
        updateGlobalAverages(global_average, expected_global_average, n, roll, current_average, expected_new_average)
        if current_average[roll] > expected_new_average[roll]:
            tresholds.append(current_average[roll])
            break





if __name__ == "__main__":            
    number_of_simulations = 10000
    global_average = np.zeros(49)
    expected_global_average = np.zeros(49)
    tresholds = []
    for n in range(1, number_of_simulations + 1):
        runSimulation(global_average, expected_global_average, n, tresholds)
    plt.plot(np.arange(1, 50), global_average)
    plt.plot(np.arange(1, 50), expected_global_average)
    plt.legend(["Global Average Roll", "Expected Global Average Roll"])
    plt.xlabel("Number of rolls")
    plt.ylabel("Average roll value until roll")
    plt.show()
    print(min(tresholds))
    print(f"{len(tresholds) / number_of_simulations * 100}%")
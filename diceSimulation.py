import numpy as np

DIE = [1, 2, 3, 4, 5, 6]


def calculateExpectedPayout(ep, throws_left):
    reroll = []
    if ep[throws_left] == 0:
        for value in DIE:
            if value > calculateExpectedPayout(ep, throws_left - 1):
                reroll.append(value)
        ep[throws_left] = (len(reroll) / 6) * (np.mean(reroll)) + (1 - len(reroll) / 6) * ep[throws_left - 1]
        return ep[throws_left]

    return ep[throws_left]


if __name__ == "__main__":
    EP_array = np.zeros(20)
    EP_array[0] = 3.5
    throws_left = 19
    calculateExpectedPayout(EP_array, throws_left)
    print(EP_array)
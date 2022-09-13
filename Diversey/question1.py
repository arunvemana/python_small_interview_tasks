"""
Question1:
You have been asked to play the following two player game.
A fair 6 sided die is rolled until a one of the player wins.
Player 1 wins when two 1's are rolled consecutively.
Player 2 wins when a 1 is rolled immediately followed by 2.
"""


def checking_probability_of_dice():
    import random
    import collections
    liste = random.choices((1, 2, 3, 4, 5, 6), k=1000000)
    c = collections.Counter(liste)
    print(c)
    # calculating the probability
    p = [j / 1e6 for j in c.values()]
    print("probality of the dice", p)
    # plotting the graph for visual
    import matplotlib.pyplot as plt
    # plt.bar(c.keys(),p)
    # plt.show()
    # checking with fair dice probablity that is 1/6
    p = [round(j - 1 / 6, 6) for j in p]
    print("Difference from actually fair dice ", p)  # almost equal to the fair dice
    # plt.bar(c.keys(),p)
    # plt.show()


import random


def dice_roll():
    dice_value = random.choices((1, 2, 3, 4, 5, 6))
    return dice_value[0]


def question_1():
    roll_counter = 0
    previous_value = 0
    while True:
        v = dice_roll()
        if previous_value == 1:
            print("Playar 1 is the winner")
            print("At roll counter:", roll_counter)
            break
        elif previous_value + 1 == 2:
            print("player 2 is the winner")
            print("At roll counter:", roll_counter)
            break
        else:
            print("Rolling again")
            print("Roll count:", roll_counter)
            previous_value = v
            roll_counter +=1


if __name__ == '__main__':
    """if the choice was given,
    Choose the Player 1 because, probablity of rolling of dice
    is higher than the Player 2 """
    # checking_probability_of_dice()
    question_1()

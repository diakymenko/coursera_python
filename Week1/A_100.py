"""
TODO: Write a description here
"""

NUM_OF_PLAYERS = 2
NUM_OF_STONES = 20
def main():
    play()

def play():
    stones = NUM_OF_STONES
    while True:
        for player in range(1, NUM_OF_PLAYERS + 1):
            if check_winner(player, stones):
                return
            stones = ask_player(player, stones)
            print("")

def check_winner(player, stones):
    if stones <= 0:
        print("Player", player, "wins!")
        return True
    else:
        print("There are", stones, "stones left")
        return False

def ask_player(player, stones):
    answer = int(
        input("Player " + str(
            player) + " would you like to remove 1 or 2 stones? "))
    while answer != 1 and answer != 2:
        answer = int(input("Please enter 1 or 2: "))
    stones = stones - answer
    return stones






def main():
    stones = 20
    while stones > 0:
        stones = ask_player_1(stones)
        if stones > 0:
            stones = ask_player_2(stones)


def ask_player_1(stones):
    print("There are", stones, "stones left")
    answer_1 = int(input("Player 1 would you like to remove 1 or 2 stones? "))
    if answer_1 == 1 or answer_1 == 2:
        stones1 = stones - answer_1
    while answer_1 != 1 and answer_1 != 2:
        answer_1 = int(input("Please enter 1 or 2: "))
    stones1 = stones - answer_1
    if stones1 <= 0:
        print("")
        print("Player 2 wins!")
    else:
        print("")
        print("There are", stones1, "stones left")
    return stones1


def ask_player_2(stones1):
    answer_2 = int(input("Player 2 would you like to remove 1 or 2 stones? "))
    if answer_2 == 1 or answer_2 == 2:
        stones = stones1 - answer_2
    while answer_2 != 1 and answer_2 != 2:
        answer_2 = int(input("Please enter 1 or 2: "))
    stones = stones1 - answer_2
    if stones <= 0:
        print("")
        print("Player 1 wins!")
    print("")
    return stones


main()

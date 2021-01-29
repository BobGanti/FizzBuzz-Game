# FizzBuzz Game
# returns Fizz if input is divisible by 3
# returns Buzz if input is divisible by 5
# returns FizzBuzz if input is divisible by 3 and 5
# game over if input is not divisible by neither 3 nor 5

# --- checking for integer and boundaries ------------------------------------------ #
def isValidNum(num, limit):
    try:
        return int(num)           
    except ValueError: 
        return None


def settings(num, limit):
    response = isValidNum(num, limit)
    while response == None:
        print(f"Number should be +ve integer not less than {limit}!")
        response = isValidNum(input(f"Enter a number again (+ve integer not less than {limit}): "), limit)
    return response

def fizzBuzz(input):
    num = settings(input, 1)
    if (num % 3 == 0) and (num % 5 == 0):
        print("FizzBuzz")
        return 2
    elif (num % 3 == 0):
        print("Fizz")
        return 1
    elif (num % 5 == 0):
        print("Buzz")
        return 1
    else:
        return None

def playGame():
    print("IF DIVISIBLE BY 3 SCORES 1 POINT, DISPLAYS 'Fizz'."
          "\nIF DIVISIBLE BY 5 SCORES 1 POINT & DISPLAYS 'Buzz'"
          "\nIF DIVISIBLE BY 3 AND 5 SCORES 2 POINTS, DISPLAYS 'FizzBuzz'")

    playerList = []
    scoreList = []
    numPlayers = settings(input("\nEnter number of Players (+ve integer above 0): "), 0)

    for i in range(1, numPlayers+1):
        player = input(f"Enter name of player {i}: ")
        playerList.append(player)
        scoreList.append(0)

    for i in range(len(playerList)):
        print(f"\n{playerList[i]} IS PLAYING NOW")
        num = input("Enter a number to cheCk (+ve integer not less than 1): ")
        res = fizzBuzz(num)
        if res != None:
            scoreList[i] += res
        while res != None:
            num = input(f"Enter a number to chek (+ve integer not less than 1): ")
            res = fizzBuzz(num)
            if res != None:
                scoreList[i] += res

    print("*" * 60)

    winnerList = []
    maxScore = max(scoreList)
    for i in range(len(scoreList)):
        if scoreList[i] == maxScore:
            winnerList.append(playerList[i])

    if numPlayers > 1:
        if len(winnerList) > 1:
            print("\nDRAW GAME FOR THE FOLLOWING:")
            for i in range(len(winnerList)):
                print(winnerList[i])
        else:
            print(f"\nThe Winner is {winnerList[0]}")

        for i in range(len(playerList)):
            print(f"{playerList[i]}: {scoreList[i]} Points")

    else:
        print(f"\n{winnerList[0]},  You scored {scoreList[0]} Points")

playGame()
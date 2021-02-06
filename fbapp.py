

#--- checking for integer and boundaries ------------------------------------------ #
def isValidInput(num, limit):
    try:
        if int(num) >= limit:
            return int(num)
    except ValueError:
        return None

# *** Access colors in Dictionary *****
def colors(color):
    colorDict = {
        "black": "\u001b[30m",
        "red": "\u001b[31m",
        "green": "\u001b[32m",
        "yellow": "\u001b[33m",
        "blue": "\u001b[34m",
        "magenta": "\u001b[35m",
        "cyan": "\u001b[36m",
        "gray": "\u001b[37m",
        "reset": "\u001b[0m"
    }
    return colorDict.get(color)

# *** Access colors in a static class
class Colors:
    black = "\u001b[30m"
    red = "\u001b[31m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    blue = "\u001b[34m"
    magenta = "\u001b[35m"
    cyan = "\u001b[36m"
    gray = "\u001b[37m"
    reset = "\u001b[0m"

def settings(num, limit):
    response = isValidInput(num, limit)
    while response == None:
        print(f"{colors('red')} Number should be integer not less than {limit}! {colors('reset')}")
        response = isValidInput(input(f"Enter a number again (integer not less than {limit}): "), limit)
    return response

def fizzBuzz(num, list):
    if num not in list:
        if (num % 3 == 0) and (num % 5 == 0):
            print(f"{colors('yellow')} FizzBuzz {colors('reset')}")
            return 2
        elif (num % 3 == 0):
            print(f"{colors('yellow')} Fizz {colors('reset')}")
            return 1
        elif (num % 5 == 0):
            print(f"{colors('yellow')} Buzz {colors('reset')}")
            return 1
        else:
            print(f"{colors('red')}TIME's UP! {num} is not divisible {colors('reset')}")
            return None
    else:
        print(f"{colors('red')} TIME's UP! You already played {num} {colors('reset')}")
        return None

def playGame():
    print(f"""{colors('gray')}IF DIVISIBLE BY 3 SCORES 1 POINT, DISPLAYS 'Fizz'.
                              IF DIVISIBLE BY 5 SCORES 1 POINT & DISPLAYS 'Buzz'
                              IF DIVISIBLE BY 3 AND 5 SCORES 2 POINTS, DISPLAYS 'FizzBuzz'
       {colors('reset')} """)

    playerList = []
    scoreList = []
    playedNumList = []
    startNum = settings(input("Enter start of range  to FizzBuzz (integer above 0): "), 1)
    numPlayers = settings(input("Enter number of Players (integer above 0): "), 1)

    for i in range(1, numPlayers+1):

        # Ternary operation ==> create surfix for i(example: if i=1, surfix = 1st; i=2, surfix = nd)
        surfix = (i==1) * "st" + (i==2) * "nd" + (i==3) * "rd" or "th"
        player = input(f"Enter name of {i}{surfix} player: ")
        playerList.append(player)
        scoreList.append(0)
        playedNumList.append([])

    for i in range(len(playerList)):
        print(f"\n{colors('cyan')}{playerList[i]} IS PLAYING NOW {colors('reset')}")
        num = settings(input(f"Enter a number to check (integer not less than {startNum}): "),
                       startNum+1)
        res = fizzBuzz(num, playedNumList[i])
        if res is not None:
            scoreList[i] += res
            playedNumList[i].append(num)

        while res is not None:
            num = settings(input(f"Enter a number to check (integer not less than {startNum}): "), startNum + 1)
            res = fizzBuzz(num, playedNumList[i])
            if res is not None:
                scoreList[i] += res
                playedNumList[i].append(num)

    print("-" * 60)
    print(F"\n{colors('cyan')}*** SCRORE BOARD ***{colors('reset')}")
    winnerList = []
    maxScore = max(scoreList)
    for i in range(len(scoreList)):
        if scoreList[i] == maxScore:
            winnerList.append(playerList[i])

    if numPlayers > 1:
        if len(winnerList) > 1:
            print(f"\n{colors('blue')} DRAW GAME FOR THE FOLLOWING:{colors('reset')}")
            for i in range(len(winnerList)):
                print(winnerList[i])
        else:
            print(f"\n{colors('magenta')}The Winner is {winnerList[0]} {colors('reset')}")

        for i in range(len(playerList)):
            print(f"\n{playerList[i]}: {scoreList[i]} Points")
            print(f"Played: {playedNumList[i]}")
    else:
        print(f"\n{colors('magenta')}{winnerList[0]}, You scored {scoreList[0]} Points {colors('reset')}")
        print(f"Played: {playedNumList[0]}")

playGame()

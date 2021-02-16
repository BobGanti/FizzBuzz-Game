
def colors(color):
    colorDict = {
        "red": "\u001b[31m",
        "yellow": "\u001b[33m",
        "cyan": "\u001b[36m",
        "magenta": "\u001b[35m",
        "gray": "\u001b[37m",
        "reset": "\u001b[0m"
    }
    return colorDict[color]

def isValidInput(num, limit):
    try:
        intNum = int(num)
        if intNum >= limit:
            return intNum
    except ValueError:
        return None

def setup(num, limit):
    response = isValidInput(num, limit)
    while response is None:
        print(f"{colors('red')}Number should be an integer not less than {limit}: {colors('reset')}")
        response = isValidInput(input(f"Enter a number again (integer not less than {limit}): "), limit)
    return response

def fizzBuzz(num, list):
    if num not in list:
        if num % 3 == 0 and num % 5 == 0:
            print(f"{colors('yellow')} FizzBuzz {colors('reset')}")
            return 3
        if num % 3 == 0:
            print(f"{colors('yellow')} Fizz {colors('reset')}")
            return 1
        if num % 5 == 0:
            print(f"{colors('yellow')} Buzz {colors('reset')}")
            return 1
        else:
            print(f"{colors('red')} TIME's UP! {num} IS NOT A MULTIPLE OF 3 OF 5 {colors('reset')}")
            return None
    else:
        print(f"{colors('red')} TIME's UP! YOU ALREADY PLAYED {num} {colors('reset')}")

def playGame():
    print(f"""{colors('gray')}
        IF INPUT IS A MULTIPLE OF 3, PLAYER SCORES 1 POINT & PROGRAM DISPLAYS 'Fizz'.
        IF INPUT IS A MULTIPLE OF 5, PLAYER SCORES 1 POINT & PROGRAM DISPLAYS 'Buzz'.
        IF INPUT IS A MULTIPLE 3 AND 5, PLAYER SCORES 2 POINTS & PROGRAM DISPLAYS 'FizzBuzz'
        BUT IF INPUT IS NOT A MULTIPLE, THE PLAYER LOSES TURN TO PLAY
        AND IF THE INPUT IS A REPEAT, THE PLAYER LOSES TURN TO PLAY
           {colors('reset')} """)

    playedNums = []
    scoreList = []
    playerList = []
    startNum = setup(input("Enter start of range: "), 1)
    numPlayers = setup(input("Enter number of players: "), 1)

    count = 1
    while count <= numPlayers:
        # ***** Ternary expressions ( var = val1 if (condition) else val2 ) *****
        # setting surfix Ex. 1st, 2nd, 3rd, 4th, .... 21st 22nd
        surfix = "st" if count % 10 == 1 and count != 11 \
            else ("nd" if count % 10 == 2 and count != 12
            else ("rd" if count % 10 == 3 and count != 13
            else "th"))

        text = f"{count}{surfix}" if numPlayers > 1 else ""

        playerName = input(f"Enter the name of {text} player: ")
        playerList.append(playerName)
        scoreList.append(0)
        playedNums.append([])
        count += 1

    for i in range(numPlayers):
        # Display current player's session
        print(f"\n{colors('cyan')} {playerList[i]} IS PLAYING NOW {colors('reset')}")
        num = setup(input("Enter a number for FizzBuzz: "), startNum)
        response = fizzBuzz(num, playedNums)
        if response is not None:
            scoreList[i] += response
            playedNums[i].append(num)

        while response is not None:
            num = setup(input("Enter a number for FizzBuzz: "), startNum)
            num = int(num)
            response = fizzBuzz(num, playedNums[i])
            if response is not None:
                scoreList[i] += response
                playedNums[i].append(num)

    print("-" * 60)

    print(f"\n{colors('cyan')} ***** SCORE BOARD ***** {colors('reset')}")
    winnerList = []
    maxScore = max(scoreList)

    for i in range(len(scoreList)):
        if scoreList[i] == maxScore:
            winnerList.append(playerList[i])

    if numPlayers > 1:
        if len(winnerList) > 1:
            print(f"{colors('yellow')} DRAW GAME FOR THE FOLLOWING: {colors('reset')}")
            for i in range(len(winnerList)):
                print(f"{winnerList[i]} WITH {scoreList[playerList.index(winnerList[i])]} POINTS")
        else:
            print(f"{colors('yellow')} THE WINNER IS \n{colors('reset')}{winnerList[0]} WITH {scoreList[playerList.index(winnerList[0])]} POINTS")

        for i in range(len(playerList)):
            print(f"\n{colors('magenta')} {playerList[i]}: scores {scoreList[i]} Points {colors('reset')}")
            print(f"Played: {playedNums[i]}")
    else:
        print(f"\n{winnerList[0]} You scored {scoreList[0]} Points")
        print(f"Played: {playedNums[0]}")

playGame()

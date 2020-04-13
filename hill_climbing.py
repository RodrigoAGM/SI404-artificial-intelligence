###################################################################
#Hill climbing algorithm applied to solve a simple 3x3 sort puzzle#
###################################################################


import random

solved = "1238*4765"

def getHeuristic(first:str, second:str):
    counter = 0
    index = 0

    for c in first:
        if c != second[index] and c != "*":
            counter = counter+1

        index = index+1
    
    return counter

def getNMovements(pos:int):
    if pos == 4:
        return 4
    elif pos % 2 == 0:
        return 2
    else:
        return 3
    
def moveCharacter(x:str, pos:int, movement:str):

    lst = list(x)

    if movement == "U":
        lst[pos], lst[pos-3] = lst[pos-3], lst[pos]
    elif movement == "D":
        lst[pos], lst[pos+3] = lst[pos+3], lst[pos]
    elif movement == "R":
        lst[pos], lst[pos+1] = lst[pos+1], lst[pos]
    else:
        lst[pos], lst[pos-1] = lst[pos-1], lst[pos]
    
    return "".join(lst)

def getPossibleMovements(pos:int):
    movements = []

    if pos > 2:
        movements.append("U")

    if pos < 6:
        movements.append("D")    
    
    if pos % 3 != 0:
        movements.append("L")

    if (pos+1) % 3 != 0:
        movements.append("R")

    return movements

def hillClimbing():

    print("Ingrese el estado inicial: ")
    current = str(input())

    flag = False

    while True:

        if current == solved:
            print("SOLVED")
            print(current)
            break
        print(current)
        bestSet = current
        bestHeuristic = getHeuristic(current, solved)
        pos = current.index("*")

        movements = getPossibleMovements(pos)
        print(movements)
        for mov in movements:
            result = moveCharacter(current, pos, mov)
            resultHe = getHeuristic(result, solved)

            if  resultHe <= bestHeuristic:

                if bestHeuristic == resultHe:
                    #Probability for movements with the same heuristic
                    if random.randint(1,50) < 25:
                        bestSet = result
                        bestHeuristic = resultHe
                        #We found at least 1 better set
                        flag = True
                else:  
                    bestSet = result
                    bestHeuristic = resultHe
                    #We found at least 1 better set
                    flag = True
            
        if flag:
            flag = False
            current = bestSet
        else:
            print("No solution found with this initial set")
            break

hillClimbing()
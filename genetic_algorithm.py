###################################################################
##### Genetic algorithm applied to solve the N-Queens problem #####
###################################################################

import random

N = 8
INIT_POP = 4
MUTATION_PROB = 10

def maxAttacks():
    return N*(N-1)/2

def getRandomBetween(minVal, maxVal):
    return random.randint(minVal, maxVal)

def fitness(gen:str):

    attacks = 0
    index = 0

    for g in gen:
        #First we add the horizontal matches 
        attacks = attacks + (gen.count(g)-1)

        #Then we create another for to get diagonal matches
        subindex = 0
        for c in gen:
            #We skip the evaluation for the same column
            if index != subindex:
                coef = abs(index - subindex)
                if int(g) + coef == int(c) or int(g) - coef == int(c):
                    attacks = attacks + 1

            subindex = subindex + 1

        index = index + 1
    
    #Return the fitness result of pair matches 
    return maxAttacks() - (attacks / 2)

def generateGen():
    gen = ""

    for _ in range(N):
        gen = gen + str(random.randint(1,N))

    return gen
    
def calculateSelectionProbabilities(population:list, fitnessValues:list):

    selectionProbabilities = []
    limits = []
    limitSum = 0

    totalFitness = sum(fitnessValues)

    for gen in fitnessValues:
        value = gen/totalFitness
        selectionProbabilities.append(value)
        limits.append(limitSum)
        limitSum = limitSum + value
    
    return selectionProbabilities, limits


def getRandomGen(population:list, limits:list):

    randValue = random.uniform(0,100)
    lastGen = population[0]
    index = 0

    for gen in population:

        if limits[index] > randValue:
            break

        lastGen = gen
        index = index + 1
    
    return lastGen

def reproduce(x:str, y:str):
    c = getRandomBetween(1, N-1)

    child1 = x[0:c] + y[c:] 
    child2 = y[0:c] + x[c:] 

    return child1, child2

def mutate(x:str):
    index = getRandomBetween(0,N-1)
    #print("OldX " + x)
    x = x[0:index] + str(getRandomBetween(1,N)) + x[index+1:]
    #print("NewX " + x)

    return x

def geneticAlgorithm():

    population = []
    fitnessValues = []
    limits = []
    generation = 0

    for _ in range(INIT_POP):  
        gen = generateGen()
        population.append(gen)
        fitnessValues.append(fitness(gen))

    while True:

        print("Genration: ", generation)
        print("Population: ", population)
        print("Values ", fitnessValues)
        _, limits = calculateSelectionProbabilities(population, fitnessValues)

        if maxAttacks() in fitnessValues:
            print("Solution found at generation: " + str(generation))
            print(population[fitnessValues.index(maxAttacks())])
            break

        newPopulation = []
        newfitnessValues = []

        for _ in range(int(INIT_POP/2)):
            x = getRandomGen(population, limits)
            y = getRandomGen(population, limits)
            while x == y:
                y = getRandomGen(population, limits)
            #print("XY values:" + x + "," + y)

            child1, child2 = reproduce(x,y)
            #print(child1 + "," + child2)
            if getRandomBetween(1,100) <= MUTATION_PROB:
                child1 = mutate(child1)
                child2 = mutate(child2)

            
            newPopulation.append(child1)
            newPopulation.append(child2)
            newfitnessValues.append(fitness(child1))
            newfitnessValues.append(fitness(child2))

        population = newPopulation
        fitnessValues = newfitnessValues
        #print(fitnessValues)
        generation = generation + 1
            
random.seed(a=None, version=2)
geneticAlgorithm()
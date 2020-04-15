
import heapq


class priorityQueue:
    def __init__(self):
        self.cities = []

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))

    def pop(self):
        return heapq.heappop(self.cities)[1]

    def isEmpty(self):
        if (self.cities == []):
            return True
        else:
            return False

    def check(self):
        print(self.cities)


class ctNode:
    def __init__(self, city, distance):
        self.city = str(city)
        self.distance = str(distance)


romania = {
    "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
    "Bucharest": {"Fagaras": 211, "Urziceni": 85, "Giurgiu": 90, "Pitesti": 101},
    "Craiova": {"Dobreta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
    "Dobreta": {"Mehadia": 75, "Craiova": 120},
    "Eforie": {"Hirsova": 86},
    "Fagaras": {"Bucharest": 211, "Sibiu": 99},
    "Giurgiu": {"Bucharest": 90},
    "Hirsova": {"Eforie": 86},
    "Iasi": {"Neamt": 87, "Vaslui": 92},
    "Lugoj": {"Timisoara": 111, "Mehadia": 70},
    "Mehadia": {"Dobreta": 75, "Lugoj": 70},
    "Neamt": {"Iasi": 87},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Pitesti": {"Rimnicu Vilcea": 97, "Bucharest": 101},
    "Rimnicu Vilcea": {"Sibiu": 80, "Pitesti": 97},
    "Sibiu": {"Fagaras": 99, "Oradea": 151, "Arad": 140, "Rimnicu Vilcea": 80},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Urziceni": {"Hirsova": 98, "Bucharest": 85},
    "Vaslui": {"Iasi": 92, "Urziceni": 142},
    "Zerind": {"Oradea": 71, "Arad": 75}
}


h = {
    "Arad": 366,
    "Bucharest": 0,
    "Craiova": 160,
    "Dobreta": 242,
    "Eforie": 161,
    "Fagaras": 178,
    "Giurgiu": 77,
    "Hirsova": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 98,
    "Rimnicu Vilcea": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374
}


def heuristic(node, values):
    return values[node]


def astar(start, end):
    path = {}
    distance = {}
    q = priorityQueue()

    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []

    while (q.isEmpty() == False):
        current = q.pop()
        expandedList.append(current)

        if (current == end):
            break

        for new in romania[current]:

            city = new
            city_distance = romania[current][new]
            g_cost = distance[current] + int(city_distance)

            print(city, city_distance, "now : " +
                  str(distance[current]), g_cost)

            if (city not in distance or g_cost < distance[city]):
                distance[city] = g_cost
                f_cost = g_cost + heuristic(city, h)
                q.push(city, f_cost)
                path[city] = current

    printoutput(start, end, path, distance, expandedList)


def printoutput(start, end, path, distance, expandedlist):
    finalpath = []
    i = end

    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()
    print("Going from", start, "to ", end)
    print("=======================================================")
    print("The shortest route is\t: " + str(finalpath))
    print("The amount of cities visited is \t\t: " + str(len(finalpath)))
    print("Total distance \t\t\t\t: " + str(distance[end]))


def main():
    src = "Arad"
    dst = "Bucharest"
    # makedict()
    astar(src, dst)


if __name__ == "__main__":
    main()

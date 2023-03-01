import math
import sys
import random

Q_LIMIT = 100
BUSY = 1
IDLE = 0

# Global variables
simulationTime = 0.0
serverStatus = IDLE
numInQueue = 0
timeLastEvent = 0.0
numCustomersDelayed = 0
totalOfDelays = 0.0
areaNumInQueue = 0.0
areaServerStatus = 0.0
timeNextEvent = [0.0, 0.0,1.0e+30]
timeArrival = [0.0] * (Q_LIMIT + 1)# added this line

# Exponential distribution function
def expon(mean):
    return -mean * math.log((random.random()))

# Initialization function
def initialize():
    global simulationTime, serverStatus, numInQueue, timeLastEvent, numCustomersDelayed, totalOfDelays, areaNumInQueue, areaServerStatus, timeNextEvent, timeArrival

    simulationTime = 0.0
    serverStatus = IDLE
    numInQueue = 0
    timeLastEvent = 0.0
    numCustomersDelayed = 0
    totalOfDelays = 0.0
    areaNumInQueue = 0.0
    areaServerStatus = 0.0
    timeNextEvent = [0.0, 0.0,1.0e+30]
    timeArrival = [0.0] * (Q_LIMIT + 1)
    timeNextEvent[1] = simulationTime + expon(meanInterarrival)

# Timing function
def timing():
    global nextEventType, simulationTime, timeNextEvent

    minTimeNextEvent = 1.0e+29
    nextEventType = 0

    for i in range(0, numEvents):#1,ne+1
        if timeNextEvent[i] < minTimeNextEvent:
            minTimeNextEvent = timeNextEvent[i]
            nextEventType = i + 1

    if nextEventType == 0:
        sys.stderr.write("Event list empty at time %f\n" % simulationTime)
        sys.exit(1)

    simulationTime = minTimeNextEvent

# Arrival event function
def arrive():
    global serverStatus, numInQueue, timeNextEvent, totalOfDelays, numCustomersDelayed, areaNumInQueue, timeArrival

    timeNextEvent[0] = simulationTime + expon(meanInterarrival)

    if serverStatus == BUSY:
        numInQueue += 1

        if numInQueue > Q_LIMIT:
            print("error")

        # Update the arrival time of the customer that just arrived in the queue
        timeArrival[numInQueue] = simulationTime
    else:
        delay = 0.0
        totalOfDelays += delay
        numCustomersDelayed += 1
        serverStatus = BUSY
        timeNextEvent[1] = simulationTime + expon(meanService)

# Departure event function
def depart():
    global serverStatus, numInQueue, timeNextEvent, totalOfDelays, numCustomersDelayed, areaNumInQueue, areaServerStatus, timeArrival

    if numInQueue == 0:
        serverStatus = IDLE
        timeNextEvent[1] = 1.0e+30
    else:
        numInQueue -= 1
        delay = simulationTime - timeArrival[1]
        totalOfDelays += delay
        numCustomersDelayed += 1
        timeNextEvent[1] = simulationTime + expon(meanService)

        #timeArrival.pop(0)
        timeArrival.append(0.0)

def update_time_avg_stats():
    global areaNumInQueue, areaServerStatus, timeLastEvent

    timeSinceLastEvent = simulationTime - timeLastEvent
    areaNumInQueue += numInQueue * timeSinceLastEvent
    areaServerStatus += serverStatus * timeSinceLastEvent
    timeLastEvent = simulationTime


# with open("mm1.in", "r") as infile:
#     line = infile.read()
# # turn to float
# listOfInputs = line.split()
# self.mean_interarrival = float(listOfInputs[0])
# self.mean_service = float(listOfInputs[1])
# self.num_delays_required = int(listOfInputs[2])

def main():
    global numEvents, meanInterarrival, meanService

    # Set the simulation parameters
    numEvents = 2
    with open("input_file.txt", "r") as f:
        line = f.read()
        listOfInputs = line.split()
        delaysRequired = int(listOfInputs[2])
        meanInterarrival = float(listOfInputs[0])
        meanService = float(listOfInputs[1])
    # Initialize the simulation
    initialize()

    while numCustomersDelayed < delaysRequired:
        timing()
        update_time_avg_stats()

        if nextEventType == 1:
            arrive()
        elif nextEventType == 2:
            depart()
    with open('output_file.txt', 'w') as f:
        f.write("Single-server queuing system.\n")
        f.write("Mean interarrival time:\n".format(meanInterarrival))
        f.write("Mean Service Time:\n".format(meanService))
        f.write("Number of customers served:\n".format(delaysRequired))
        f.write("Average delay in queue: {:.3f} minutes\n".format(totalOfDelays / numCustomersDelayed))
        f.write("Average number in queue: {:.3f}\n".format(areaNumInQueue / simulationTime))
        f.write("Server utilization: {:.3f}\n".format(areaServerStatus / simulationTime))
        f.write("Time simulation ended: {:.3f} minutes\n".format(simulationTime))
main()

import random
class Simulation():
    def __init__(self):
        self.Q_LIMIT = 100
        self.BUSY = 1
        self.IDLE = 0

        self.next_event_type = 0
        self.num_custs_delayed = 0
        self.num_delays_required =0
        self.num_events = 0
        self.num_in_q = 0
        self.server_status = self.IDLE

        self.area_num_in_q = 0.0
        self.area_server_status = 0.0
        self.mean_interarrival = 0.0
        self.mean_service = 0.0
        self.sim_time = 0.0
        self.time_arrival =[0.0]*101#********
        self.time_last_event = 0.0
        self.time_next_event = [0]*3
        self.total_of_delays = 0.0
    def mainfunc(self):
        self.num_events =2
        with open("mm1.in", "r") as infile:
            line = infile.read()
        # turn to float
        listOfInputs = line.split()
        self.mean_interarrival = float(listOfInputs[0])
        self.mean_service = float(listOfInputs[1])
        self.num_delays_required = int(listOfInputs[2])

        with open("mm1.out", 'w') as outfile:
            outfile.write(
                f"Single Server Queuing System\n\nMean interarrival time: {self.mean_interarrival}\nMean Service time: {self.mean_service}"
                f"\nNumber of Customers: {self.num_delays_required} ")
        self.initialize()
        while self.num_custs_delayed < self.num_delays_required:
            self.timing()
            self.update_time_avg_stats()
            if self.next_event_type == 1:
                self.arrive()
            elif self.next_event_type == 2:
                self.depart()
        self.report()

    def initialize(self):
        self.sim_time = 0.0
        self.server_status = self.IDLE
        self.num_in_q = 0
        self.time_last_event = 0.0
        self.num_custs_delayed = 0
        self.total_of_delays = 0.0
        self.area_num_in_q = 0.0
        self.area_server_status = 0.0
        a= self.sim_time + self.expon(self.mean_interarrival)
        b = 10**30
        self.time_next_event =[0,a,b]
    def expon(self,mean):
        return -mean* random.random()
    def timing(self):
        min_time_next_event = 10**29 #initialize before? put self or not
        self.next_event_type = 0
        for i in range(self.num_events):
            if self.time_next_event[i] < min_time_next_event:
                min_time_next_event = self.time_next_event[i]
                self.next_event_type = i
        if(self.next_event_type == 0):
            with open("mm1.out", 'w') as outfile:
                outfile.write(f"Event list is empty at time {self.sim_time}")  # ------->why even though sim time is global?
        self.sim_time = min_time_next_event
    def arrive(self):
        self.time_next_event[1] = self.sim_time + self.expon(self.mean_interarrival)
        if self.server_status == self.BUSY:
            self.num_in_q +=1
            if self.num_in_q > self.Q_LIMIT:
                with open("mm1.out", 'w') as outfile:
                    outfile.write(f"Overflow of the array time_arrival at  {self.sim_time} and number = {self.num_in_q}")
            with open("mm1.out", 'w') as outfile:
                outfile.write(f" length of time arrival array is {len(self.time_arrival)} and number in q = {self.num_in_q}")

            self.time_arrival[self.num_in_q] = self.sim_time #length of arrival array = 100 and numinq is 100 be 0
        else:
            delay = 0.0
            self.total_of_delays +=delay
            self.num_custs_delayed +=1
            self.server_status = self.BUSY
            self.time_next_event[2] = self.sim_time + self.expon(self.mean_service)
    def depart(self):
        if self.num_in_q == 0:
            self.server_status = self.IDLE
            self.time_next_event[2] = 10**30
        else:
            self.num_in_q -= 1
            delay = self.sim_time - self.time_arrival[1]
            self.total_of_delays += delay
            self.num_custs_delayed +=1
            self.time_next_event[2] = self.sim_time + self.expon(self.mean_service)
            for i in range(self.num_in_q):
                self.time_arrival[i] = self.time_arrival[i + 1]
    def report(self):
            with open("mm1.out", 'w') as outfile:
                outfile.write(
                f"Average delay in queue  {self.total_of_delays / self.num_custs_delayed}\nAverage number in queue: {self.area_num_in_q / self.sim_time}"
                f"Server Utilization: {self.area_server_status / self.sim_time}\n Time Simulation: {self.sim_time} minutes")
    def update_time_avg_stats(self):
        time_since_last_event = self.sim_time - self.time_last_event
        self.time_last_event = self.sim_time
        self.area_num_in_q += self.num_in_q  * time_since_last_event
        self.area_server_status += self.server_status * time_since_last_event

print("testing main func")
test = Simulation()
test.mainfunc()

print("testing main func2")
#expon,min-time-next-event,time-since-last,put time of arrival at 0 not 100?

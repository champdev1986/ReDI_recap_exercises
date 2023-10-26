import random

class Train:
    def __init__(self, num_wagons, direction):
        self.num_wagons = num_wagons
        self.direction = direction
    
    def go(self):
        print(f"Train is going {self.direction}")
    
    def specifications(self):
        print(f"Train specifications:\n\tNumber of wagons: {self.num_wagons}\n\tTrain direction: {self.direction}")
    
    @staticmethod
    def average_speed(time, distance):
        avg_speed = distance/time
        return avg_speed

class StopLight:
    def __init__(self, state="Red"):
        self.state = state
    
    def change_state(self):
        if self.state == "Red":
            self.state = "Green"
        else:
            self.state = "Red"
    
    def get_state(self):
        return self.state

class Station:
    def __init__(self, name, train1: Train, train2: Train, stoplight1, stoplight2):
        self.name = name
        self.train1 = train1
        self.train2 = train2
        self.stoplight1 = StopLight()
        self.stoplight2 = StopLight("Green")
    
    def change_light_state(self):
        # if self.stoplight1.get_state() == "Red":
        #     self.stoplight1.state == "Green"
        #     self.stoplight2.state == "Red"
        # else:
        #     self.stoplight1.state == "Red"
        #     self.stoplight2.state == "Green"

        self.stoplight1.change_state()
        self.stoplight2.change_state()
        print("New state:\n\tStoplight1 = " + self.stoplight1.get_state() + "\n\tStoplight2 = " + self.stoplight2.get_state())
        # print("New state:\n\tStoplight1 = {self.stoplight1.get_state()}\n\tStoplight2 = {self.stoplight2.get_state()}")

    
    def random_train_go(self, stopLight: StopLight):
        if(stopLight.get_state()== "Red"):
            print("The station is occupied")
        else: 
            if(random.randint(1,2)==1):
                self.train1.go() 
            else:
                self.train2.go()
            self.change_light_state()
    
    @staticmethod
    def join_trains(trainA: Train, trainB: Train):
        joined_train = Train(trainA.num_wagons+trainB.num_wagons, "West")
        return joined_train
    
trainA = Train(2, "East")
trainB = Train(3, "South")

trainA.specifications()
trainB.specifications()

main_station = Station("MarienPlatz", trainA, trainB)
stoplight = StopLight()

main_station.random_train_go(stoplight)





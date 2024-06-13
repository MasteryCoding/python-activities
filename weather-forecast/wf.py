import random
import math
import statistics 

class Weather:
    def __init__ (self,name,temperature):
        self.name = name
        self.temperature = temperature
		
    def fluc_simulator(self): 
        simulated_data = []

        for temp in self.temperature:
            fluctuation = random.uniform(-3,3)
            simulated_temp = temp + fluctuation 
            simulated_data.append(simulated_temp)

        return simulated_data 

    def cal_statistics(self):
        data = self.fluc_simulator()
        avg_temp = statistics.mean(data)
        dev = statistics.stdev(data) 
        
        return math.floor(avg_temp), math.floor(dev)

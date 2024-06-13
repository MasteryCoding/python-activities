import random
import math
import statistics 

newYork = [75, 78, 80, 82, 79, 77, 76, 74, 72, 70, 68, 65, 63, 61, 60, 62, 65, 68, 71, 73, 75, 77, 79, 80, 82, 84, 86, 88, 90, 91]

def fluc_simulation(data): 
	simulated_data = []
	for temp in data:
		fluctuation = random.uniform(-3,3)
		simulated_temp = temp + fluctuation 
		simulated_data.append(simulated_temp)
	return simulated_data 

def cal_statistics(data):
	avg_temp = statistics.mean(data)
	dev = statistics.stdev(data) 

	return math.floor(avg_temp), math.floor(dev)


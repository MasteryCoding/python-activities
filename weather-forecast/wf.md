# Weather Forecast

## Introduction

In this activity, we are going to write a program that forecasts weather using the data collected by importing 3 modules: `random`, `math`, and `statistics`.

## Overview

### Step 1: Create a Class and its Data  

Let’s start by importing 3 modules to use and creating a class called `Weather` to store the data and functions. The class should contain the following for its data: 
* Name of the location
* Temperature data 

#### Solution

```py
import random
import math
import statistics 

class Weather:
    def __init__ (self, name, temperature):
        self.name = name
        self.temperature = temperature 
```

### Step 2: Weather Fluctuation Simulator

Now we will add a function called `fluc_simulator` inside the class, simulating flunctuations of temperature that takes into account the variations not captured in the data. To do so, we will: 

* Create a new list to store simulated data 
* Use `random` module to generate random fluctuations from -3 to 3
* Add fluctuations to each temperature from the data 
* Store the simulated data into the list and return the list

* hint: 
    * Look for a function in `random` module that generates random floats in a given range  

#### Solution

```py
def fluc_simulator(self): 
	simulated_data = []

	for temp in self.temperature:
		fluctuation = random.uniform(-3,3)
		simulated_temp = temp + fluctuation 
		simulated_data.append(simulated_temp)

	return simulated_data 
```

#### Test Code

If it makes sense for the activity to have test code you can provide the code here:

```py
newYork = Weather("New York", [75, 78, 80, 82, 79, 77])
print(newYork.fluc_simulator())
```

When you run the code, you should see the list of floats generated on your screen like following: 

```py
[77.48256207541884, 78.98458988230598, 80.71239102930222, 81.13580915646887, 77.11160645768278, 75.5871245728463] 
```
(Students can have different numbers)

### Step 3: Calculate Statistics   

Using the output from above, let’s predict the temperature and its potential deviation. We will create a function called `cal_statistics` inside the class that does the following: 

* Assign the output of the weather fluctuation simulator to a list
* Calculate the average temperature of the list using `statistics` module
* Calculate the standard deviation of the list for temperature deviation using `statistics` module
* Return the rounded average temperature and its deviation using `math` module

#### Solution

```py
def cal_statistics(self):
    data = self.fluc_simulator()
    avg_temp = statistics.mean(data)
    dev = statistics.stdev(data) 

    return math.floor(avg_temp), math.floor(dev)
```

#### Test Code

If it makes sense for the activity to have test code you can provide the code here:

```py
newYork = Weather("New York", [75, 78, 80, 82, 79, 77])
print(newYork.cal_statistics())
```
(Students can have different location name for the argument)

When you run the code, you should see two integers on your screen like following: 

```py
(77, 3)
```
(Students can have different numbers)

## Conclusion

There we have our weather forecaster! 
Try forecasting the weather by creating instances of the `Weather` class.

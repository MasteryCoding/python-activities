# Weather Forecast

## Introduction

In this activity, we are going to write a program that forecasts weather using the data collected by importing 3 modules: `random`, `math`, and `statistics`.

## Overview

### Step 1: Data Collection

Let’s start by collecting the data we’ll be using for the forecast. Choose any location and search the temperature record of the location for the last 30 days. 

Then import the modules and store the data you collected in a list. 

#### Solution

```py
import random
import math
import statistics 

newYork = [75, 78, 80, 82, 79, 77, 76, 74, 72, 70, 68, 65, 63, 61, 60, 62, 65, 68, 71, 73, 75, 77, 79, 80, 82, 84, 86, 88, 90, 91]
```
(Students can have different location and data)

### Step 2: Simulate Weather Fluctuation

Now we will create a function called `fluc_simulation`that will simulate changes of temperature to take into account the variations not captured in the data. To do so, we will: 

* Use `random` module to generate random fluctuations
* Take the data as an input
* Create a new list to store simulated data 
* Create random fluctuations using function from `random` module 
* Add fluctuations to each temperature from the data 
* Store the simulated data into the list 

Then we will return the list. 

#### Solution

```py
def fluc_simulation(data): 
	simulated_data = []
	for temp in data:
		fluctuation = random.uniform(-3,3)
		simulated_temp = temp + fluctuation 
		simulated_data.append(simulated_temp)
	return simulated_data 
```

#### Test Code

If it makes sense for the activity to have test code you can provide the code here:

```py
print(fluc_simulation(newYork))
```
(Students can have different location name for the argument)

When you run the code, you should see the list of 30 floats generated on your screen like following: 

```py
[72.65509429749771, 75.83370396990925, 77.47884850709855, 79.14802518983764, 79.97376070921723, 79.45952127026752, 75.04690588119094, 76.81147761490281, 74.34278296140671, 67.82718340622331, 70.70848777612682, 63.7207323414876, 62.727299852117056, 60.258493964890285, 61.35189955361317, 62.831148413193816, 66.28791476442332, 69.33028667253656, 73.09250347949485, 71.88977328640378, 72.74766283729949, 78.9647644892453, 78.82113283038852, 81.46904052540792, 79.19061437840676, 82.57756319462563, 86.94223498264357, 85.92953022628055, 92.06049070798704, 90.24648508517805] 
```
(Students can have different numbers)

### Step 3: Calculate Statistics   

Using the simulated data above, let’s predict the temperature and its potential deviation. We will create a function called `cal_statistics` that does the following: 

* Take simulated data as an input
* Calculate the average temperature of the input using `statistics` module
* Calculate the standard deviation of the input for deviation using `statistics` module
* Return the rounded number of average temperature and its deviation using `math` module

#### Solution

```py
def cal_statistics(data):
	avg_temp = statistics.mean(data)
	dev = statistics.stdev(data) 

	return math.floor(avg_temp), math.floor(dev)
```

#### Test Code

If it makes sense for the activity to have test code you can provide the code here:

```py
print(cal_statistics(newYork))
```
(Students can have different location name for the argument)

When you run the code, you should see two integers on your screen like following: 

```py
(75, 8)
```
(Students can have different numbers)

## Conclusion

There we have our weather forecaster! 
Try forecasting the weather by running functions using the data from Step 1 and those of other locations as well.

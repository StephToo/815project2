import random

# Define the probability distribution with two configurable parameters
# https://www.programiz.com/python-programming/if-elif-else

def probability_distribution(parameter1, parameter2, scenario):
    if scenario == 1:
        return random.normalvariate(0, parameter1)
    elif scenario == 2:
        return random.normalvariate(0, parameter2)
    else:
        raise ValueError('Invalid scenario value')

# Define a second probability distribution for the parameter values
#  https://www.geeksforgeeks.org/random-normalvariate-function-in-python/
def parameter_distribution():
    return abs(random.normalvariate(0, 1))

# Simulate the experiment for two different scenarios and save the results to a text file
# https://www.pythontutorial.net/python-basics/python-write-text-file/

with open('simulated_data.txt', 'w') as file:
# https://www.geeksforgeeks.org/writing-to-file-in-python/
    # Scenario 1: parameter1 = 2.2, parameter2 = 2.3
    for i in range(2000):
        parameter_value = parameter_distribution()
        result = probability_distribution(2.2, 2.3, 1)
        file.write(str(result) + ',1\n')
    # Scenario 2: parameter1 = 2.0, parameter2 = 3.5
    for i in range(1000):
        parameter_value = parameter_distribution()
        result = probability_distribution(2.0, 3.5, 2)
        file.write(str(result) + ',2\n')



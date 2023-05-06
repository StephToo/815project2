import matplotlib.pyplot as plt

# Load the data from the text file
# https://www.pythontutorial.net/python-basics/python-write-text-file/
with open('simulated_data.txt', 'r') as file:
    data = [line.strip().split(',') for line in file]

# Split the data into two sets based on the scenario number
# https://sparkbyexamples.com/python/python-convert-string-to-float/
# https://stackoverflow.com/questions/6981717/pythonic-way-to-combine-for-loop-and-if-statement
scenario1_data = [float(d[0]) for d in data if d[1] == '1']
scenario2_data = [float(d[0]) for d in data if d[1] == '2']

# Create separate histograms for each scenario
# https://www.geeksforgeeks.org/how-to-plot-two-histograms-together-in-matplotlib/
plt.hist(scenario1_data, bins=50, alpha=0.5, label='Scenario 1')
plt.hist(scenario2_data, bins=50, alpha=0.5, label='Scenario 2')

# Add labels and title to the plot
# https://www.geeksforgeeks.org/how-to-plot-data-from-a-text-file-using-matplotlib/
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Simulated Data')

# Add a legend to the plot
plt.legend()

# Display the plot
plt.show()

import statistics

cremation_costs = [1320, 1052, 1090, 1285, 1570, 995, 1150, 1585, 820, 1195, 1160, 590]

# Calculate the mean (average) cost
mean_cost = statistics.mean(cremation_costs)

# Calculate the median cost
median_cost = statistics.median(cremation_costs)

# Calculate the standard deviation
std_deviation = statistics.stdev(cremation_costs)

print("Mean (average) cost: $", mean_cost)
print("Median cost: $", median_cost)
print("Standard deviation: $", std_deviation)

# US Medical Insurance Costs
# Project goals:
# 1) Determine least expensive region
# 2) Average age of person with one child
# 3) Average BMI by region
import csv
from collections import defaultdict

with open("C:\\Users\\ayamr\\Documents\\Coding\\Python portfolio\\Insurance.csv") as insurance_data:
# Save data into seperate lists for analysis
    reader = csv.DictReader(insurance_data)
    age = []
    sex = []
    bmi = []
    children = []
    smoker = []
    region = []
    charges = []
    for col in reader:
        age.append(col['age'])
        sex.append(col['sex'])
        bmi.append(col['bmi'])
        children.append(col['children'])
        smoker.append(col['smoker'])
        region.append(col['region'])
        charges.append(col['charges'])
    reader2 = csv.DictReader(insurance_data)
# Save data into a list of dictionaries
    for row in reader2:
        data = [row for row in reader2]
# Function to determine least expensive region by average cost of insurance
def least_expensive(r, c):
    charges_float = [float(x) for x in c]
    duplicate_dict={} 
    for i in r:
        duplicate_dict[i]=r.count(i)
    d = defaultdict(float)
    for k, v in zip(r, charges_float):
        d[k] += v
    region_average = {k: d[k]/duplicate_dict[k] for k in d.keys() & duplicate_dict}
    region_average_sorted = {k: v for k, v in sorted(region_average.items(), key=lambda item: item[1])}
    cheapest_region = list(region_average_sorted.keys())[0]
    cheapest_amount = list(region_average_sorted.values())[0]
    pricey_region = list(region_average_sorted.keys())[-1]
    pricey_amount = list(region_average_sorted.values())[-1]
    return ("The cheapest region for health insurance is the " + cheapest_region + " region with an average cost of $" + str(cheapest_amount) + ". The most expensive region is the " + pricey_region + " region with an average cost of $" + str(pricey_amount) +".")
# print(least_expensive(region, charges))







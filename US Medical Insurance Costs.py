# US Medical Insurance Costs
# Project goals:
# 1) Determine least expensive region
# 2) Average age of person with one child
# 3) Compare BMI of smokers vs non smoker
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
def least_expensive():
    charges_float = [float(x) for x in charges]
    duplicate_dict={} 
    for i in region:
        duplicate_dict[i]=region.count(i) # counts number of times a region apears in the data
    d = defaultdict(float)
    for k, v in zip(region, charges_float):
        d[k] += v # create dictionary with regions as keys and amounts as values where the values are total amounts for each unique regions
    region_average = {k: d[k]/duplicate_dict[k] for k in d.keys() & duplicate_dict} # divides the total amount per regions by the number of instances of the regions to get an average
    region_average_sorted = {k: v for k, v in sorted(region_average.items(), key=lambda item: item[1])} # sorts low to high
    cheapest_region = list(region_average_sorted.keys())[0]
    cheapest_amount = list(region_average_sorted.values())[0]
    pricey_region = list(region_average_sorted.keys())[-1]
    pricey_amount = list(region_average_sorted.values())[-1]
    print("The cheapest region for health insurance is the " + cheapest_region + " region with an average cost of $" + str(cheapest_amount) + ". The most expensive region is the " + pricey_region + " region with an average cost of $" + str(pricey_amount) +".")
# least_expensive()
# Function to determine the average age of a person with one child
def one_child_age():
    age_child = list(zip(age,children)) # zipped list of ages and children
    total_age = []
    for index, tuple in enumerate(age_child):
        howold = tuple[0]
        child = tuple[1]
        if child == '1':
            total_age.append(howold)  # adds all ages to total_age list that have a child value of 1
    sum_of_ages = sum(int(i) for i in total_age) 
    avg_age_one_child = sum_of_ages / children.count('1') # divides total ages by total instances of 1 child for average
    print("The average age of a person with one child is " + str(avg_age_one_child) + " years old.")
# one_child_age()

# Function to compare the BMI of smokers versus non smokers
def compare_BMI():
    average_BMI = (sum(float(i) for i in bmi)) / len(bmi)
    smoker_bmi = list(zip(smoker, bmi))
    smoker_bmi_list = []
    non_smoker_bmi_list = []
    for index, tuple in enumerate(smoker_bmi):
        smkr = tuple[0]
        weight = tuple[1]
        if smkr == 'yes':
            smoker_bmi_list.append(weight)
        else:
            non_smoker_bmi_list.append(weight)
    smoker_bmi_avg = sum(float(i) for i in smoker_bmi_list) / len(smoker_bmi_list)
    non_smoker_bmi_avg = sum(float(i) for i in non_smoker_bmi_list) / len(non_smoker_bmi_list)
    print("The average BMI for a smoker is " + str(smoker_bmi_avg) + ". The average BMI for a non smoker is " + str(non_smoker_bmi_avg) + ".")
# compare_BMI()


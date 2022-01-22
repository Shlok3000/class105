from cgitb import reset
import csv

import math

with open("data.csv") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]
print(data)

def mean(data):
    n = len(data)
    total = 0 
    for x in data:
        total += int(x)
    mean = total/n
    return(mean)
print(mean(data))

squared_list = []
for num in data:
    a = int(num) - mean(data)
    a = a**2
    squared_list.append(a)

print(squared_list)
sum = 0
 
for i in squared_list:
    sum = sum+i

result = sum/len(data) - 1

std_deviation = math.sqrt(result)
print(std_deviation)
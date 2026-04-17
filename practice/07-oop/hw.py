import csv

with open("studen.csv") as file:
    reader = csv.reader(file)
    
    f = 0
    q = 0
    
    for row in reader:
        f += int(row[1])
        q += 1
    
print(f / q)
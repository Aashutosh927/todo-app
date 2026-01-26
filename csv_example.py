import csv

with open("weather.csv", 'r') as file:
     data = list(csv.reader(file))

print(data)
country = input("Enter the name of country: ")

for row in data:
    if row[0] == country:
        print(row[1])

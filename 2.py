import csv

n = int(input())

with open('vps.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    print('\n'.join([row[0] for row in reader if int(row[-2]) >= n]))

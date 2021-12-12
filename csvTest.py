import csv
import numpy

with open ("task19.csv", "r") as input:
    rd = csv.reader(input, delimiter=';')
    averageMassOsinki = []
    averageMassBerezki = []
    sumDist = 0
    sumPetrol = 0

    for line in rd:
        if (line[0] == "Дата"):
            continue 

        inf = line[0].split(' ')
        if int(inf[0]) >= 7 and int(inf[0]) <= 9:
            sumDist += float(line[3])

        if line[1] == "Осинки":
            averageMassOsinki.append(float(line[5]))

        if int(inf[0]) >= 1 and int(inf[0]) <= 3:
            sumPetrol+=float(line[4])

        if line[2] == "Березки":
            averageMassBerezki.append(float(line[5]))

    print(sumDist)
    print(numpy.mean(averageMassOsinki))
    print(sumPetrol)
    print(numpy.mean(averageMassBerezki))

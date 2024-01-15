import matplotlib.pyplot as plt
import numpy as np
import csv

def getTransformGraph():
    temperature_deltas = []
    pressure_deltas = []
    with open('./scripts/data1.csv', 'r') as file:
        file = csv.DictReader(file)
        for row in file:    
            temperature_deltas.append(int(row.get('delta T')))
            pressure_deltas.append(float(row.get('delta P')))

    slope, intercept = np.polyfit(temperature_deltas, pressure_deltas, 1)

    abline_values = [slope * i + intercept for i in temperature_deltas]

    print("Slope: ",slope, ", Intercept: ",intercept)

    fig, ax = plt.subplots( nrows=1, ncols=1 )

    ax.scatter(temperature_deltas, pressure_deltas)
    
    ax.plot(temperature_deltas, abline_values,)

    plt.xticks(range(min(temperature_deltas), max(temperature_deltas) + 10, 5))
    
    plt.xlabel('T (°C)')
    plt.ylabel('P (Atm)')

    plt.grid(True)
    
    fig.savefig('./images/plot-1.png')

    plt.close(fig)


getTransformGraph()
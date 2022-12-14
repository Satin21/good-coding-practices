import pandas as pd
from matplotlib import pyplot as plt

def plot_temperatures(temperatures, mean):

    plt.plot(temperatures, "r-")
    plt.xlabel('measurements')
    plt.ylabel('Air temperature (degC)');

    # plot results
    plt.axhline(y=mean, color="b", linestyle="--")
    plt.savefig(str(len(temperatures))+".png", format='png')
    plt.show()
    # plt.clf()

for num_measurements in [25, 100, 500]:
    # read data from file
    data = pd.read_csv("temperatures.csv", nrows=num_measurements)
    temperatures = data["Air temperature (degC)"]

    # compute statistics
    mean = sum(temperatures) / num_measurements

    plot_temperatures(temperatures, mean)



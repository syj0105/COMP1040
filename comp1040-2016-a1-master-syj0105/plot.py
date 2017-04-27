# COMP1040 -- Assignment 1
#
# Plot yearly average temperature data for recording stations.
#
# NOTE: Make sure your project interpreter is configured to use the Anaconda
#       libraries, otherwise the plotting will not work!
#       Go to Preferences -> Project Interpreter and choose the interpreter
#       that mentions `anaconda`.

# Load in all the functions from the data.py file
from data import *

import matplotlib.pyplot as pyplot

#===============================================================================
# Functions for building a plot
# NOTE: You do not need to modify the code below here!
def collect_by_year(readings):
    """
    Returns a dictionary with an entry for each year in readings that is the
    list of temperature readings for that year.
    :param readings: The list of readings to analyse.
    :return: A dictionary of the form { year: [ temps ] }.
    """
    by_year = {}
    for reading in readings:
        year = reading['year']
        if year not in by_year:
            by_year[year] = []
        by_year[year].append(reading['temp'])

    return by_year

def plot_station_by_year(station_id, stat):
    """
    Plots temperature data vs. year for the given station and statistic.

    :param station_id: The BoM station ID to plot
    :param stat: 'max' to plot the maximum temperature, 'min' for minimum.
    """

    readings = get_readings(station_id, stat)
    yearly = collect_by_year(readings)
    if yearly:
        years = list(yearly.keys())
        avg_temps = []

        for year in years:
            temps = yearly[year]
            avg_temps.append(sum(temps)/len(temps))

        station_name = station_id_to_name(station_id)
        pyplot.plot(years, avg_temps)
        pyplot.title("Average yearly {} temperatures in {}".format(stat, station_name))
        pyplot.xlabel("Year")
        pyplot.ylabel("Average Temp. (ºC)")
        pyplot.show()

# NOTE: You do not need to modify the code above here!
#===============================================================================


# This code below is executed when the file is run from PyCharm or the console.
# Try changing the station ID to a different string, for example:
#    Adelaide:      023090
#    Brisbane:      040842
#    Canberra:      070351
#    Darwin:        014015
#    Hobart:        094220
#    Melbourne:     086071
#    Perth:         009021
#    Sydney:        066062
#
# Station IDs for other cities and locations can be found in `stations.txt`.
if __name__ == '__main__':
    plot_station_by_year('070351', 'min')

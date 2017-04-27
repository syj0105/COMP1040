# COMP1040 -- Assignment 1
#
# Constructs a report of the hottest year recorded at a station for every month.

# Read in the functions from data.py
from data import *

# Short names for months
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#===============================================================================
# Functions for building a report
# NOTE: You do not need to modify the code below here!

def hottest_years(station_id):
    """
    Prints the hottest years for each month for the given station ID.

    :param station_id: The station ID to report
    """
    readings = get_readings(station_id, 'max')
    station_name = station_id_to_name(station_id)
    print("Hottest years by month for {}".format(station_name))
    for month_index, month_name in enumerate(MONTHS):
        # Add one to month index since hottest_year expect Jan index to be 1
        year, temp = hottest_year(readings, month_index + 1)
        print("{}: {}ºC in {}".format(month_name, temp, year))

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
    hottest_years('070351')

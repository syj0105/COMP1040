# COMP1040 -- Assignment 1
#
# Data processing of temperature data from the Australian Bureau of Meteorology.
#
# This module contains functions for requesting and processing data from the
# BoM's website. Many of these functions are unfinished or broken and need
# fixing.
#
# Unit tests for these functions can be found in the file `test_data.py`.
#
# Once these functions in this file are working, the code in `plot.py` and
# `report.py` should work correctly.

import csv
import urllib.request
import os.path
import matplotlib.pyplot as pyplot

# BoM climate URL template
BOM_TEMPLATE = 'http://www.bom.gov.au/climate/change/acorn/sat/data/acorn.sat.{0}T.{1}.daily.txt'

##########
# Helper functions

def bom_data_url(station_id  , stat):
    str1 = BOM_TEMPLATE.replace('{1}',str(station_id))   # Use station_id to replace {1} in BOM_TEMPLATE.
    str1 = str1.replace('{0}',stat)                      # Use stat to replace {0} in str1.
    return str1


    """
    Returns the web address for the temperature data of the given type for the
    given station ID.

    :param station_id: The station ID for which to get the data
    :param stat: Whether to get the maximum ('max') or minimum ('min') temps
    :return: A BoM URL for the given station ID and stat parameter
    """
    # FIXME: Currently ignores arguments and always returns same web address. Use the global
    # variable BOM_TEMPLATE as a template for constructing the return string.
    # return 'http://www.bom.gov.au/climate/change/acorn/sat/data/acorn.sat.minT.070351.daily.txt'


def is_missing(value):
    """
    Tests whether the given value represents a missing value (99999.9) or not.
    :param value: The string value to test
    :return: True if the value represents a missing value, False otherwise.
    """
    # FIXME: Currently always returns False. You may want to have a look at the function
    # test_is_missing in 'test_data.py' to see how this function will be tested.
    if value == '99999.9':
        return True
    else:
        return False


def make_reading(date_str, temp_str):
    date_value = parse_date(date_str)    # Change the format of dates.
    return {'year': date_value[0], 'month': date_value[1], 'day': date_value[2],'temp': float(temp_str)}


    """
    Create a dictionary with 'year', 'month', 'day', and 'temp' keys
    from the input date and temperature strings.

    The values for 'year', 'month', and 'day' keys are ints, and the
    value for the 'temp' key is a float.

    :param date_str: String representation of a date in YYYYMMDD format
    :param temp_str: String representing a temperature (in Celsius)
    :return: A dict of the form
            {'year': int, 'month': int, 'day': int, 'temp': float}
    """
    # TODO: Implement the make_reading function


def station_id_to_name(station_id):
    f = open("stations.txt", "r")         # Open stations.txt file.
    while True:
        lines = f.readline()              # Read every line and check if the given string is in the text.
        if lines:
            n = lines.strip().split(',')  # Remove space and separate string by the comma ','.
            if n[0] == station_id:        # Find corresponding station_id.
                f.close()                 # Close the file.
                return n[1]               # Return station_id's name.
        else:
            break
    f.close()
    return None                           # Not find station_id.

    """
    Returns the station name for a given station ID based on the contents
    of the stations.txt file.

    :param station_id: String containing ID for a weather station
    :return: Name associated with the ID in the stations.txt file, or None
             if there is no such station.
    """
    # TODO: Implement station name lookup using stations.txt file


def parse_date(date_str):
    year, mon, day = int(date_str[:4]), int(date_str[4:6]), int(date_str[6:])
    return year, mon, day


    """Given a string with format YYYYMMDD, returns the year, month, and day
    as integers.

    :param date_str: A string representation of a date in YYYYMMDD format.
    :return: A triple of integers (year, month, day)
    """
    # FIXME: Currently returns None instead of triple with year, month, day. return None


def hottest_year(readings, month):
    length = len(readings)                                 # Compute the length of readings.
    return_value = [0, -1000000.0]                         # Define the initial value of the year and temperature.
    for i in range(length):                                # Iterate length times.
        if readings[i]['month'] == month:                  # Find month.
            if readings[i]['temp'] > return_value[1]:      # Search for greater temperatures than before.
                return_value[0] = readings[i]['year']      # Change the value saved before.
                return_value[1] = readings[i]['temp']
            elif readings[i]['temp'] == return_value[1]:
                if readings[i]['year'] > return_value[0]:  # Use the more recent years.
                    return_value[0] = readings[i]['year']
    return return_value[0], return_value[1]



    """
    Finds, for the given month, the year in which that month had the highest
    recorded temperature and returns the year and the temperature.

    In the case of two years having equal highest temperature for a given month,
    the more recent year is used.

    :param readings: List of readings of the form returned by make_reading
    :param month: An integer between 1 and 12 representing the month
    :return: The integer year and float temperature that was most recent and
             hottest for the given month
    """
    # TODO: Implement hottest_year_by_month


#===============================================================================
# Extra functions for downloading and storing data
# NOTE: You do not need to modify the code below here!

# Location where downloaded data files will be stored relative to project.
DATA_DIR = 'cache'

def make_filename(station_id, stat):
    """
    Constructs a filename for caching data based on the station ID and
    temperature type.
    :param station_id: The station ID string
    :param stat: The statistic ('min' or 'max')
    :return: A path for where to store data for the station and statistic.
    """

    return os.path.join(DATA_DIR,"{0}-{1}.txt".format(station_id, stat))


def load_readings(filename):
    """
    Reads data from the named file and converts it to a list of readings
    (represented as dictionaries).
    Missing data in the file are not reported as readings.

    :param file: The BOM data file with temperatures for a specific station
    :return: List of readings (i.e., same as output of make_reading)
    """
    temps = []
    with open(filename) as temperature_data:
        rows = csv.reader(temperature_data, delimiter=' ', skipinitialspace=True)

        for i, row in enumerate(rows):
            if i == 0:
                continue

            date_str = row[0]
            temp_str = row[1]
            if is_missing(temp_str):
                continue

            reading = make_reading(date_str, temp_str)
            temps.append(reading)

    return temps

def save_remote_data(station_id, stat):
    """
    Downloads the given temp_type data for the given station_id and returns
    a local file named `cache/station_id-temp_type.txt` containing the
    downloaded data.

    :param station_id: A string representing the station ID.
    :param stat: A string ('max' or 'min') specifying which statistic to fetch.
    :return: The local filename used to save the temperature data.
    """

    # Create a cache directory if one does not already exist
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    # Fetch and save the temperature data
    url = bom_data_url(station_id, stat)
    filename = make_filename(station_id, stat)
    try:
        urllib.request.urlretrieve(url, filename)
    except urllib.error.URLError as e:
        print("Could not retrieve data for {}-{}.".format(station_id, stat))
        print("Check whether your internet connection is working.")
        print(e.reason)
        os._exit(1)

    return filename


def get_readings(station_id, stat):
    """
    Returns the list of readings for the given station ID and statistic type.

    :param station_id: A string station ID (e.g, '009741')
    :param stat: 'min' or 'max'
    :return: A list of readings for the given station and statistic
    """
    filename = make_filename(station_id, stat)
    if not os.path.exists(filename):
        filename = save_remote_data(station_id, stat)

    return load_readings(filename)

# NOTE: You do not need to modify the code above here!
#===============================================================================


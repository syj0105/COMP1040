#!/usr/bin/env python3
# COMP1040: The Craft of Computing
#
# Functions for processing and displaying traffic events on a map
# of Canberra from the ACTPol_Traffic twitter account.
#
# Modify locations in the code marked FIXME or TODO and run the associated
# unit tests to make sure your code is working. Once the unit tests have
# passed you should run the code in this file to animate the tweet events.
#

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tweet_utils as tu

# --- read_street_locations ----------------------------------------------

def read_street_locations(filename):
    """
    Reads street locations processed from Google Map's geocode API.

    :param filename: name of file with the street locations
    :return: a dictionary of street latitude and longitude locations
        indexed by street name and suburb, e.g.,

        street_locations[("Northbourne Ave", "City")] = (-35.278417, 149.129469)
    """

    street_locations = dict()
    fh = open(filename, "r")
    fh.readline() # skip header line
    for line in fh:
        query_name, returned_name, lat, lon, t, n = line.strip().split("|")
        # ignore if returned_name is None
        if (returned_name == "None"):
            continue

        # TODO: Write code to extract the street and suburb from the
        # `query_name`. 1.Do not include the state and make sure you
        # remove whitespace from around the text. 2.Also extract the
        # latitude and longitude as floats. 3.Add a key-value pair to
        # the `street_locations` dictionary where the key is a tuple
        # of street name and suburb, and the value is a tuple of
        # latitude and longitude coordinates.
        street = query_name.split(',')[0]               # split query by ',', and street is the first item.
        suburb = ' '.join(query_name.split(" ")[:-1]).split(",")[-1].strip()
        street_locations[(street, suburb)] = (eval(lat), eval(lon))  # Convert str object to float type
    fh.close()
    return street_locations

# --- read_map -----------------------------------------------------------

def read_map(resolution):
    """
    Reads a map image and corresponding latitude and longitude extent.

    :param resolution: Resolution of the map (either 'lores' or 'hires'
    :return: A tuple of the map and dictionary of lat/lon limits, e.g.,
        (map, {'lat_min': -10.0, 'lat_max': 10.0, 'lon_min': 120.0, 'lon_max': 122.0})
    """

    map = plt.imread("data/canberraMap_" + resolution + ".jpg")

    limits = {}
    limit = []
    with open("data/canberraMapLatLon_" + resolution + ".txt")as f:
        for li in f.readlines():
            for d in li.strip('\n').split(' '):
                limit.append(eval(d))    # Add d to limit, and convert str object to float type
    limits['lat_max'] = limit[0]         # The first item in limit is lat_max.
    limits['lat_min'] = limit[1]
    limits['lon_min'] = limit[2]
    limits['lon_max'] = limit[3]


    # TODO: Implement code to read the latitude and longitude limits
    # for the map at the given resolution. Place the values into the
    # limits dictionary with the following keys: "lat_min", "lat_max",
    # "lon_min", and "lon_max".

    return (map, limits)

# --- latlon_to_point ----------------------------------------------------

def latlon_to_point(lat, lon, limits):
    """
    Converts latitude and longitude coordinates to approximate (x, y) point.

    :param lat: Latitude for the point of interest
    :param lon: Longitude for the point of interest
    :param limits: Dictionary of minimum and maximum latitude and longitude for the
        map as returned by the read_map function
    :return: A tuple of approximate (x, y) coordinates of the point on the map
        computed by interpolating between latitude and longitude limits
    """

    # TODO: Replace the following code to compute x and y map coordinates by
    # interpolating between latitude and longitude limits. For example, when
    # lon == limits['lon_min'] the x coordinate should be 0, and when lon ==
    # limits['lon_max'] the x coordinate should be 1. Similalry for latitude.

    x, y = 0, 0

    x = (lon - limits['lon_min']) / (limits['lon_max'] - limits['lon_min'])  # Convert lon to 0~1
    y = (lat - limits['lat_min']) / (limits['lat_max'] - limits['lat_min'])  # Convert lat to 0~1

    return (x, y)

# --- animate_tweets -----------------------------------------------------

def animate_tweets(tweet, street_locations, map_image, map_limits):
    """Animate tweets on a map."""

    # TODO: Write code to extract the date/time and message from the
    # tweet. Also normalise the message by applying the conversions
    # defined in tu.CONVERSIONS.

    date_time = None    # FIXME: replace this variable with the correct date/time string
    msg = ""            # FIXME: replace this variable with the normalized message
    date_time = tu.split_tweet(tweet)[0][2:]   # Apply split_tweet in tu to get date_time and msg
    msg = tu.split_tweet(tweet)[1]
    msg = tu.normalize_message(msg,tu.CONVERSIONS)    # Normalize msg

    # YOU DO NOT NEED TO MODIFY ANYTHING BELOW THIS LINE

    # find street mentions
    streets = tu.match_streets(msg, street_locations)
    if not streets:
        return []

    # plot street mentions on the map
    H, W = len(map_image), len(map_image[0])
    ax = plt.gca()
    ax.clear()
    ax.set_axis_off()
    ax.imshow(map_image)

    for street in streets:
        lat, lon = street_locations[street]
        (x, y) = latlon_to_point(lat, lon, map_limits)
        plt.plot(W * x, H * (1 - y), 'ro')
        plt.text(
            W * x, H * (1 - y), street[0] + ", " + street[1] + "\n" + date_time
        )

    return []


# --- main ---------------------------------------------------------------
# YOU DO NOT NEED TO MODIFY ANYTHING BELOW THIS LINE

def main():
    # read street locations
    street_locations = read_street_locations(
        "data/canberraStreetLocations.txt"
    )

    # read map and limits
    map_image, map_limits = read_map("lores")

    # show map
    fig = plt.figure()
    plt.ioff()

    ax = plt.axes([0, 0, 1, 1])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(map_image)

    # open the file of tweets
    with open("data/ACTPol_Traffic", "r") as tweet_fh:
        # start animation
        ani = animation.FuncAnimation(
            fig, animate_tweets, interval=100, repeat=False,
            fargs=(street_locations, map_image, map_limits),
            frames=tweet_fh.readlines()
        )
        plt.show()


if __name__ == "__main__":
    main()

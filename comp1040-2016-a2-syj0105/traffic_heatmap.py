#!/usr/bin/env python3
# COMP1040: The Craft of Computing
#
# Scrtipt for displaying heatmap of traffic events on a map
# of Canberra from the ACTPol_Traffic twitter account.
#
# Modify locations in the code marked FIXME or TODO.
#

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndimage
import tweet_utils as tu
import traffic

# --- create_heat_map ----------------------------------------------------

def create_heat_map(map_limits):
    """
    Creates a heat map of traffic events.

    :param map_limits: latitude and longitude map limits as returned by traffic.read_map
    :return: a 2d numpy array of traffic event counts binned by map location. The array
        can be any size (e.g., 50-by-50) but is assumed to span the map limits.
    """

    # read street locations
    street_locations = traffic.read_street_locations("data/canberraStreetLocations.txt")

    # TODO: Write your code here for creating a heatmap of traffic events from the
    # `data/ACTPol_Traffic` file of tweets. This task is challenging.

    return None

# --- main ---------------------------------------------------------------
# YOU DO NOT NEED TO MODIFY ANYTHING BELOW THIS LINE

def main():
    # read the map and lat/lon extent
    map_image, map_limits =  traffic.read_map("lores")
    greymap = matplotlib.colors.rgb_to_hsv(map_image)[:,:,2]

    # produce a heat map
    heatmap = create_heat_map(map_limits)

    # rescale the heatmap
    zoom = (np.shape(greymap)[0] / np.shape(heatmap)[0], np.shape(greymap)[1] / np.shape(heatmap)[1])
    heatmap = ndimage.interpolation.zoom(heatmap, zoom)
    heatmap -= np.amin(heatmap)
    heatmap /= np.amax(heatmap)

    # merge the heat map with the map of Canberra and show
    red = np.uint8(greymap / 2 + 127 * heatmap)
    blue = np.uint8(greymap / 2)
    green = np.uint8(greymap / 2 + 127 - 127 * heatmap)

    rgb = np.dstack((red, green, blue))

    plt.clf()
    plt.imshow(rgb)
    plt.show()


if __name__ == "__main__":
    main()


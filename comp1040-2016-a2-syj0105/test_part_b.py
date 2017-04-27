#!/usr/bin/env python3
# COMP1040: The Craft of Computing
#
# Test suite for Part B of Assignment 2
#
# These test can be run by right-clicking on the `test_part_b.py` file in the
# Project view in PyCharm and choosing "Run Unittests in test_part_b".
# Individual tests can also be run by selecting then right clicking on a test
# name in this file (e.g., `test_read_map`) and selecting "Run".
#
# NOTE: You should make sure all these tests here are passing before running
#       the code in `traffic.py`.

import unittest
import traffic

# --- tests --------------------------------------------------------------

class TestPartB(unittest.TestCase):

    def test_read_street_locations(self):
        """Checks that street locations can be read successfully from data/canberraStreetLocations.txt"""
        street_locations = traffic.read_street_locations("data/canberraStreetLocations.txt")
        self.assertEqual(street_locations[('Athllon Dr', 'Greenway')], (-35.408366, 149.063385))
        self.assertEqual(street_locations[('Monaro Hwy', 'Hume')], (-35.389207, 149.164727))
        self.assertEqual(street_locations[('North Rd', 'Acton')], (-35.27505, 149.12102))

    def test_read_map(self):
        """Makes sure the read map function returns correct limits."""
        map_image, map_limits =  traffic.read_map("lores")
        self.assertEqual(map_limits['lon_min'], 148.886719)
        self.assertEqual(map_limits['lon_max'], 149.414062)
        self.assertEqual(map_limits['lat_min'], -35.603719)
        self.assertEqual(map_limits['lat_max'], -35.173808)
        map_image, map_limits =  traffic.read_map("hires")
        self.assertEqual(map_limits['lon_min'], 148.930664)
        self.assertEqual(map_limits['lon_max'], 149.370117)
        self.assertEqual(map_limits['lat_min'], -35.496456)
        self.assertEqual(map_limits['lat_max'], -35.173808)

    def test_latlon_to_point(self):
        """Tests latlot_to_point function"""
        map_limits = {'lat_min': -35.603719, 'lon_max': 149.414062, 'lat_max': -35.173808, 'lon_min': 148.886719}
        expected_x = 0.335011558
        expected_y = 0.454403353
        x, y = traffic.latlon_to_point(-35.408366, 149.063385, map_limits)
        self.assertAlmostEqual(x, expected_x, 7)
        self.assertAlmostEqual(y, expected_y, 7)

if __name__ == '__main__':
    unittest.main()

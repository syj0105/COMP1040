# COMP1040 -- Assignment 1
#
# Unit tests for the functions in the file `data.py`.
#
# These test can be run by right-clicking on the `test_data.py` file in the
# Project view in PyCharm and choosing "Run Unittests in test_data".
# Individual tests can also be run by selecting then right clicking on a test
# name in this file (e.g., `test_is_missing`) and selecting the "Run" option.
#
# NOTE: You should make sure all these tests here are passing before running
#       the code in `plot.py` or `report.py`.
import unittest

# Read in the functions implemented in `data.py`
import data

class ConverterTests(unittest.TestCase):
    def test_bom_url(self):
        self.assertEqual(
            'http://www.bom.gov.au/climate/change/acorn/sat/data/acorn.sat.maxT.12345.daily.txt',
            data.bom_data_url('12345', 'max')
        )
        self.assertEqual(
            'http://www.bom.gov.au/climate/change/acorn/sat/data/acorn.sat.minT.54321.daily.txt',
            data.bom_data_url('54321', 'min')
        )

    def test_is_missing(self):
        self.assertTrue(data.is_missing('99999.9'), 'Missing value')
        self.assertFalse(data.is_missing('13'), 'Non-missing value')

    def test_make_reading(self):
        self.assertEqual(
            {'year': 2015, 'month': 7, 'day': 20, 'temp': 12.1},
            data.make_reading("20150720","12.1")
        )
        self.assertEqual(
            {'year': 1990, 'month': 12, 'day': 1, 'temp': 27.5},
            data.make_reading("19901201","27.5")
        )

    def test_station_id_to_name(self):
        self.assertEqual('Canberra',data.station_id_to_name('070351'))
        self.assertEqual('Melbourne Regional Office', data.station_id_to_name('086071'))
        self.assertEqual(None, data.station_id_to_name('000000'))

    def test_parse_date(self):
        self.assertEqual((2015,7,20), data.parse_date("20150720"))
        self.assertEqual((1998,12,25), data.parse_date("19981225"))

    def test_hottest_year(self):
        readings = [
            {'year': 2015, 'month': 7, 'day': 20, 'temp': 12.1},
            {'year': 2015, 'month': 2, 'day': 2, 'temp': 35.0},
            {'year': 2015, 'month': 1, 'day': 17, 'temp': 28.4},
            {'year': 2014, 'month': 7, 'day': 10, 'temp': 24.3},
            {'year': 2014, 'month': 2, 'day': 3, 'temp': 25.1},
            {'year': 2014, 'month': 1, 'day': 7, 'temp': 28.4}
        ]
        # Basic tests
        self.assertEqual((2014,24.3), data.hottest_year(readings, 7))
        self.assertEqual((2015,35.0), data.hottest_year(readings, 2))

        # Check that ties are resolved to most recent year
        self.assertEqual((2015,28.4), data.hottest_year(readings, 1))


if __name__ == '__main__':
    unittest.main()

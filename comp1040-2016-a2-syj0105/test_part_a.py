#!/usr/bin/env python3
# COMP1040: The Craft of Computing
#
# Test suite for Part A of Assignment 2
#
# These test can be run by right-clicking on the `test_part_a.py` file in the
# Project view in PyCharm and choosing "Run Unittests in test_part_a".
# Individual tests can also be run by selecting then right clicking on a test
# name in this file (e.g., `test_normalize_message`) and selecting "Run".
#
# NOTE: You should make sure all these tests here are passing before running
#       the code in `tweet_utils.py` or `traffic.py`.

import unittest
import tweet_utils as tu

# --- tests --------------------------------------------------------------

class TestPartA(unittest.TestCase):

    def test_normalize_message(self):
        """Basic test that the normalize_message function works."""
        msg = "Cowlishaw Street &amp; Athllon Drive, Greenway now free of obstruction."
        expected_msg = "Cowlishaw St and Athllon Dr Greenway now free of obstruction"
        self.assertEqual(tu.normalize_message(msg, tu.CONVERSIONS), expected_msg)

        msg = "Two vehicle collision Monaro Highway Hume southbound near Caltex Service Stn."
        expected_msg = "Two vehicle collision Monaro Hwy Hume southbound near Caltex Service Stn"
        self.assertEqual(tu.normalize_message(msg, tu.CONVERSIONS), expected_msg)

    def test_split_tweets(self):
        """Basic test that the split_tweets function works."""
        tweet = "624876398314819584 2015-07-25 19:38:37 AEST <ACTPol_Traffic> Collision at intersection of Cowlishaw St &amp; Athllon Dr Greenway. Avoid area if possible."
        expected_split = ('2015-07-25 19:38:37', 'Collision at intersection of Cowlishaw St &amp; Athllon Dr Greenway. Avoid area if possible.')
        self.assertEqual(tu.split_tweet(tweet), expected_split)

        tweet = "615792637262467074 2015-06-30 18:03:00 AEST <ACTPol_Traffic> Two vehicle collision Monaro Hwy Hume southbound near Caltex Service Stn.\nExpect possible delays"
        expected_split = ('2015-06-30 18:03:00', 'Two vehicle collision Monaro Hwy Hume southbound near Caltex Service Stn.\nExpect possible delays')
        self.assertEqual(tu.split_tweet(tweet), expected_split)

    def test_read_and_normalize_tweets(self):
        """Test that we can read tweets from the ACTPol_Traffic file and process them."""
        try:
            fh = open("data/ACTPol_Traffic", "r")
            for tweet in fh:
                (date_time, msg) = tu.split_tweet(tweet)
                msg = tu.normalize_message(msg, tu.CONVERSIONS)
            fh.close()
        except:
            self.fail()

    def test_match_streets(self):
        """Test that we can match streets within tweets."""
        street_locations = {
            ('Athllon Dr', 'Greenway'): None,
            ('Monaro Hwy', 'Hume'): None,
            ('North Rd', 'Acton'): None
        }

        msg = "Cowlishaw St and Athllon Dr Greenway now free of obstruction"
        self.assertEqual(tu.match_streets(msg, street_locations), [('Athllon Dr', 'Greenway')])

        msg = "Two vehicle collision Monaro Hwy Hume southbound near Caltex Service Stn"
        self.assertEqual(tu.match_streets(msg, street_locations), [('Monaro Hwy', 'Hume')])

    def test_suburb_histogram(self):
        """Test suburb histogram counts on a small number of cases."""
        h = tu.suburb_histogram("data/ACTPol_Traffic", "data/canberraSuburbs.txt")
        self.assertEqual(h['Flynn'], 15)
        self.assertEqual(h['Red Hill'], 8)
        self.assertEqual(h['Dodsworth'], 0)
        self.assertTrue('Turner' in h)
        self.assertFalse('' in h)
        
if __name__ == '__main__':
    unittest.main()

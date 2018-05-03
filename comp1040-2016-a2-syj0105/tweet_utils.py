#!/usr/bin/env python3
# COMP1040: The Craft of Computing
#
# Utility functions for processing tweets.
#
# Modify locations in the code marked FIXME or TODO and run the associated
# unit tests to make sure your code is working. Once the unit tests have
# passed you should run the code in this file to plot a histogram of suburb
# mentions.
#

import matplotlib.pyplot as plt

# --- constants ----------------------------------------------------------

CONVERSIONS = {"&amp;": "and",
               "Avenue": "Ave", "Av": "Ave",
               "Circle": "Cir",
               "Circuit": "Cct",
               "Close": "Cl",
               "Crescent": "Cres", "Cr": "Cres",
               "Drive": "Dr",
               "Highway": "Hwy",
               "Lane": "Ln",
               "Parade": "Pde",
               "Parkway": "Pkwy",
               "Place": "Pl",
               "Road": "Rd",
               "Street": "St"}

# --- normalize_message --------------------------------------------------

def normalize_message(msg, conversions):
    """
    Removes commas and periods (full stops) and converts various tokens
    into a standard form, such as converting 'Road' to 'Rd'.

    :param msg: The tweet message (string) to normalise
    :param conversions: Dictionary of abbreviation conversions to apply
    :return: A tweet message (string) with conversions applied
    """

    # first eliminate commas and periods from the message
    msg = msg.translate({ord(i): None for i in ".,"})
    
    # break message into list of whitespace separated tokens
    tokens = msg.strip().split(" ")

    # TODO: Implement for each token check whether it should be converted
    # and if so convert it. That is, if a token appears as a key in the
    # `conversions` dictionary then replace it with the corresponding dictionary
    # value.
    for i in range(len(tokens)):
        if tokens[i] in conversions.keys():      # Check if a token appears as a key in the conversions dictionary.
            tokens[i] = conversions[tokens[i]]   # Convert the token to corresponding dictionary value.

    # return the tokens reassembled into a space separated string
    return " ".join(tokens)

# --- split_tweet --------------------------------------------------------

def split_tweet(tweet):
    """
    Extracts the time/date and message from a tweet.

    :param tweet: The full tweet including tweet ID, time stamp, user Id, and message, e.g.,
        '624876398314819584 2015-07-25 19:38:37 AEST <ACTPol_Traffic> Collision at intersection of Cowlishaw St &amp; Athllon Dr Greenway. Avoid area if possible.'
    :return: Tuple containing the time/date and tweet message, e.g.,
        ('2015-07-25 19:38:37', 'Collision at intersection of Cowlishaw St &amp; Athllon Dr Greenway. Avoid area if possible.')
    """

    # TODO: Implement code to split the tweet into the date and time component
    # and message component. The tweet Id and user Id should be ignored.
    tweet_split = tweet.split(" ")              # Split tweet with whitespace
    date_and_time = " ".join(tweet_split[1:3])  # Slice to get date_and_time
    message = " ".join(tweet_split[5:])         # Slice from the sixth item to the end to get message

    return date_and_time, message

# --- match_streets ------------------------------------------------------

def match_streets(tweet_msg, street_locations):
    """
    Finds mentions of all streets within a tweet.

    :param tweet_msg: The tweet message extracted from split_tweet
    :param street_locations: Dictionary of (street, suburb) locations as returned by read_street_locations
    :return: List of (street, suburb) pairs found in the tweet, e.g.,
        [("Northbourne Ave", "City"), ("Athllon Dr", "Greenway")]
    """

    # TODO: Implement this function. Currently the return value is an empty list.
    for key in street_locations.keys():
        if tweet_msg.find(" ".join(key)) != -1:  # Check if tweet_msg contains street_locations key
            return [key]


# --- suburb_histogram ---------------------------------------------------
def suburb_histogram(tweets_filename, suburb_filename):
    """
    Counts the number of times a suburb is mentioned in a collection of tweets.

    :param tweets_filename: The file containing the tweets
    :param suburb_filename: The file containing a list of suburbs
    :return: A dictionary indexed by suburb containing the number of times the suburb was mentioned, e.g.,
        {'Flynn': 15, 'Red Hill': 12}
    """

    # read suburb list
    suburbs = list()
    with open(suburb_filename) as fh:
        for suburb in fh:
            suburbs.append(suburb.strip())

    # initialise histogram
    histogram = dict()
    for suburb in suburbs:
        histogram[suburb] = 0

    # update histogram
    with open(tweets_filename) as fh:
        # TODO: Implement code that will process each tweet in the file and
        # update the count of the number of times each suburb is mentioned
        # in the tweet message.

        for li in fh:
            for key in histogram.keys():
                if key in li:
                    histogram[key] += 1

        return histogram



# --- main ---------------------------------------------------------------
# YOU DO NOT NEED TO MODIFY ANYTHING BELOW THIS LINE

def main():

    # produce histogram
    h = suburb_histogram("data/ACTPol_Traffic", "data/canberraSuburbs.txt")

    # plot histogram
    plt.bar(range(len(h)), h.values(), width=0.9, color="b", align="center")
    plt.title("Canberra Suburb Mentions in ACTPol_Traffic Tweets")
    plt.xticks(range(len(h)), list(h.keys()), rotation=75)
    plt.show()

if __name__ == "__main__":
    main()


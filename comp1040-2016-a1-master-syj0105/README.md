# COMP1040: Assignment 1
Semester 2, 2016

This `README.md` document describes the assignment and method of assessment.
Please read through the entire document carefully.

_This assignment is worth **10%** of your course grade.  It is due on
**Friday, 5 August 2016**._


## Background

The main aims for this assignment are:

1. To learn how to edit and run code with the PyCharm IDE.

2. To familiarise you with working with code repositories such as GitLab.

3. To give you experience writing code for simple data reading and manipulation.

4. To give you experience reading and modifying code for simple data 
   visualisation and web requests.

Some code and data is supplied via the repository this README file is in.


### Overview & Main Tasks

1. Implement a number of small data conversion routines

2. Use these routines to manipulate data for reporting and plotting:

  2.1 Report, for a select number of stations (e.g., capital cities) and each 
      month, the year and temperature that had the maximum temperature and the 
      temperature.

  2.2 Plot the yearly maximum/minimum temperature for a given station. 



### Getting and submitting the assignment

This assignment is entirely managed from within the School's GitLab server.
You will fork and checkout the assignment to work on it and then commit your
changes and push them back to the GitLab server to submit your solutions.

#### Getting the assignment

First, you will need to _fork_ a copy of the assignment from the COMP1040 
account here: <https://gitlab.cecs.anu.edu.au/comp1040/comp1040-2016-a1>

Once you have forked the project, you will need to check the project repository
out with the PyCharm IDE. This is done using the following steps:

1. Start a new Project in PyCharm either by using the "Checkout from VCS" option
   on the PyCharm splash screen, or by going to the 
   "VCS > Checkout from Version Control > Git" menu item.

2. In the pop-up, enter the Git HTTPS URI for your fork of the assignment. It 
   should something like this: 
   `https://gitlab.cecs.anu.edu.au/u1234567/comp1040-2016-a1.git`.
   
   __Note__: The address you put into the address field should start with 
   `https://gitlab` and *not* `git@gitlab`. 

3. Test that you have access to your repository by pressing the "Test" button.
   This may ask you for your username and password that you used to log into
   your GitLab account.


**Important**: Make sure your fork of the assignment is _private_ before you
start committing work to it, otherwise everyone using GitLab will be able to see 
your work. You can set a Project to private via the GitLab interface:

1. Go to the version of the assignment that you've forked from your Profile page.
 
2. Click on the "Settings" tab in the top right.

3. Under "Visibility Level", select "Private".

4. Click on the "Save changes" button 


#### Submitting your assignment

We can only mark your assignment if you code is pushed to the GitLab repository
you pulled it from.
It is your responsibility to ensure that all the changes you have made to the
repository are correctly pushed to the assignment repository hosted on GitLab.

__Note__: In Week 2 we will check that you have successfully forked the 
assignment repository to your own account and have completed the first issue
which involves adding a new file to the repository (see below).



## The Tasks

When you pull the assignment repository from GitLab you will notice there are 
the following files:

 - `data.py`:      Code to download and process historical temperature data from 
                   the Bureau of Meteorology.
                   
 - `plot.py`:      Code to read in temperature data and create plots.
 
 - `report.py`:    Creates a "hottest year by month" report.

 - `stations.txt`: List of weather station IDs and their names.

 - `test_data.py`: Unit tests for the functions in `data.py`.

Your task is to fix errors in and add code to the `data.py` file so all the 
tests in `test_data.py` pass and the required output is produced when the code
in `plot.py` and `report.py` is run.

The precise tasks you must complete are given in the issues section of your
GitLab repository for the assignment. You can find them by going to the
following web address, where `uNNNNNNN` should be replaced by your ANU ID:

    https://gitlab.cecs.anu.edu.au/uNNNNNNN/comp1040-2016-a1/issues

Each issue describes a problem with the code that must be fixed. After you fix 
each problem and verify that your fix is working by using the unit tests, 
close the associated issue using the web interface.

__Note__: There are many lines of comments within the assignment files. 
          Make sure you take the time to read these as they contain useful 
          information on things like how to call functions, how to run units 
          tests, etc.


### Marking Scheme

Marks will be awarded for correctly closing the issues associated with this
assignment on GitLab. We will run the provided unit tests and some of our own
tests to check the correctness of your code.

The maximum marks that will be awarded for each issue can be found in the title
of each issue. 

This assignment is worth 10% of your final grade.


## Copying & Plagiarism

The ANU takes plagiarism (i.e., the unattributed copying of another's work) very
seriously (see [Academic Honesty & Plagiarism][AHP]).

While we fully expect you to discuss approaches to questions with your
classmates you must never copy a complete or partial solution from someone else
and claim it as your own.

Make sure the code you write is your own. If you do get help from
someone or somewhere on the web, you must make a note (e.g., in the
code comments or a `NOTES.md` file) as to the nature of that help.


## Notes & References

The following sections provide some detail about the code and data used in this
assignment.


### Running the Unit Tests

The unit tests in `test_data.py` are pieces of code that check to see whether
the code you have written is working correctly.

You can run each of the tests separately by opening the `test_data.py` file
in PyCharm, selecting a test (e.g., the text `test_is_missing` after `def`),
then right-clicking on it and choosing "Run..." from the pop-up menu.

If you wish to run all the tests, find the `test_data.py` file in the Project
window on the left of PyCharm, right-click its name and choose 
"Run Unittests in test_data".

If the tests pass you will see a green bar appear in a window near the bottom of
your IDE. If it fails the bar will be red and some error messages will appear.
Read through the messages to see why the test(s) failed.


### Running the Plot and Report

Once you have the unit tests passing you can try to run the code in the 
`plot.py` and `report.py` files.

To do this, just select the file from the Project pane on the left-hand side of
the PyCharm IDE, right-click it and select "Run plot" (in the case of the 
`plot.py` file) or "Run report" (for `report.py`).

If you code is working, you should see a window with a plot of temperature
data appear when you run the `plot.py` file. The `report.py` file procudes
some text on the output console.

Once these are running, you can try changing the station from which the 
temperature data is obtained. Have a look in the comments towards the end of
the `plot.py` and `report.py` files for more information on this.

__Note__: You must be connected to the internet for the plot and report code
          to run as the functions in those files make requests to the 
          BoM web site to obtain the temperature data for the stations.


### The BoM data format

The data we will be looking at is from the Bureau of Meteorology web site:

    http://www.bom.gov.au/climate/change/acorn-sat/#tabs=Data-and-network

(Click on the dropdown menu that reads "Sortable list of ACORN-SAT stations"
to see the list of data sets)
    
They have a number of freely available files containing historical temperature
data dating back over 100 years for more than 100 different sites around
Australia.

If you have a look at an [example][] you will see that the data starts with a
_header_:

    MIN TEMP   015590 19100101 20140630 missing_value=99999.9 ALICE SPRINGS AIRPORT          

The header is followed by many rows of data that all look like this:

    19100101    20.9
    19100102    20.9
    19100103    22.5

Each row consists of a _datestamp_ of the form `YYYYMMDD` 
(e.g., `19100101`, which represents the date January 1st, 1910).

[example]: http://www.bom.gov.au/climate/change/acorn/sat/data/acorn.sat.minT.015590.daily.txt

Some of the code you write for this assignment will read in and reformat the
information in these files.


## Working with PyCharm and GitLab

Notes on how to use PyCharm and GitLab will be made available during the 
lectures and summarised on the [COMP1040 Course Overview Wiki][wiki].

The first lab session in Week 1 will be dedicated to helping you set up your lab
or home machine so you can access and work on this assignment.


## Other References 

If you are interested in trying out some of the more advanced features of the
PyCharm IDE, you can read about some nice tricks here:

- [An overview of some of PyCharm's more advanced editor features][AdvPyCharm]

[AdvPyCharm]: http://pedrokroger.net/getting-started-pycharm-python-ide/
[wiki]: https://gitlab.cecs.anu.edu.au/comp1040/course-overview/wikis/home
[AHP]: http://www.anu.edu.au/students/program-administration/assessments-exams/academic-honesty-plagiarism
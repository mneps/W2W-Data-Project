# When2Work Analysis

## Overview
This program scrapes data from the When2Work scheduling website and outputs a CSV file with data relating to hours worked by employee, per year.  The program allows the user to specify the date range for which they would like to scrape.  I have only conducted tested with the TSNY-NYC When2Work instance, but this program should theoretically should work for any company's When2Work account.

## Setup
To run this program, you will need Python3.7 and to install the packages listed in the `requirements.txt` file.  You will also need to save your When2Work credentials as environement variables under the names `W2W_USERNAME` and `W2W_PASSWORD`.  The final step is to set the variables in the `src/fields.py` file to your liking.

## Running the Program
Simply run the `src/main.py` script.  When the program is finished running, a file titled `results.csv` will be outputted in the directory specified in `src/fields.py`.  All  figures in `results.csv` represent the number of hours worked, rounded to the hundredth place.  In the case of TSNY-NYC, training shifts and shifts where the employee was shadowing another staff member are excluded from this analysis.
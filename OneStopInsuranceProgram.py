# Description: A program for the One Stop Insurance Company to enter and calculate new insurance policy information for its customers.
# Authour: Justin Seaward
# Date(s): July 29, 2025 - 


# Define program laibraries.
import datetime
import os
import sys
import FormatValues

# Define program constants.
f = open("Defults.dat", "r") # Defaults.dat is the file where the values for the constants are stored in. 

POL_NUM = int(f.readline()) # Policy number starts at 1944.
BAS_PREM_COST = int(f.readline()) # Basic premium cost is $869.00.
DIS_CAR_ESP = float(f.readline()) # Discount for additional car(s) is 25%.
EXT_LIB_COST = int(f.readline()) # The cost of extra liability coverage is $130.00.
GLASS_COST = int(f.readline()) # The cost for glass coverage is $86.00.
LOANER_COV_COST = int(f.readline()) # The cost for the loaner car coverage $58.00.
HST_ESP = float(f.readline()) # HST rate is 15%.
PRO_FEE_COST = float(f.readline()) # Processing fee for the monthly payments is $39.99.

f.close

# Define program fucntions.

# Main program starts here.
    

while True:

    os.system("cls" if os.name == "nt" else "clear") # Clears the screen when program is lanched.

    # Gather user inputs.
    while True:
    # Input and validations for customer first name.
        print()
        CustFN = input("Enter the customers first name: ").title()
        if CustFN == "":
            print()
            print("   Data Entry Error - Customer first name cannot be blank.")
            print()
        elif CustFN.isalpha() == False:
            print()
            print("     Data Entry Error - Invalid characters, must contain letters only.")
            print()
        else:
            break

        while True:
            # Input and validations for customer last name.
            print()
            CustLN = input("Enter the customers last name: ").title()
            if CustLN == "":
                print()
                print("    Data Entry Error - Customer last name cannot be blank.")
                print()
            elif CustLN.isalpha() == False:
                print()
                print("    Data Entry Error - Invalid characters, must contain letters only.")
                print()
            else:
                break
    
        
            

# Any housekeeping duties at the end of the program.
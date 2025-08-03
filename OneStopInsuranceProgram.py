# Description: A program for the One Stop Insurance Company to enter and calculate new insurance policy information for its customers.
# Authour: Justin Seaward
# Date(s): July 29, 2025 - 


# Define program laibraries.
import datetime
import os
import sys
import FormatValues as FV

# Define program constants.
f = open("Defaults.dat", "r") # Defaults.dat is the file where the values for the constants are stored in. 

POL_NUM = int(f.readline()) # Policy number starts at 1944.
BASIC_PREM_COST = float(f.readline()) # Basic premium cost is $869.00.
DIS_CAR_ESP = float(f.readline()) # Discount for additional car(s) is 25%.
EXT_LIA_COST = float(f.readline()) # The cost of extra liability coverage is $130.00.
GLASS_COST = float(f.readline()) # The cost for glass coverage is $86.00.
LOANER_CAR_COST = float(f.readline()) # The cost for the loaner car coverage $58.00.
HST_ESP = float(f.readline()) # HST rate is 15%.
PRO_FEE_COST = float(f.readline()) # Processing fee for the monthly payments is $39.99.

f.close

CURR_DATE = datetime.datetime.now() # Current date.

# Define program fucntions.

# Main program starts here.

while True:

    os.system("cls" if os.name == "nt" else "clear") # Clears the screen when program is lanched.
    # Gather user inputs.
    
    while True:
        # Input and validation(s) for customer first name.
        print()
        CustFN = "Rusty"#input("Enter the customers first name: ").title()
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
        
        #print(CustFN) # Test print.
        
    while True:
        # Input and validation(s) for customer last name.
        print()
        CustLN = "Shakeford"#input("Enter the customers last name: ").title()
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
        
        #print(CustLN) # Test print.

    while True:
        # Input and validation(s) for street address.
        print()
        StAdd = "128 school lane"#input("Enter the street address: ")
        if StAdd == "":
            print()
            print("    Data Entry Error - Street address cannot be blank.")
            print()
        else:
            break
    
        #print(StAdd) # Test print.

    while True:
        # Input and validation(s) for city.
        print()
        City = "deep bite"#input("Enter the city: ").title
        if City == "":
            print()
            print("    Data Entry Error - City cannot be blank.")
            print()
        else:
            break
    
        #print(City) # Test print.

    while True:
        # Input and validation(s) for the postal code.
        print()
        PostalCode = "A9A9A9"#input("Enter the postalcode (A9A9A9): ").upper
        if PostalCode == "":
            print()
            print("    Data Entry Error - Postalcode cannot be blank.")
            print()
        elif len(PostalCode) != 6:
            print()
            print("   Data Entry Error - Postalcode must be 6 characters.")
            print()    
        else:
            break
        ###########
        # Not working from line 108 to 116.
        '''
        elif PostalCode[0].isalpha != True or PostalCode[2].isalpha != True or PostalCode[4].isalpha != True:
            print()
            print("   Data Entry Error - Postalcode must conatin three letters and three numbers (A9A9A9).")
            print()
        elif PostalCode[1].isdigit == False or PostalCode[3].isdigit == False or PostalCode[5].isdigit == False:
            print()
            print("   Data Entry Error - Postalcode must conatin three letters and three numbers (A9A9A9).")
            print()
        ###########
        '''
    
        #print(PostalCode) # Test print.

    ProvLst = ["NL", "NS", "PEI", "NB", "QE", "ON", "MB", "SK", "AB", "BC", "NWT", "YT", "NT"] # Canadian province list to compare agaisnt user input.

    while True:
        # Input and validation for the province.
        Prov = "NL"#input("Enter the customer province (XX): ").upper()
        if Prov == "":
            print()
            print(" Data entry Error - The province cannot be blank.")
            print()
        elif len(Prov) != 2:
            print()
            print("Data entry error - The province must be two(2) charaters.")
            print()
        elif Prov not in ProvLst:
            print()
            print("Data entry error - The province entered is invalid." )
            print()
        else:
            break

        #print(Prov) # Test print.   

    while True:
    # Input and validations for phone number.
        try:
            print()
            PhoNum = "7094635555"#input("Enter the phone number (9999999999): ")
            if PhoNum == "":
                print()
                print("    Data Entry Error - Phone number cannot be blank.")
                print()
                continue
        except ValueError:
            print()
            print("    Data Entry Error - Phone number contains invalid characters.")
            print()
        else:
            if len(PhoNum) != 10:
                print()
                print("    Data Entry Error - Phone number has to contain 10 characters.")
                print()
            else:
                break
           
        #print(PhoNum) #test print.
       
    while True:
        # Input and validation(s) for the number of cars to be insured.
        print()
        try:
            NumCarsInsure = input("Enter the number of cars to be insured: ")
            NumCarsInsure = int(NumCarsInsure)
        except ValueError:
            print()
            print("    Data Entry Error - Number of cars to be insured contains invalid characters.")
            print()
        else:
            break

        #print(NumCarsInsure) # Test print.

    while True:
        # Input and validation(s) for extra liability uo to #1,000,000.
        print()
        ExtLia = input("Would you like extra liability up to $1,000,000 (Y or N): ").upper() 
        if ExtLia == "":
            print()
            print("    Data Entry Error - Extra liability cannot be blank.")
            print()
        elif ExtLia != "Y" and ExtLia != "N":
            print()
            print("    Data Entry Error - Extra liability must be entered as Y or N.")
            print()
        else:
            break

        #print(ExtLia) # Test print.
    
    while True:
        # Input and validation(s) for glass coverage.
        print()
        GlassCover = input("Would you like glass coverage (Y or N): ").upper() 
        if GlassCover == "":
            print()
            print("    Data entry error - Glass coverage cannot be blank.")
            print()
        elif GlassCover != "Y" and GlassCover != "N":
            print()
            print("    Data entry error - Glass coverage must be entered as Y or N.")
            print()
        else:
            break
    
        #print(GlassCover) # Test print.
    
    while True:
        # Input and validation(s) for the optional loaner car coverage.
        print()
        LoanCar= input("Would you like to add a loaner car (Y or N): ").upper()
        if LoanCar == "":
            print()
            print("    Data entry error - Loaner car cannot be blank.")
            print()
        elif LoanCar != "Y" and LoanCar != "N":
            print()
            print("    Data entry error - Loaner car must be entered as Y or N.")
            print()
        else:
            break

        #print(LoanCar) # Test print.

    PayMethodLst =["Full", "Monthly", "Downpay"]
    #DownPayAmt = 0
    MonPay = 0
    while True:
        # Input and validation for the payment type.
        print()
        PayMethod = "Full"#input("Enter the payment method (Full, Monthly, Downpay): ").title()
        if PayMethod == "":
            print()
            print(" Data entry error - The payment method cannot be blank.")
            print()
        elif PayMethod not in PayMethodLst:
            print()
            print("Data entry error - The payment method entered is invalid, must be Full, Monthly, or DownPay" )
            print()
        elif PayMethod == "Monthly" or PayMethod == "Downpay":
            print()
            DownPayAmt = input("Enter the down payment amount: ")
            DownPayAmt = float(DownPayAmt)
            continue
        else:
            DownPayAmt = 0
            break
            
    
        #print(PayMethod) # Test print.
        #print(DownPayAmt) # Test print.
    
    while True:
        # Input and validation for the claim number.
        try:
            ClaimNum = input("Enter the claim number: ")
            if ClaimNum == "":
                print()
                print(" Data entry error - The claim number cannot be blank.")
                print()
                continue
            elif len(ClaimNum) != 5:
                print()
                print(" Data entry error - The claim number has to be 5 characters.")
                print()
                continue
            ClaimNum = int(ClaimNum)
        except ValueError:
                print()
                print(" Data entry error - The claim number contains invalid characters.")
                print()
        else:
            break

        #print(ClaimNum) # Test print.

    while True:
        # Input and validation for the claim date.
        print()
        try:
            ClaimDate = input("Enter the claim date: ")
            ClaimDate = datetime.datetime.strptime(ClaimDate, "%Y-%m-%d")
            if ClaimDate == "":
                print()
                print(" Data entry error - Claim datew cannot be blank.")
                print()
        except ValueError:
                print()
                print(" Data entry error - Claim date must be entered YYYY-MM-DD.")
                print()
        else:
            '''
            # Check that the date does not exceed the current date.
            if ClaimDate > CURR_DATE:
                print() 
                print(" Data entry error - Claim date can not exceed the current date.")
                print()
                continue
            '''
        #else:    
            break
        
        #print(ClaimDate) # Test print.

    while True:
        # Input and validation for the claim amount.
        print()
        try:
            ClaimAmt = input("Enter the claim amount: ")
            ClaimAmt = float(ClaimAmt)
            if ClaimAmt == "":
                print()
                print(" Data entry error - The claim amount cannot be blank.")
                print()
                continue
        except ValueError:
                print()
                print(" Data entry error - The claim amount contains invalid characters.")
                print()
        else:
            break    

        #print(ClaimAmt) # Test print.

    # Define program calculations.

    # Calculation for insurance premium.
    if NumCarsInsure == 1:
        InsureCost = BASIC_PREM_COST
    elif NumCarsInsure > 1:
        NumCarsInsure -= 1
        InsureCost = (BASIC_PREM_COST - (DIS_CAR_ESP * BASIC_PREM_COST)) * NumCarsInsure
        NumCarsInsure += 1

    # Calculation for total extra cost.

    # Option for extra liability.
    if ExtLia == "Y":
        ExtLiaCost = EXT_LIA_COST * NumCarsInsure
        ExtLia == "Yes"
    elif ExtLia == "N":
        ExtLiaCost = 0
        ExtLia = "No" 
        
    # Option for glass coverage.
    if  GlassCover == "Y":
        GlassCoverCost = GLASS_COST * NumCarsInsure
        GlassCover == "Yes"
    else: 
        GlassCover == "N"
        GlassCoverCost = 0
        GlassCover = "No"

    # Option for loaner car.
    if LoanCar == "Y":
        LoanCarCost = LOANER_CAR_COST * NumCarsInsure
        LoanCar == "Yes"
    else: 
        LoanCar == "N"
        LoanCarCost = 0
        LoanCar = "No"

    # If statement and calculations for 8 monthly payments with or without down payment.
    if PayMethod == "Downpay":
        MonPay = ((TotCostHst + PRO_FEE_COST) - DownPayAmt) / 8
    elif PayMethod == "Monthly":
        MonPay = (TotCostHst + PRO_FEE_COST) / 8
    #else:
       # MonPay == "Full"

    # Calculation for total extra cost.
    TotExtCosts = EXT_LIA_COST + GLASS_COST + LOANER_CAR_COST

    # Calculation for total insurance premium.
    TotInsurPrem = InsureCost + TotExtCosts

    # Calculation for HST.
    HST = TotInsurPrem * HST_ESP

    # Calculation for total cost.
    TotCostHst = TotInsurPrem * (HST_ESP + 1)

    # Invoice date.
    InvoiceDate = CURR_DATE

    # Format for Invoice date.
    InvoiceDateDsp = FV.FDateM(InvoiceDate)

    # Format for customer name.
    CustNameDsp = CustFN + CustLN    

    # Format for phone number.
    PhoNumDsp = "(" + PhoNum[0:3] + ")" + " " + PhoNum[3:6] + "-" + PhoNum[6:10]

    # Format for postal code.
    PostCodeDsp = PostalCode[0:2] + "-" + PostalCode[3:6]

    # Format for city, province and postalcode.
    CityProPostDsp = City + ", " + Prov + ", " + PostCodeDsp

    # Format for insurance cost.
    InsureCostDsp = FV.FDollar2(InsureCost)

    # Format for extra liability cost.
    ExtLiaCostDsp = FV.FDollar2(ExtLiaCost)  

    # Format for glass coverage.
    GlassCoverCostDsp = FV.FDollar2(GlassCoverCost)

    # Format for loaner car cost.
    LoanCarCostDsp = FV.FDollar2(LoanCarCost)

    # Format for HST.
    HSTDsp = FV.FDollar2(HST)

    # Format for total extra cost.
    TotExtCostDsp = FV.FDollar2(TotExtCosts)

    # Format for total insureance permium.
    TotInsurPremDsp = FV.FDollar2(TotInsurPrem)

    # Format for total cost.
    TotCostHstDsp = FV.FDollar2(TotCostHst)

    # Format for down payment.
    DownPayAmtDsp = FV.FDollar2(DownPayAmt)

    # Format for monthly pay.
    MonPayDsp = FV.FDollar2(MonPay)#

    # Format for claim amount.
    ClaimAmtDsp = FV.FDollar2(ClaimAmt)

    # Function for first pay date.
    FirstPayDate = FV.FirstPayDate(CURR_DATE)

    ### Display Receipt ###

    print(f" -------------------------------------------------------------------- ")
    print(f" ---------               One Stop Insurance                 --------- ")
    print(f" -------------------------------------------------------------------- ")
    print()
    print(f" Policy Number: {POL_NUM:<15d}      Invoice Date: {InvoiceDateDsp:>10s}")
    print()
    print(f" Customer: {CustNameDsp:<20s}      Phone Number: {PhoNumDsp:<13s}     ")
    print(f" Address:  {StAdd:<20s}                                               ")
    print(f"           {CityProPostDsp:<20s}   Cars on policy: {NumCarsInsure:<2d}")
    print()
    print(f" -------------------------------------------------------------------- ")
    print(f"            Options              &                Cost                ")
    print(f"                                                                      ")
    print(f"                                  Insurance Premiums: {InsureCostDsp:>8s}")
    print(f"                                                          ----------- ")
    print(f" Extra Liability: {ExtLia:<3s}    Liability Cost:     {ExtLiaCostDsp:>8s}")
    print(f" Glass Coverage:  {GlassCover:<3s}Glass Coverage:     {GlassCoverCostDsp:>8s}")
    print(f" Loaner Car:      {LoanCar:<3s}   Loaner Car Cost:    {LoanCarCostDsp:>8s}")
    print(f"                  -------------                           ----------- ")
    print(f" Total Extra Cost: {TotExtCostDsp:<8s}          Total premium cost: {TotInsurPremDsp:<8s}")
    print(f"                  -------------                           ----------- ")
    print(f"                                  HST:                {HSTDsp:>8s}   ")
    print(f"                                  Total Cost:         {TotCostHstDsp:>8s}")
    print(f" Payment Method: {PayMethod:<7s}                          ----------- ")
    print(f" Monthly Payment:{MonPayDsp:<8s}                                      ")
    print(f" Down Payment:   {DownPayAmtDsp:<8s} First Payment Date: {FirstPayDate:<10s}")
    print(f" -------------------------------------------------------------------- ")
    print()

    POL_NUM += 1

    f = open("Policies.dat", "a") 
 
    f.write(f"{str(CustNameDsp)},")
    f.write(f"{str(StAdd)}, ")
    f.write(f"{str(City)}, ")
    f.write(f"{str(Prov)}, ")
    f.write(f"{str(PostalCode)}, ")
    f.write(f"{FV.FDateS(InvoiceDate)}, ")
    f.write(f"{str(NumCarsInsure)}, ")
    f.write(f"{str(InsureCost)},")
    f.write(f"{str(ExtLiaCost)}, ")
    f.write(f"{str(GlassCoverCost)}, ")
    f.write(f"{str(LoanCarCost)},")
    f.write(f"{str(TotExtCosts)},")
    f.write(f"{str(TotInsurPrem)},")
    f.write(f"{str(HST)},")
    f.write(f"{str(TotCostHst)},")
    f.write(f"{str(PayMethod)},")
    f.write(f"{str(MonPay)},")
    f.write(f"{str(DownPayAmt)},")
    f.write(f"{str(FirstPayDate)},")
    f.write(f"{str(ClaimNum)},")
    f.write(f"{FV.FDateS(ClaimDate)},")
    f.write(f"{str(ClaimAmt)}\n")
    
    f.close()

    f = open("Policies.dat", "r")

    for ClaimRecords in f:

        ClaimLst = ClaimRecords.splitt(",")

        ClaimNumR = ClaimLst[20].strip()
        ClaimDateR = ClaimLst[21].strip()
        ClaimAmtR = float(ClaimLst[22].strip())

    print(f"       Claim Number          Claim Date           Amount              ")
    print(f"   -----------------------------------------------------------        ")
    print(f"         {ClaimNumR:<5d}            {ClaimDate}          {ClaimAmtR:<8}        ")

    f.close()

    f = open("Defaults.dat", "w")

    f.write(f"{POL_NUM}\n")
    f.write(f"{BASIC_PREM_COST}\n")
    f.write(f"{DIS_CAR_ESP}\n")
    f.write(f"{EXT_LIA_COST}\n")
    f.write(f"{GLASS_COST}\n")
    f.write(f"{LOANER_CAR_COST}\n")
    f.write(f"{HST_ESP}\n")
    f.write(f"{PRO_FEE_COST}\n")
    
    f.close()


    Wait = input("Press enter key to continue or enter End: ").title()
    if Wait == "End":
        break
    if Wait == "":
        continue

# Any housekeeping duties at the end of the program.
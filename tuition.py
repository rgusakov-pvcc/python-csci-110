# Name: Ruslan Gusakov
# Prog Purpose: this program computes college tuition & fees based on number of credits
#
#
#
#
#

import datetime
# define tuition and fee rates
RATE_TUITION_IN = 155
RATE_TUITION_OUT = 331.60
RATE_CAPITAL = 23.5
RATE_INSTITUTION = 1.75
RATE_ACTIVITY = 2.90

# define global variables
inout = 1
numcredits = 0
scholarshipamt = 0
tuitionfee = 0
capitalfee = 0
institutionfee = 0
activityfee = 0
totalowed = 0
balance = 0

# Define Program Functions


def main():
    another_student = True
    while another_student:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\n Would you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno.upper() != "Y":
            another_student = False


def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = float(input("Scholarship amount received: "))


def perform_calculations():
    global tuitionfee, capitalfee, institutionfee, activityfee, totalowed, balance
    if inout == 1:
        tuitionfee = numcredits * RATE_TUITION_IN
        capitalfee = 0
    else:
        tuitionfee = numcredits * RATE_TUITION_OUT
        capitalfee = numcredits * RATE_CAPITAL
    institutionfee = numcredits * RATE_INSTITUTION
    activityfee = numcredits * RATE_ACTIVITY
    totalowed = tuitionfee + capitalfee + institutionfee + activityfee
    balance = totalowed - scholarshipamt


def display_results():
    print('\n----------------------------------------------------------------------')
    print("Number of creds: "  +  str(numcredits))
    print('----------------------------------------------------------------------')
    print("Tuition: "  +  format(tuitionfee,'10,.2f'))
    print("Capital Fee: "  +  str(capitalfee))
    print("Institution Fee: " +    str(institutionfee))
    print("Activity Fee: " + str(activityfee))
    print("Total: "  + str(totalowed))
    print("Scholarship: " + str(scholarshipamt))
    print('----------------------------------------------------------------------')
    print("Balanced Owed: " + str(balance))
    print('----------------------------------------------------------------------')
    print(str(datetime.datetime.now()))
    print("Note: PVCC Fee Rates: https://www.pvc.edu/tuition-and-fees")


# call on main program to execute
main()

#This code displays the rate at which the car battery will go from x% to 100%

battery_per = int(input("What is the current battery?: "))

#This code calculates 1% as 10 minutes

def chargetime(x):
    chargefull = 100 - battery_per
    chargeTime = chargefull * 600
    Chargecon = chargeTime /60
    #It then converts the minutes to hours for simplification
    ChargeconHour = Chargecon / 60
    #If the user enters a number that is not 0-199, the code will not calculate
    if x >= 100:
        print("Battery is already full.")
    if x <= 100:
        print("It will take you", Chargecon, "minute(s)")
        Summary = input("Do you want this converted into hours? (Y/N):")
        if Summary == 'Y'or Summary == 'y':
            print("It will take you", ChargeconHour, "hour(s)")

chargetime(battery_per)
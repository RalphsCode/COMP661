from datetime import datetime, timedelta;
while True:
     again = input("Are you ready to start the time distance calculator? y/n ");
     if again == 'y':
            dDate = str(input('When are you leaving (YYYY/MM/DD)? '));
            dDateFormatted = datetime.strptime(dDate, '%Y/%m/%d');

            dTime = str(input('What time are you leaving? (use military time - eg: 0930) '));
            dTimeFormatted = datetime.strptime(dTime, '%H%M')

            dDate_dTime = dDate + ' ' + dTime;
            dDate_dTime_formatted = datetime.strptime(dDate_dTime, '%Y/%m/%d %H%M')

            tDistance = int(input('How many miles are you travelling? '))
            tSpeed = int(input('At what MPH do you typically drive? '));

            hoursNeeded = tDistance // tSpeed
            minsNeeded = int(((tDistance % tSpeed)/100 * 60))
            aTime = (dDate_dTime_formatted + timedelta(hours = hoursNeeded, minutes = minsNeeded));

            print("\n***************************************************");
            print(f"Travelling for {tDistance} miles at a speed of {tSpeed}mph,"); 
            print(f"your drive time will be: {hoursNeeded} hours and {minsNeeded} minutes.");
            print(f"And you will arrive on: {aTime:%Y/%m/%d at: %I:%M %p}.\n\t - Drive Safely!");
            print("***************************************************");

           
     else :
            print("\nThanks for using my travel calculator. Bye.\n");
            
            break;

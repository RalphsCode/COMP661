from datetime import timedelta, datetime;

while True:
  userName = (input('\nPlease enter your name: ') or "Bill Gates");
  bDay = (input('\nWhen were you born (MM/DD/YYYY)? ') or "04/25/2001");

################### FUNCTIONS ##################
  def intro() :
    print("\n**********************************************");
    print(f"Hello {userName},");  
  
  def age() :
    if bDayFormatted > twoYearMark :
      displayAge = ageDays;
      unit = 'days ';
    else :
      displayAge = ageYears;
      unit = 'years ';
    print(f"I have determined that you are {displayAge} {unit}old."); 
  
  def footer() :
      print("**********************************************");
  
########################## DOING THE MATH ###########################
## NEED TODAYS DATE, BIRTHDAY DATE, YESTERDAY, TOMORROW, USERS AGE ##

  bDayFormatted = datetime.strptime(bDay, '%m/%d/%Y');                    # datetime.datetime
  bDayMonth = bDayFormatted.month;                                        # Int
  bDayDay = bDayFormatted.day;                                            # Int

  today = datetime.now();                                                 # datetime.datetime
  todayFormatted = datetime.strftime(today, '%m/%d/%y');                  # str
  todayFormatted= datetime.strptime(todayFormatted, '%m/%d/%y');          # datetime.datetime
  thisMonth = today.month                                                 # Int
  thisDay = today.day                                                     # Int
  yesterDay = (today - timedelta (days=1))
  yesterDay = yesterDay.day                                               # Int

  toMorrow = (today + timedelta (days=1))
  toMorrow = toMorrow.day                                                 # Int
        
  userAge = abs(today - bDayFormatted);                                      # datetime.timedelta

  ageYears = (userAge.days//365);                                         # Integer
  ageDays = (userAge.days);                                               # Integer 
  twoYearMark = (today - timedelta (days=731))                            # datetime.datetime;

  bDayMonthDay = '2023' + '/' + bDay[0:5];
  bDayMonthDayFormatted = datetime.strptime(bDayMonthDay, '%Y/%m/%d');

############### DISPLAY RELEVANT MESSAGE ##############

  if bDayFormatted < today :

      if bDayMonth == thisMonth and bDayDay == thisDay :
        intro();
        print("Your birthday is Today, \nH A P P Y   B I R T H D A Y !!!");
        age();
        footer(); 
        
      elif bDayMonth == thisMonth and bDayDay == yesterDay :
        intro();
        print("Your birthday was yesterday, \nBelated Happy Birthday!");

        age();
        footer(); 
      
      elif bDayMonth == thisMonth and bDayDay == toMorrow :
        intro();
        print("Your birthday is tomorrow, \nHave a Happy Birthday!");
        age();
        footer(); 

      else :
        intro();
        age();
        print(f"Your birthday is {bDayFormatted.strftime('%B %d')}, and");
        if bDayMonthDayFormatted > today :
          print('your 2023 Birthday is yet to come.');
          daysToBirthday = str(bDayMonthDayFormatted - today);
          print(f"There are {daysToBirthday.split()[0]} days until the big day!");
        else:
          print('your 2023 Birthday has already past.');
          timeToNextBday = timedelta(days=365);
          daysToBirthday = str((bDayMonthDayFormatted + timeToNextBday) - today);
          print(f"There are {daysToBirthday.split()[0]} days until your next big day!");
        footer();
  
############ IF THE BIRTHDAY ENTERED IS IN THE FUTURE THROW AN ERROR ###########  

  else:
    print(f"\nERROR: Your birthday cannot be in the future, please try again.")
    continue;
  
############ ASK IF THE USERS WANTS TO USE THE APP AGAIN ################

  again = input("\nWant to do the birthday calculator again? y/n ");
  if again != 'y':
    print("\nThanks for using my birthday calculator. Bye.\n");
    break;

############  END  ###########
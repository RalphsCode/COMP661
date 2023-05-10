# START APPLICATION
#############################################################

def displayContacts() :                                                                                                                     # FUNCTION TO DISPLAY ALL CONTACT NAMES
    i = 0; 
    print("\nContacts List:\n")
    for contact in contacts:
        print(f"({i+1}) {contacts[i][0]}\n");
        i += 1   

def menu():                                                                                                                                 # FUNCTION TO SHOW THE MAIN MENU
    choice = input("Please make a number selection: \n\t 1. List all contacts - press 1 \n\t 2. View a contact - press 2\n\t 3. Add a contact - press 3\n\t 4. Delete a contact - press 4\n\t 5. EXIT application - press 5   ")
    return choice
               
contacts = [['Joan Doe', '8589830734', 'jdoe@gmail.com'], ['Crystal Ball', '619543902', 'cball@yahoo.com']]                                 # ORIGINAL LIST OF CONTACTS
while True:
        userChoice = menu()
        if userChoice == '1' :                                                                                                              # VIEW ALL CONTACT NAMES
                displayContacts()
        elif userChoice == '2' :                                                                                                            # VIEW A SPECIFIC CONTACT       
                displayContacts()
                viewContact = int(input('\n Please enter the number of the contact that you wish to view: '))
                print(f'\nHere is contact number {viewContact}:')
                print(f'\t{contacts[viewContact - 1]}\n')
        elif userChoice == '3' :                                                                                                             # ADD A NEW CONTACT
                newContactName = input('\nPlease enter the new contact first and last name: ') or 'Ben Dover'
                newContactPhone = input('Please enter the new contact phone number (all digits): ') or '6194359908'                          # USES DEFAULT VALUES
                newContactEmail = input('Please enter the new contact email address: ') or 'ben@hotmail.com'
                newContactList = [[newContactName, newContactPhone, newContactEmail]]
                contacts.extend(newContactList)
                print(f"\n{newContactName} has been added.\n")
        elif userChoice == '4' :                                                                                                             # DELETE A CONTACT
                displayContacts()
                delContact = int(input('\n Please enter the number of the contact that you wish to remove: '))
                if delContact > len(contacts):                                                                                                # ENSURE ENTRY IS VALID
                       print(f'\n>>>>> ERROR: I COULD NOT FIND A CONTACT NUMBER {delContact}, please try again <<<<<\n')
                       continue
                else: removed = contacts.pop(delContact -1)
                print(f"\nXXX {removed[0]} has been deleted XXX\n")

        elif userChoice == '5' :                                                                                                              # EXIT APPLICATION
                break;    

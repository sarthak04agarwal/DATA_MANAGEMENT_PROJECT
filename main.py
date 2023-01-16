import json

# Loads the song-data JSON file
with open("song-data.json", "r") as file_ref:
    song_Data = json.load(file_ref)

# Loads the user-data JSON file
with open("user-data.json", "r") as file_ref:
    user_Data = json.load(file_ref)

# Method that displays all the song data
def display_All():
    for i in range (len(song_Data)):
        print("Title: " + song_Data[i]['title'])
        print("Artist: " + song_Data[i]['artist'])
        print("Genre: " + song_Data[i]['genre'])
        print("Length: " + str(song_Data[i]['length']))
        print("Released: " + song_Data[i]['released'] + '\n')

# Method that filters data based on some criteria
def filter_Data():
    status = input("1. Title\n2. Artist\n3. Genre\n4. Length\n5. Released Date\nPlease select the search criteria: ")
    if status ==  '1':
        status2 = input("\nPlease enter the Title that you want to search: ")
        print(" ")
        found = False
        for i in range(len(song_Data)):
            if song_Data[i]['title'] == status2:
                found = True
                print("Title: " + song_Data[i]['title'])
                print("Artist: " + song_Data[i]['artist'])
                print("Genre: " + song_Data[i]['genre'])
                print("Length: " + str(song_Data[i]['length']))
                print("Released: " + song_Data[i]['released'] + '\n')
        if not found:
            print("Not found.")
    elif status ==  '2':
        status2 = input("\nPlease enter the Artist that you want to search: ")
        found = False
        for i in range(len(song_Data)):
            if song_Data[i]['artist'] == status2:
                found = True
                print("Title: " + song_Data[i]['title'])
                print("Artist: " + song_Data[i]['artist'])
                print("Genre: " + song_Data[i]['genre'])
                print("Length: " + str(song_Data[i]['length']))
                print("Released: " + song_Data[i]['released'] + '\n')
        if not found:
            print("Not found.")
    elif status == '3':
        status2 = input("\nPlease enter the Genre that you want to search: ")
        found = False
        for i in range(len(song_Data)):
            if song_Data[i]['genre'] == status2:
                found = True
                print("Title: " + song_Data[i]['title'])
                print("Artist: " + song_Data[i]['artist'])
                print("Genre: " + song_Data[i]['genre'])
                print("Length: " + str(song_Data[i]['length']))
                print("Released: " + song_Data[i]['released'] + '\n')
        if not found:
            print("Not found.")
    elif status == '4':
        status2 = input("\nPlease enter the Length that you want to search: ")
        found = False
        for i in range(len(song_Data)):
            if str(song_Data[i]['length']) == status2:
                found = True
                print("Title: " + song_Data[i]['title'])
                print("Artist: " + song_Data[i]['artist'])
                print("Genre: " + song_Data[i]['genre'])
                print("Length: " + str(song_Data[i]['length']))
                print("Released: " + song_Data[i]['released'] + '\n')
        if not found:
            print("Not found.")
    elif status == '5':
        status2 = input("\nPlease enter the Released Data that you want to search: ")
        found = False
        for i in range(len(song_Data)):
            if song_Data[i]['released'] == status2:
                found = True
                print("Title: " + song_Data[i]['title'])
                print("Artist: " + song_Data[i]['artist'])
                print("Genre: " + song_Data[i]['genre'])
                print("Length: " + str(song_Data[i]['length']))
                print("Released: " + song_Data[i]['released'] + '\n')
        if not found:
            print("Not found.")
    else:
        print("Please select a valid option.")

def myFunc(e):
  return e['length']

# Method that sorts the data based on the length of each song, the user can pick whether the list should be sorted in an ascending order or a descending order
def sort_Data():
    sort =  input("Do you want the Length of the songs in ascending order or descending order? \n1: Ascending order \n2: Descending order \nPlease select a number: ")
    if sort == '1':
        song_Data.sort(key=myFunc)
        print("Data sorted succesfully.")
    elif sort == '2':
        song_Data.sort(reverse=True, key=myFunc)
        print("Data sorted succesfully.")
    else:
        print("Please type one of the numbers above")
# Method that adds song to a user's favorite list
def add_Favorite():
    if loggedIn:
        for i in range(len(song_Data)):
            print(song_Data[i]['title'] + ': ' + str(i+1))
        add_Fav = input("Please select the number which correlaates to the song that you want to add to you favorite list: ")
        add_Fav = int(add_Fav)-1
        if song_Data[add_Fav]['title'] in user_Data[loggedInPos]['faves']:
            print(song_Data[add_Fav]['title'] + " is already in your favorite list.")
        else:
            user_Data[loggedInPos]['faves'].append(song_Data[int(add_Fav)]['title'])
            print(song_Data[add_Fav]['title'] + " has been added to your favorite list.")

# Method that removes a song from the user's favorite list
def remove_Favorite():
    if loggedIn:
        for i in range(len(user_Data[loggedInPos]['faves'])):
            print(user_Data[loggedInPos]['faves'][i] + ': ' + str(i+1))
        rem_Fav = input("Please select the number which correlaates to the song that you want to remove from your favorite list: ")
        if user_Data[loggedInPos]['faves'][int(rem_Fav)-1] in user_Data[loggedInPos]['faves']:
            print(user_Data[loggedInPos]['faves'])
            removed = user_Data[loggedInPos]['faves'].pop(int(rem_Fav)-1)
            print(removed + " has been removed from your favorite list.")
            print(user_Data[loggedInPos]['faves'])
        else:
            print("Please enter one of the numbers above.")

# Method that displays the logged in user's favorite songs
def display_Favorite():
    print(user_Data[loggedInPos]['username'] + "'s Favorites: " + str(user_Data[loggedInPos]['faves']))
    

# This loop is the main menu that appears in the starting of the program
loop = True
loggedIn = False
loggedInPos = None
def displayMenu():
    global loop
    status = input("\n1. Log in to account\n2. Create new account\n3. Log out of account\n4. Exit\n Please type your number: ")
    print(" ")
    if status == "1":
        oldUser()
        if(loggedIn):
            displaySecMenu()
    elif status == "2":
        newUser()
    elif status == '3':
        logOut()
    elif status == '4':
        loop = False
    else:
        print("Invalid selection. Please select a valid option.")

# Method that displays the second menu 
# This menu appears once the user has logged into his account from the first menu
def displaySecMenu():
    loop2 = True
    while(loop2):
        selection = input("\n1. Display All Data \n2. Display some of the data \n3. Sort the data \n4. Add data to favorite list \n5. Remove data from favorite \n6. Display Favorite List \n7. Exit" + "\n Please type your number: ")
        print(" ")
        if selection == "1":
            display_All()
        elif selection == "2":
            filter_Data()
        elif selection == "3":
            sort_Data()
        elif selection == "4":
            add_Favorite()
        elif selection == "5":
            remove_Favorite()
        elif selection == "6":
            display_Favorite()
        elif selection == '7':
            loop2 = False
        else:
            print("Invalid selection. Please select a valid option.")
            

# Method to create a new account
def newUser():
    userFound = False
    createLogin = input("Create login name: ")
    
    for i in range(len(user_Data)):
        if user_Data[i]['username'] == createLogin:
            userFound = True
            
    if userFound:
        print("User already exists\n")
    else:
        createPassw = input("Create password: ")
        user_Data.append(
            {
                "username" : createLogin,
                "password" : createPassw,
            }
        )
        print("\nUser created\n")

# Method for signing into an account            
def oldUser():
    login = input("Enter login name: ")
    usernameFound = False
    for i in range(len(user_Data)):
            if user_Data[i]['username'] == login:
                passw = input("Enter password: ")
                if user_Data[i]['password'] == passw:
                    global loggedInPos
                    global loggedIn
                    loggedIn = True
                    loggedInPos = i
                    usernameFound = True
                    print("User found. Logged in")
                else:
                    print("Password incorrect")
                    usernameFound = True
    if not usernameFound:           
        print("User not found")
                    
# Method to loggout of account        
def logOut():
    global loggedIn
    if loggedIn == True:
        loggedIn = False
        global loggedInPos
        loggedInPos = None
        print("Logged out successfully.")
    else:
        print("Not logged in.")


# This starts everything and display the first menu of the program
while loop:
    displayMenu()
# This makes sure that the data that was changed there also gets changed in the actual file
with open("user-data.json", "w") as file_ref:
    json.dump(user_Data, file_ref)

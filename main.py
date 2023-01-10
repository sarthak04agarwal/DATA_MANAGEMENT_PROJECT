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
        print("Language: " + song_Data[i]['language'])
        print("Released: " + song_Data[i]['released'] + '\n')

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


def display_Favorite():
    print(user_Data[loggedInPos]['username'] + "'s Favorites: " + user_Data[loggedInPos]['faves'])
       


loop = True
loggedIn = False
loggedInPos = None
def displayMenu():
    global loop
    status = input("\n1. Log in to account\n2. Create new account\n3. Log out of account\n Please type your number: ")
    if status == "1":
        oldUser()
        if(loggedIn):
            displaySecMenu()
    elif status == "2":
        newUser()
    elif status == '3':
        logOut()
    else:
        loop = False

# Method that displays the second menu 
def displaySecMenu():
    loop2 = True
    while(loop2):
        selection = input("1. Display All Data \n2. Display some of the data \n3. Sort the data \n4. Add data to favorite list \n5. Remove data from favorite \n6. Display Favorite List \n7. Exit" + "\n Please type your number: ")
        if selection == "1":
            display_All()
        elif selection == "2":
            print("Hello")
        elif selection == "3":
            print("Hello")
        elif selection == "4":
            print("Hello")
        elif selection == "5":
            print("Hello")
        elif selection == "6":
            display_Favorite()
        else:
            loop2 = False


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
    if loggedIn == True:
        global loggedIn
        loggedIn = False
        global loggedInPos
        loggedInPos = None
        print("Logged out successfully.")



while loop:
    displayMenu()
with open("user-data.json", "w") as file_ref:
    json.dump(user_Data, file_ref)
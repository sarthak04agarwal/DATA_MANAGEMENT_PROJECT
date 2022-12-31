import json


with open("song-data.json", "r") as file_ref:
    song_Data = json.load(file_ref)

with open("user-data.json", "r") as file_ref:
    user_Data = json.load(file_ref)


def display_All():
    for i in range (len(song_Data)):
        print("Title: " + song_Data[i]['title'])
        print("Artist: " + song_Data[i]['artist'])
        print("Genre: " + song_Data[i]['genre'])
        print("Length: " + str(song_Data[i]['length']))
        print("Language: " + song_Data[i]['language'])
        print("Released: " + song_Data[i]['released'] + '\n')


#def display_Favorite():
   

	
#menu = ("1. Display All Data \n2. Display some of the data \n3. Sort the data \n4. Add data to favorite list \n5. Remove data from favorite \n6. Display Favorite List \n7. Exit" + "\n Please type your number: ")


loop = True
loggedIn = False
loggedInPos = None
def displayMenu():
    global loop
    status = input("\n1. Log in to account\n2. Create new account\n3. Log out of account\n Please type your number: ")
    if status == "1":
        oldUser()
    elif status == "2":
        newUser()
    elif status == '3':
        logOut()
    else:
        loop = False

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
    global loggedIn
    login = input("Enter login name: ")
    usernameFound = False
    for i in range(len(user_Data)):
            if user_Data[i]['username'] == login:
                passw = input("Enter password: ")
                if user_Data[i]['password'] == passw:
                    print("User found. Logged in")
                    loggedIn = True
                    usernameFound = True
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
        print("Logged out successfully.")



while loop:
    displayMenu()


'''
loop = True
while(loop):
    selection = input(menu2)
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
        print("Hello ")
    else:
        loop = False
'''


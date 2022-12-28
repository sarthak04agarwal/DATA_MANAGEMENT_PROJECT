import json

file = open("song-data.json", "r")
dataStr = file.read()
file.close()
song_Data = json.loads(dataStr)

file = open("user-data.json", "r")
dataStr = file.read()
file.close()

user_Data = json.loads(dataStr)



def display_All():
    for i in range (len(song_Data)):
        print("Title: " + song_Data[i]['title'])
        print("Artist: " + song_Data[i]['artist'])
        print("Genre: " + song_Data[i]['genre'])
        print("Length: " + str(song_Data[i]['length']))
        print("Language: " + song_Data[i]['language'])
        print("Released: " + song_Data[i]['released'] + '\n')


#def display_Favorite():
   

menu = ("1. Display All Data \n2. Display some of the data \n3. Sort the data \n4. Add data to favorite list \n5. Remove data from favorite \n6. Display Favorite List \n7. Exit" + "\n Please type your number: ")

menu2 = ("1. Log in to account\n2. Log out of account\n3. Create new account\n Please type your number: ")

print(user_Data)
loop2 = True 
while(loop2):
    selection2 = input(menu2)
    if selection2 == "1":
        usernamelogin = input("Please enter your username: ")
        passwordlogin = input("Please enter your password: ")
        user_Data['username'] = usernamein
        user_Data['password'] = passwordin
    elif selection2 == "3":
        usernamein = input("Please enter your new Username: ")
        passwordin = input("Please enter your password: ")
        user_Data['username'] = usernamein
        user_Data['password'] = passwordin
        print(user_Data)
    #elif selection2 == "2":
        #print("Hello")
    #else:
        #loop2 = False

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

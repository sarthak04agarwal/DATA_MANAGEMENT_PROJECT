import json

file = open("song-data.json", "r")
dataStr = file.read()
file.close()

song_Data = json.loads(dataStr)

def display_All():
    for i in range (len(song_Data)):
        print("Title " + song_Data[i]['title'])
        print("Artist " + song_Data[i]['artist'])
        print("Genre " + song_Data[i]['genre'])
        print("length " + song_Data[i]['length'])
        print("language " + song_Data[i]['language'])
        print("released " + song_Data[i]['released'] + "\n")
        


menu = ("1. Display All Data \n2. Display some of the data \n3. Sort the data \n4. Add data to favorite list \n5. Remove data from favorite \n6. Display Favorite List \n7. Exit" + "\n Please type your number: ")


loop = True
while(loop):
    selection = input(menu)
    if selection == "1":
        #display_All()
    elif selection == "2":
        #search_contact()
    elif selection == "3":
        #edit_contact()
    elif selection == "4":
        #new_contact()
    elif selection == "5":
        #remove_contact()
    elif selection == "6":
        #remove_contact()
    else:
        #loop = False
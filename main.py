import json

# Open a file and use json.load to load JSON data from file as data
with open("song-data.json", "r") as file_ref:
    song_Data = json.load(file_ref)




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
        print("H")
    elif selection == "2":
        print("Hello")
    elif selection == "3":
        print("Hello")
    elif selection == "4":
        print("Hello")
    elif selection == "5":
        print("Hello")
    elif selection == "6":
        print("Hello")
    else:
        loop = False



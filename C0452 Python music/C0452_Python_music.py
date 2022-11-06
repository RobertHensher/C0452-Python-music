## Music
## This shows artists, songs, number of plays. Implemented in nested dictionaries. Format example - key0: (key0:value0,key1:value1...)
music = {
        'Bob Dylan':{'end of the line':1013213, 'the boxer':654124, 'hurricane':52355205}, 
        'Madonna':{'hung up':1443176, 'frozen':3567406, 'material girl':145325},
        'MF DOOM':{'rap snitches':1412223, 'Sofa king':37638, 'doomsday':1543535},
        'Freddie Dredd':{'GTG':244534, 'WTH':543336, 'cha cha':1234148}
        }






## menu added for selection
## loop added so that selection can be presented until Q is pressed
while (True):
  
   print ("L = List")
   print ("A = Add")
   print ("D = Delete")
   print ("P = List popular songs")
   print ("Q = Quit")
   print('---------------------------------------')
   selection= input ("Make a selection: ") 



   if selection ==  'L':

       ## If L is pressed the list of songs will be shown
       print('---------------------------------------')
       print('List of songs:')
       print('---------------------------------------')
       for artist, songs, in music.items():
    
            for songtitle, playcount in songs.items():
             print(songtitle)
       print('---------------------------------------')



       # add option allows new song for whatever artist chosen

       continue
   elif selection ==  'A':
        artist = input("name of artist:")
        song = input("name of song:")
        music[artist] = {song:0}
        continue



   elif selection ==  'D':
       
      ## delete of song
        ## input of artist and input of song will delete from dictionary
         ## checking incorrect input for artist name and song
         artist = input("name of artist:")
         found = music.get(artist)
         if found:
             print('---------------------------------------')
             print ("artist was found- ") 
             print('---------------------------------------')
             song = input("name of song:")
             songfound = music.get(song)
             if songfound: 

                del(music[artist][song])
                print('---------------------------------------')
                print ("Song removed")
                print('---------------------------------------')
             else :
                print('---------------------------------------')
                print ("song was not found-")
                print('---------------------------------------')

                continue

         else :
             print('---------------------------------------')
             print ("artist was not found-")
             print('---------------------------------------')

        
             continue


         
          ## code searches through dictionary to find songs that are more than inputed number 
   elif selection ==  'P':
         NumPlaysInput = input ("input number of plays: ")
         if NumPlaysInput.isdigit() :
            print('Its a number')
         else :
             print('Its NOT a number')
             print('---------------------------------------')
             continue
         print ("List of songs: ")
         for artist, songs, in music.items():
            for songtitle, playcount in songs.items():
                if (int(NumPlaysInput)<playcount):
                    print(songtitle)
         print('---------------------------------------')
         continue





   elif selection ==  'Q':
        break
   else:
        print ("need to select from choices")
        continue 






















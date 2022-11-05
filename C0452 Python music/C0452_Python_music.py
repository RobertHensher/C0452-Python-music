## Music
## This shows artists, songs, number of plays. Implemented in nested dictionaries. Format example - key0: (key0:value0,key1:value1...)
music = {
        'Bob Dylan':{'end of the line':1013213, 'the boxer':654124, 'hurricane':52355205}, 
        'Madonna':{'hung up':1443176, 'frozen':3567406, 'material girl':145325},
        'MF DOOM':{'rap snitches':1412223, 'Sofa king':37638, 'doomsday':1543535},
        'Freddie Dredd':{'GTG':244534, 'WTH':543336, 'cha cha':1234148}
        }


## List of songs
## this bit of code lists the songs that are in the dictionary

print('---------------------------------------')
print('List of songs:')
print('---------------------------------------')
for artist, songs, in music.items():
    
    for songtitle, playcount in songs.items():
        print(songtitle)
print('---------------------------------------')




## delete of song
## input of artist and input of song will delete from dictionary
artist = input("name of artist:")
song = input("name of song:")
del(music[artist][song])




print('---------------------------------------')
print('List of songs:')
print('---------------------------------------')
for artist, songs, in music.items():
    
    for songtitle, playcount in songs.items():
        print(songtitle)
print('---------------------------------------')










#TU12
cont = 0
video_game_char = ['Jack Cooper','BT-7274','Captin Lastomosa','Captin Brigs','Droz']
while cont == 0:
    while input('Do you want to input a charichter to the list?') == 'yes':
        video_game_char.append(input('Input the name of the person'))
    else:
        print('goodbye')
        cont = 1
while cont == 0:
    while input('Do you want to input a another?') == 'no':
        cont = 1
        print('goodbye')
    else:
        video_game_char.append(input('Input the name of the person'))
print(video_game_char)
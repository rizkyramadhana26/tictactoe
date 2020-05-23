def take_player_step(number_of_steps):
    if number_of_steps % 2 == 1:
        player = 'X' #X starts first
    else: player = 'O'
    position = input('%s chooses ... (example: 5)' % player)
    while (position not in ['1','2','3','4','5','6','7','8','9']) or (game_matrix[int(position)-1] == 'X') or (game_matrix[int(position)-1] == 'O'):
        print('Not valid!')
        position = input('%s chooses ... (example: 5)' % player)
    game_matrix[int(position)-1] = player
def check():
    #horizontal check
    for i in [0,3,6]:
        if (game_matrix[i] == game_matrix[i+1]) and (game_matrix[i] == game_matrix[i+2]):
            print('Player %s wins!' % game_matrix[i])
            return True
        else: continue
    #vertical check
    for i in range(0,3):
        if (game_matrix[i] == game_matrix[i+3]) and (game_matrix[i] == game_matrix[i+6]):
            print('Player %s wins!' % game_matrix[i])
            return True
        else: continue
    #diagonal check
    if (game_matrix[0] == game_matrix[4]) and (game_matrix[0] == game_matrix[8]):
        print('Player %s wins!' % game_matrix[0])
        return True
    elif (game_matrix[2] == game_matrix[4]) and (game_matrix[2] == game_matrix[6]):
        print('Player %s wins!' % game_matrix[2])
        return True
    else: 
        return False
def display(list):
    for i  in range (0,9):
        if i % 3 != 2:
            print(list[i], end='') 
        else:
            print(list[i])
#THE GAME
game_matrix = ['1','2','3','4','5','6','7','8','9']
number_of_steps = 1
game_status = False
while game_status == False:
    print('Steps number ', number_of_steps)
    display(game_matrix)
    take_player_step(number_of_steps)
    game_status = check()
    if game_status == True:
        display(game_matrix)
        break
    number_of_steps = number_of_steps + 1
    if number_of_steps == 10:
        print('Tie!')
        display(game_matrix)
        game_status = True
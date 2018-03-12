
def printer(board):
    'print board with positions to choose'
    print('{}\n{}\n{}'.format(board[0], board[1], board[2]))

def instert_to_board(player, player_choice, board):
    '''inserting player to board return update board '''
    counter = 0
    for arr in board:
        for i, pos in enumerate(arr):
            if player_choice == counter:
                arr[i] = 'X' if player == 0 else 'O'
            counter += 1
    return board

def winner(tab,way_to_win):
    '''check who win. Return True when anybody win.'''
    for arr in way_to_win:
        if (0==tab[arr[0]]==tab[arr[1]]==tab[arr[2]]or
            1==tab[arr[0]]==tab[arr[1]]==tab[arr[2]]):
            return True

def draw(board):
    'when all fild are occupied in used_nums return True'
    return all(board)

def main_func(player, board_with_fields, used_nums, way_to_win):
    'main function'
    while True:
        choice = int(input('{} Choose position od 0-8: '.format('Player "X"' if player == 0 else 'Player "O"')))
        if 0 <= choice <= 8:
            # check if choosen position is empty
            if used_nums[choice] == '':
                # when is empty replace from '' to X or O
                used_nums[choice] = player
                # prints update table
                printer(instert_to_board(player, choice, board_with_fields))
                if winner(used_nums, way_to_win):
                    print('KoniecGry wygrał {}'.format('X' if player == 0 else 'O'))
                    break
                if draw(used_nums):
                    print('KoniecGry REMIS')
                    break
                # swith players
                if player == 0:
                    player = 1
                else:
                    player = 0
            else:
                print('field occupied try again')
        else:
            print('Wrong chooice try again 0-8')



# table to view
board_with_fields = [['0','1','2'],
                    ['3','4','5'],
                    ['6','7','8']]
# list with choosen positions
used_nums = ['','','','','','','','','']

way_to_win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[6,4,2]]
player = 0

# [0, 1, 2]
# [3, 4, 5]
# [6, 7, 8]

#main
if __name__ == '__main__':
    main_func(player, board_with_fields, used_nums, way_to_win)
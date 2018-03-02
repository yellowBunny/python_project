import random

def printer(tab):
    'print table with positions to choose'
    print('{}\n{}\n{}'.format(tab[0],tab[1],tab[2]))

def instert_to_tab(player=None,n=None):
    '''inserting player to table return update table
        player - X or O
        n - position number'''
    c=0
    for arr in tab:
        for i,pos in enumerate(arr):
            if n==c:
                arr[i]=player
            c += 1
    return tab

def winner(tab):
    '''check who win. Return True when anybody win.
    tab - used_nums'''
    for arr in way_to_win:
        if players[0]==tab[arr[0]]==tab[arr[1]]==tab[arr[2]] or players[1]==tab[arr[0]]==tab[arr[1]]==tab[arr[2]]:
            return True

def draw(tab):
    '''if draw True
    tab - used_nums'''
    return all([ele for ele in tab])

def AI_moves(tab):
    'Computer movments return index of empty field '
    print('AI moves')
    #print(tab)
    best_moves=[4,0,8,2,6,7,3,1,5]
    for i,choice in enumerate(best_moves):
        choice=best_moves[i]
        if sum(1 for i in [0,8] if tab[i]=='X')==2 or sum(1 for i in [2,6] if tab[i]=='X')==2 \
                and sum(1 for i in best_moves if tab[i])==3:
            choice = random.choice(best_moves[5:])
        choice = AI_win_or_block(choice,tab)
        if not tab[choice]:
            return choice

def AI_win_or_block(choice,tab):
    '''Ai advance movments
    when player have two fileds in row or columns AI block player,
    however when a AI have two fields in row or columns take third field to win '''
    # way to win
    for arr in way_to_win:
        if sum([1 for pos in arr if tab[pos]=='O'])>=2:
            advance_choice = [pos for pos in arr if tab[pos]=='']
            if advance_choice:
                #print('advance choice to win')
                return advance_choice[-1]
    # way to block
    for arr in way_to_win:
        if sum([1 for pos in arr if tab[pos] == 'X']) >= 2:
            advance_choice = [pos for pos in arr if tab[pos] == '']
            if advance_choice:
                #print('advance choice block')
                return advance_choice[-1]
    return choice

def human(choice=None):
    'Human movement return chossen empty field'
    while 1:
        choice = int(input('Human choice position od 0-8: '))
        if 0<=choice<=8:
            if used_nums[choice]=='':
                return choice
            else: print('field occupied try again')
        else: print('Wrong choice try again 0-8')


# varibles
tab = [['0','1','2'],
       ['3','4','5'],
       ['6','7','8']]

way_to_win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[6,4,2]]
used_nums = ['','','','','','','','','']
players = ['X','O']
player = 0

#main
if __name__ == '__main__':

#view tab
    printer(instert_to_tab())
    while True:
#set choice for player or AI
        choice = human() if player==0 else AI_moves(used_nums)
        used_nums[choice]=players[player]
# prints update table
        printer(instert_to_tab(players[player],choice))
#check if someon win
        if winner(used_nums):
            print('GAME OVER THE WINNER is {}'.format('HUMAN' if players[player]=='X' else 'AI'))
            break
# check if draw
        if draw(used_nums):
            print('GAME OVER IS DRAW')
            break
#swith between player and AI
        player += 1
        if player > 1: player = 0

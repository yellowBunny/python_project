# table to view
tab = [['1','2','3'],
       ['4','5','6'],
       ['7','8','9']]
# list with choosen positions
used_nums = ['','','','','','','','','']
# players
players = ['X','O']

way_to_win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[6,4,2]]

def IA(tab):
    best_moves = [4,0,2,6,8]
    n = best_moves[0]
    for arr in way_to_win:
        # way to win
        if sum([1 for pos in arr if used_nums[pos]=='O'])>=2:
            n = [pos for pos in arr if used_nums[pos]==''][-1]
            break
        # way to block
        if sum([1 for pos in arr if used_nums[pos] == 'X']) >= 2:
            n = [pos for pos in arr if used_nums[pos] == ''][-1]
            break

    return n



                                                # [0, 1, 2]
                                                # [3, 4, 5]
                                                # [6, 7, 8]



print(IA(used_nums))
# def printer(tab):
#     'print table with positions to choose'
#     print('{}\n{}\n{}'.format(tab[0],tab[1],tab[2]))
#
# def instert_to_tab(player,n):
#     '''inserting player to table return update table
#         player - X or O
#         n - position number'''
#     c=0
#     for arr in tab:
#         for i,pos in enumerate(arr):
#             if n==c:
#                 arr[i]=player
#             c += 1
#     return tab
#
# def winner(tab):
#     '''check who win. Return True when anybody win.
#     tab - used_nums'''
#     for arr in way_to_win:
#         if players[0]==tab[arr[0]]==tab[arr[1]]==tab[arr[2]] or players[1]==tab[arr[0]]==tab[arr[1]]==tab[arr[2]]:
#             return True
#
# def draw(tab):
#     '''if draw True
#     tab - used_nums'''
#     return all([ele for ele in tab])
#
# #main
#
# player = 0
# while True:
#     choice = int(input('{} Choose position od 1-9: '.format('Player "X"' if player==0 else 'Player "O"' )))
#     if 0<choice<=9:
#         #check if choosen position is empty
#         if used_nums[choice-1]=='':
#             # when is empty replace from '' to X or O
#             used_nums[choice-1]=players[player]
#             # prints update table
#             printer(instert_to_tab(players[player],choice-1))
#             if winner(used_nums):
#                 print('KoniecGry wygrał {}'.format(players[player]))
#                 break
#             if draw(used_nums):
#                 print('KoniecGry REMIS')
#                 break
#             #swith players
#             player += 1
#             if player > 1: player = 0
#         else: print('field occupied try again')
#     else: print('Wrong chooice try again 1-9')
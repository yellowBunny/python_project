l = ['X', 'X', 'X', '', '', 'X', 'O', 'X', ''] #0

way_to_win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]

print(all([1 if l[pos] else 0 for pos in arr if l[pos]] for arr in way_to_win))



# best_moves = [4, 0, 8, 2, 6, 7, 3, 1, 5]
# d = {tuple(key):[] for key in l}
#
# def win_in_row(tab, sign):
#     for arr in way_to_win:
#         if sum(1 for pos in arr if tab[pos] == '{}'.format(sign)) >= 2:
#             choice = [pos for pos in arr if not tab[pos]]
#             if choice:
#                 return '0' if choice[-1]==0 else choice[-1]
#
#
# for arr in l:
#     x = win_in_row(arr, 'X')
#     o = win_in_row(arr, 'O')
#     for i in best_moves:
#         if not arr[i]:
#             d[tuple(arr)] +=[i]
#             if x:
#                 d[tuple(arr)]+=[int(x)]
#             if o:
#                 d[tuple(arr)]+=[int(o)]
#             break
#
# print(d)
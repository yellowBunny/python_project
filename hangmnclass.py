
class Hangman:
    def __init__(self,word,moves,empty_lst):
        self.empty_lst = empty_lst
        self.word = word
        self.moves = moves
        self.words_to_append = []


    def way_to_lose(self):
        if self.moves>=len(self.word): return True

    def way_to_win(self):
        return all(ltr.isalpha() for ltr in self.empty_lst)


    def board(self,choice):
        indexes = []
        for i, ltr in enumerate(self.word):
            if ltr == choice:
                indexes += [i]
        for i in indexes:
            self.empty_lst[i] = choice


word = 'ser'
p1_list= ['_' for loop in range(len(word))]
p = Hangman('ser',0,p1_list)
#main

while 1:
    choice = input('Wpisz :')
    if choice in word and choice not in p.words_to_append:
        p.words_to_append+=[choice]
        p.board(choice)
        print(p.empty_lst)
        if p.way_to_win():
            print('You WIN GRATAS')
            break
    else:
        if choice in p.words_to_append:
            print('{} was choosen before'.format(choice))
        else:
            p.moves+=1
            print(p.empty_lst)
            print('{} not in word'.format(choice))
            if p.way_to_lose():
                print('YOu lose')
                break










class Hangman:
    '''SIMPLE GAME FOR TWO PLAYERS MUST FIND CORRECT WORD!
        The player give a letter if letter is in word show that letter in list
        otherwise lose his loses movments'''

    def __init__(self,word,moves,empty_lst):
# list with empty hiden elements
        self.empty_lst = empty_lst
# word who we look for
        self.word = word
# number of movmes
        self.moves = moves
# letters who we did guessed
        self.words_to_append = []

    def way_to_lose(self):
        'us used moves'
        if self.moves>=len(self.word): return True

    def way_to_win(self):
        'checking if we find all letters in word'
        return all(ltr.isalpha() for ltr in self.empty_lst)


    def board(self,choice):
        '''update a list with hidden letters
        if we guess list with hidden letters will be update'''
        indexes = []
        for i, ltr in enumerate(self.word):
            if ltr == choice:
                indexes += [i]
        for i in indexes:
            self.empty_lst[i] = choice


def main(instance,word):
    '''główna funkcja'''
    choice = input('Wpisz :')
    if choice in word and choice not in instance.words_to_append:
        instance.words_to_append += [choice]
        instance.board(choice)
        print(instance.empty_lst)
        if instance.way_to_win():
            print('You WIN GRATAS')
            return True
    else:
        if choice in instance.words_to_append:
            print('{} was choosen before'.format(choice))
        else:
            instance.moves += 1
            print(instance.empty_lst)
            print('{} not in word'.format(choice))
            if instance.way_to_lose():
                print('YOu lose')
                return True
#player 1
word1 = 'ser'
p1_list= ['_' for i in range(len(word1))]
p = Hangman(word1,0,p1_list)

#player 2
word2 = 'kajak'
p2_list= ['_' for j in range(len(word2))]
p2 = Hangman(word2,0,p2_list)

#main

if __name__ == '__main__':

    while 1:
        print('Player 1')
        if main(p,word1): break
        print('Player 2')
        if main(p2,word2): break
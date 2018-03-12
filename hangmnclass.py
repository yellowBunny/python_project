from random import choice

class Hangman:
    '''SIMPLE GAME FOR TWO PLAYERS. THEY MUST FIND CORRECT WORD!
        The player give a letter if letter is in word show that letter in list
        otherwise lose his loses movments'''

    def __init__(self,word, moves=None , empty_lst=None):
        # list with empty hiden elements
        self.empty_lst = empty_lst
        # word who we look for
        self.word = word
        # number of movmes
        self.moves = moves
        # valid letters who we did guessed
        self.words_to_append = []
        # all lerrets who we did guessed
        self.used_letters = []

    def way_to_lose(self):
        'check used moves'
        if self.moves >= len(self.word):
            return True

    def way_to_win(self):
        'checking if we find all letters in word'
        return all(ltr.isalpha() for ltr in self.empty_lst)


    def board(self, choice):
        '''update a list with hidden letters
        if we guess hidden letters list will be update'''
        indexes = []
        for i, ltr in enumerate(self.word):
            if ltr == choice:
                indexes += [i]
        for i in indexes:
            self.empty_lst[i] = choice
        return self.empty_lst



def define_players_name(player):
    'func define players name'
    name = ''
    while not name:
        name = input('Enter your name or nick name {}: '.format(player))
    else:
        return name

def word_to_guess():
    'func chooses randomly one word form list'
    list_with_words_to_guess = ['ser', 'kajak', 'gofry', 'frytki', 'lody',
                                'koń', 'czołg', 'byk', 'roślina']
    return choice(list_with_words_to_guess)


def main(instance, word, player_name):
    '''main function'''
    while True:
        #print list status  with guessed letters before choice
        print(instance.empty_lst, 'previously chosen letters {}'.format(instance.used_letters))
        choice = input('{} Enter guess letter : '.format(player_name))
        # append to used_letter list
        instance.used_letters += [choice]
        if choice in word and choice not in instance.words_to_append:
            instance.words_to_append += [choice]
            instance.board(choice)
            # print list status with guessed letters after choice
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
                break


#player 1
word1 = word_to_guess()
p1_list= ['_' for i in range(len(word1))]
p = Hangman(word1,0,p1_list)

#player 2
word2 = word_to_guess()
p2_list= ['_' for j in range(len(word2))]
p2 = Hangman(word2,0,p2_list)


#main

if __name__ == '__main__':

    player1 = define_players_name('Player 1')
    player2 = define_players_name('Player 2')

    while 1:
        if main(p,word1,player1):
            break
        print('-' * 50)
        if main(p2,word2,player2):
            break
        print('-' * 50)
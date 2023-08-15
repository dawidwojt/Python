from random import choice
t = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


# Returning numbers when new game is triggered
def clear_game():
    global t
    t = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


# Shows grid
def show():
    print(' TIC TAC TOE')
    game = f' {t[0]} | {t[1]} | {t[2]} \n' \
           f'-----------\n' \
           f' {t[3]} | {t[4]} | {t[5]} \n' \
           f'-----------\n' \
           f' {t[6]} | {t[7]} | {t[8]} \n'
    print(game)


# List of possible win combinations
def matches():
    global p1, p2, p3, p4, p5, p6, p7, p8, p9
    p1 = [t[0], t[1], t[2]]
    p2 = [t[3], t[4], t[5]]
    p3 = [t[6], t[7], t[8]]
    p4 = [t[0], t[3], t[6]]
    p5 = [t[1], t[4], t[7]]
    p6 = [t[2], t[5], t[8]]
    p7 = [t[0], t[4], t[8]]
    p8 = [t[2], t[4], t[6]]


# Computer artificial intelligence
def player_ai():
    matches()
    global i
    j = []

    if t.count('X') == 0 or (t.count('X') == 1 and t.count('O') == 0):
        wyb = [s for s in t if s.isdigit()]
        i = int(choice(wyb))
    elif t.count('X') == 1 and t.count('O') == 1:
        for li in (p1, p2, p3, p4, p5, p6, p7, p8):
            if 'O' in li and 'X' not in li:
                j.append(li)
        try:
            j_chosen = choice(j)
            j_chosen = j_chosen.remove('O')
            i = choice(j_chosen)
        except:
            j_chosen = [s for s in t if s.isdigit()]
            i = int(j_chosen[0])

    elif t.count('X') == 2 and t.count('O') == 1:
        ok2 = False
        for li in (p1, p2, p3, p4, p5, p6, p7, p8):
            if li.count('X') == 2 and li.count('O') == 0:
                li = [s for s in li if s.isdigit()]
                i = int(li[0])
                break
            elif 'O' in li and 'X' not in li:
                j.append(li)
                ok2 = True
            if ok2:
                j_chosen = choice(j)
                j_chosen = [s for s in j_chosen if s.isdigit()]
                i = int(j_chosen[0])
    else:
        ok = False
        for li in (p1, p2, p3, p4, p5, p6, p7, p8):
            if li.count('X') == 0 and li.count('O') == 2:
                li = [s for s in li if s.isdigit()]
                i = int(li[0])
                break
            if t.count('X') == 2 and t.count('O') == 0:
                i = (li.remove('X'))
                break
            elif t.count('O') == 1 and t.count('X') < 2:
                j.append(li)
                ok = True
            if ok:
                j_chosen = choice(j)
                j_chosen = [s for s in j_chosen if s.isdigit()]
                i = int(j_chosen[0])
            else:
                wyb = [s for s in t if s.isdigit()]
                i = int(choice(wyb))
    return int(i)


# Game brain
def game_tech(player_first, game_type):
    if player_first:
        player_1 = True
    else:
        player_1 = False
    n1 = n2 = []
    clear_game()
    k = 1
    game_ongoing = True
    while game_ongoing and k < 9:
        try:
            if player_1:
                n = int(input('Player 1: ')) - 1
                if n in n2 or n in n1:
                    print('\n Position already filled')
                else:
                    n1.append(n)
                    t[n] = 'X'
                    show()
                    player_1 = False
            else:
                if game_type == '2':
                    n = int(input('Player 2: ')) - 1
                    if n in n1 or n in n2:
                        print('\n Position already filled')
                    else:
                        n2.append(n)
                elif game_type == '1':
                    n = player_ai() - 1
                    n2.append(n)
                t[n] = 'O'
                show()
                player_1 = True
        except IndexError:
            print('\n Wrong input, please choose a place with number between 1 and 9')
            k += 1
        matches()
        for li in (p1, p2, p3, p4, p5, p6, p7, p8):
            if li[0] == li[1] == li[2]:
                if player_1 and game_type == '1':
                    print('Computer won')
                elif not player_1 and game_type == '1':
                    print('You won')
                elif player_1 and game_type == '2':
                    print('Player 2 won')
                elif not player_1 and game_type == '2':
                    print('Player 1 won')
                game_ongoing = False
        if k == 8:
            print('Match Draw')


# New game trigger
def gameplay(round):
    round += 1
    if round % 2 != 0:
        player_first = True
    else:
        player_first = False
    print('TIC TAC TOE')
    print('Player 1 uses X\n'
          'PLayer 2 uses O\n')
    game_type = input("Click 1 to play with a computer or 2 to play together with other player \n")
    show()
    game_tech(player_first, game_type)


# Asking user if they want to play again
def again():
    return input("Wanna play again? Y/N ").upper()


gameplay(0)
game_on = True
r = 0
while game_on:
    if again() == "Y":
        r += 1
        gameplay(r)
    elif again() == "N":
        game_on = False
    else:
        print("Wrong input, try again with Y or N key ")



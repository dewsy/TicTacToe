import os
clear = lambda: os.system('cls')

def step(): #Looks for user input
    while True:
        try:
            k = input("What's your step?")
            if int(k[1]) < 1 or int(k[1]) > 3 or str(k[0]) > 'c':
                raise ValueError
            break
        except:
            print('invalid input')
    return str(k[0] + k[1])

table = {'a1':'-', 'b1':'-', 'c1':'-', 'a2':'-', 'b2':'-', 'c2':'-', 'a3':'-', 'b3':'-', 'c3':'-',}

def lookforwin(loc): #Decides if the game is won or not
    collumn = [val for key, val in table.items() if loc[0] in key]
    row = [val for key, val in table.items() if loc[1] in key]
    if collumn[0] == collumn[1] == collumn[2]:
        return "win"
    elif row[0] == row[1] == row[2]:
        return "win"
    elif table['a1'] == table['b2'] == table['c3'] != '-':
        return "win"
    elif table['a3'] == table['b2'] == table['c1'] != '-':
        return "win"
    else: pass

def printtable(): #just prints out the table
    print('\n  a b c')
    print('1', table['a1'], table['b1'], table['c1'])
    print('2', table['a2'], table['b2'], table['c2'])
    print('3', table['a3'], table['b3'], table['c3'])

def turn(Z): #This a players turn
    loc = step()
    if table[loc] == 'X' or table[loc] == 'O':
        print('\nThat field is taken! You lost!')  #Scoring should be added later!
        quit()
    else:
        table[loc] = Z
        if lookforwin(loc) == "win":
            return "win"
        else:
            clear()
            printtable()

#This is where the game starts
clear()
printtable()
while True:
    print('\nX player comes:')
    if turn('X') == "win":
        printtable()
        print("\nX player won the game!")
        break
    if '-' not in table.values():
        print("\nIt's a tie!")
        break
    print('\nO player comes:')
    if turn('O') == "win":
        printtable()
        print("\nO player won the game!")
        break
    if '-' not in table.values():
        print("\nIt's a tie!")
        break
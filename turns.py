def step():
    while True:
        try:
            z = input("What's your step?")
            if int(z[1]) < 1 or int(z[1]) > 3 or str(z[0]) > 'c' :
                raise ValueError
            break
        except:
            print('invalid input')
    return str(z[0] + z[1])

table = {
    'a1' : '-', 'b1' : '-', 'c1' : '-',
    'a2' : '-', 'b2' : '-', 'c2' : '-',
    'a3' : '-', 'b3' : '-', 'c3' : '-',
}

def printtable():
    print('\n  a b c')
    print('1', table['a1'], table['b1'], table['c1'])
    print('2', table['a2'], table['b2'], table['c2'])
    print('3', table['a3'], table['b3'], table['c3'])

def turn(X):
    loc = step()
    if table[loc] == 'X' or table[loc] == 'O':
        print('\n That field is taken! You lost!')  #Scoring should be added later!
        quit()
    else:
        table[loc] = X
        printtable()

#This is where the game starts
printtable()
while True: #This should be broken if the game ends!
    print('\nX player comes:')
    turn('X')
    print('\nO player comes:')
    turn('O')

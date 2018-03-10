def step():
    while True:
        try:
            z = input("What's your next step?")
            if int(z[1]) < 1 or int(z[1]) > 3 or str(z[0]) > 'c' :
                raise ValueError
            break
        except:
            print('invalid input')
    return str(z[0] + z[1])

def printtable():
    print(table['a1'], table['a2'], table['a3'])
    print(table['b1'], table['b2'], table['b3'])
    print(table['c1'], table['c2'], table['c3'])



table = {
    'a1' : 'u',
    'a2' : 'u',
    'a3' : 'u',
    'b1' : 'u',
    'b2' : 'u',
    'b3' : 'u',
    'c1' : 'u',
    'c2' : 'u',
    'c3' : 'u',
}


printtable()
table[step()] = 'x'
printtable()

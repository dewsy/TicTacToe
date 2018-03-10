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

print(step())
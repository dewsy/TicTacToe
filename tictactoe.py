while True:
    try:
        z = input("What's your next step?")
        lett = str(z[0])
        num = int(z[1])
        print(lett)
        print(num)
        if num < 1 or num > 3 or lett != 'a' or lett != 'b' or lett != 'c' :
            raise ValueError
        break
    except:
        print("not valid input")

print('u even lift brah?')

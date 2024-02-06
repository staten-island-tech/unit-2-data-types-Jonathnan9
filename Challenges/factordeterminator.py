def factor_determinator(x):

    print(f"The factors of your number are ({x}) ")
    for i in range(1, x+1):
            if  x % i == 0:
                print(i)


number = int(input("Pick a number "))
factor_determinator(number)

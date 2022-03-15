def factorial(x):
    fact=1
    for no in range(1,x+1):
        fact =fact*no

    print('factorial is' ,fact)
    pass

factorial(7)
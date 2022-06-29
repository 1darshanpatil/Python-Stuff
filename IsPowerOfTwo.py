# Ev(x) ~ ispoweroftwo(x)

#This is one of my favourite codes cz its so fast....#


def Ev(x):
    if x==2:        return True
    elif x%2:       return False
    return Ev(x//2)


print(Ev(int(input('Enter integer to check if is power of 2: '))))

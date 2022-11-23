year = int(input())

def isleap(year):
    if year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

if isleap(year):
    print('yes')
else:
    print('no')
def isleap(year):
    if year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

DAYS_ON_MONTH = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

class Date:
    def __init__(self) -> None:
        self.year = int(input())
        self.month = int(input())
        self.day = int(input())

    # The day count based on Dec 31, 0
    @property
    def days(self):
        result = self.day

        for month in range(1, self.month):
            result += DAYS_ON_MONTH[month]
            if month == 2 and isleap(self.year):
                result += 1

        for year in range(self.year):
            if isleap(year):
                result += 366
            else:
                result += 365

        return result

start = Date()
end = Date()

print(end.days - start.days)
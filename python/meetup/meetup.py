from datetime import date


class MeetupDayException(Exception):
    pass


def meetup_day(year, month, day_of_the_week, which):
    day = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}[day_of_the_week]
    
    if which == "teenth":
        for i in [13, 14, 15, 16, 17, 18, 19]:
            if date(year, month, i).weekday() == day:
                return date(year, month, i)
    elif which in ["1st", "2nd", "3rd", "4th", "5th"]:
        which = {"1st": 0, "2nd": 1, "3rd": 2, "4th": 3, "5th": 4}[which]
        for i in range(1, (date(year if month < 12 else year + 1, (month + 1) if month < 12 else 1, 1) - date(year, month, 1)).days + 1):
            print(i)
            if date(year, month, i).weekday() == day:
                if which == 0:
                    return date(year, month, i)
                else:
                    which -= 1
    else:
        for i in reversed(range(1, (date(year if month < 12 else year + 1, (month + 1) if month < 12 else 1, 1) - date(year, month, 1)).days + 1)):
            if date(year, month, i).weekday() == day:
                return date(year, month, i)

    raise(MeetupDayException)

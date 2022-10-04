import re


s = "07:05:45PM"


def timeConversion(s):

    r = re.search("([0-2][0-9]):([0-5][0-9]):([0-5][0-9])([a-zA-Z]{2})", s)

    am = {
        "01": "01",
        "02": "02",
        "03": "03",
        "04": "04",
        "05": "05",
        "06": "06",
        "07": "07",
        "08": "08",
        "09": "09",
        "10": "10",
        "11": "11",
        "12": "00",
    }
    pm = {
        "01": "13",
        "02": "14",
        "03": "15",
        "04": "16",
        "05": "17",
        "06": "18",
        "07": "19",
        "08": "20",
        "09": "21",
        "10": "22",
        "11": "23",
        "12": "12",
    }

    if r.group(4).__eq__("AM"):
        new_string = s.replace(r.group(0), am[r.group(1)])
        hour = f"{new_string}:{r.group(2)}:{r.group(3)}"
        print(hour)

    elif r.group(4).__eq__("PM"):
        new_string = s.replace(r.group(0), pm[r.group(1)])
        hour = f"{new_string}:{r.group(2)}:{r.group(3)}"
        print(hour)
    return hour


timeConversion(s)

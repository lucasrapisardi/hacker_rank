grades = [73, 67, 38, 33]


def diff_to_round(grade):
    """Function to check the differente to next multiple of 5"""
    return grade % 5


def diff(grades):
    """Main function to execute list addition"""
    for grade in range(0, len(grades)):
        if grades[grade] < 38:
            continue
        else:
            dif = grades[grade]
            if diff_to_round(grades[grade]) == 3:
                dif += 2
                grades[grade] = dif
            elif diff_to_round(grades[grade]) == 4:
                dif += 1
                grades[grade] = dif
            else:
                continue
    return grades


print(diff(grades))

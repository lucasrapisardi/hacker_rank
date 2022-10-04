arr = [3, 1, 9, 7, 5]


def miniMaxSum(arr):
    max = 0
    mini = 0

    sorr = sorted(arr)
    rev = sorted(arr, reverse=True)

    for i in rev[0:4]:
        max += i

    for j in sorr[0:4]:
        mini += j

    print(mini, max)

    return


miniMaxSum(arr)

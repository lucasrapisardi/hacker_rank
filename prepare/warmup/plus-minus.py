elements = 0
positives = 0
negatives = 0
zeros = 0
pos = 0
neg = 0
zero = 0

arr = [1, 2, 3, -1, -2, -3, 0, 0]


def positive(positives):
    for i in arr:
        if i > 0:
            positives += 1
    return positives


def negative(negatives):
    for i in arr:
        if i < 0:
            negatives += 1
    return negatives


def zero(zeros):
    for i in arr:
        if i == 0:
            zeros += 1
    return zeros


def get_elements(e):
    """Calculando a quantidade de itens na lista"""
    for i in arr:
        e += 1
    return e


def radios(s):
    radios = s / elements
    return radios


elements = get_elements(elements)
positives = positive(positives)
negatives = negative(negatives)
zeros = zero(zeros)

print("{:.6f}".format(radios(positives)))
print("{:.6f}".format(radios(negatives)))
print("{:.6f}".format(radios(zeros)))

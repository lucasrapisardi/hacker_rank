arr = [-4, 3, -9, 0, 4, 1]
def plusMinus(arr):
    zero = 0 
    positive = 0
    negative = 0

    elements = len(arr)
    
    for i in arr:
        if i == 0:
            zero += 1
        if i > 0:
            positive += 1
        if i < 0:
            negative += 1

    zeroes = zero/ elements
    positives = positive/ elements
    negatives = negative/ elements

    print("{:.6f}".format(positives))
    print("{:.6f}".format(negatives))
    print("{:.6f}".format(zeroes))
    return

plusMinus(arr)

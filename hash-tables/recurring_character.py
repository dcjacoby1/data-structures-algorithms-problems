def recurring_int(array):
    dict = {}
    for i in range(len(array)):
        if (dict[array[i]] != None):
            return array[i]
        else:
            dict[array[i]] = 0
    return None

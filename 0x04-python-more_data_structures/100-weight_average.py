def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    div = 0
    for k in my_list:
        average += k[0] * k[1]
        div += k[1]
    return float(average / div)

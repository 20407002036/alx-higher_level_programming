#!/usr/bin/python3
def weight_average(my_list=[]):
    # Get the weight and leave
    if len(my_list) == 0:
        return 0
    scores = [score*weight for (score, weight) in my_list]
    return sum(scores) / sum([weight for (score, weight) in my_list])

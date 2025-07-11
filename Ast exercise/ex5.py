def flatten(lst):
    return list(x for sublist in lst for x in sublist)

print(flatten([[1,2,3],[4,5],[6,7],[[7,8,9]]]))
def kerulet(a, *list):
    if len(list) == 0:
        return 4*a
    if len(list) == 1:
        return 2* a + 2 * list[0]
    k = a
    for side in list:
        k += side
    return k
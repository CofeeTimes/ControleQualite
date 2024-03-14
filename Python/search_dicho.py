def search(t, length, e):
    start = 0
    end = length - 1
    find = False
    i = -1
    
    while((find != True) and (start < end)):
        m = (int) ((start + end) / 2)
        if(t[m] == e):
            find = True
            i = m
        else:
            if(t[m] < e):
                start = m + 1
            else:
                end = m - 1
    return i
def lists(lst):
    res = []
    for s in lst:
        if isinstance(s, list):
            for l in lists(s):
                res.append(l)
        else:
            res.append(s)
    return res


fl = lists([1,1,1,1,1,1,[2,2,2,2,2,2], [2,2,[3,3,[4,4,4,4,4,4], 3,3,3,3],2,2,2,2,2], 1])
print(fl)
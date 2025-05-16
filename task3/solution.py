def appearance(intervals):
    ls, le = intervals['lesson']
    ps = intervals['pupil']
    ts = intervals['tutor']

    pupil = []
    for i in range(0, len(ps), 2):
        s = max(ps[i], ls)
        e = min(ps[i+1], le)
        if s < e:
            pupil.append((s, e))

    tutor = []
    for i in range(0, len(ts), 2):
        s = max(ts[i], ls)
        e = min(ts[i+1], le)
        if s < e:
            tutor.append((s, e))

    def merge(lst):
        lst.sort()
        res = []
        for s, e in lst:
            if res and s <= res[-1][1]:
                res[-1] = (res[-1][0], max(res[-1][1], e))
            else:
                res.append((s, e))
        return res

    pupil = merge(pupil)
    tutor = merge(tutor)


    i = j = 0
    total = 0
    while i < len(pupil) and j < len(tutor):
        start = max(pupil[i][0], tutor[j][0])
        end = min(pupil[i][1], tutor[j][1])
        if start < end:
            total += end - start
        if pupil[i][1] < tutor[j][1]:
            i += 1
        else:
            j += 1
    return total




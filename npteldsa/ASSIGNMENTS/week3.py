
p=[]
def remdup(l):
    for i in l:
        if i in p:
            p.remove(i)
        p.append(i)
    return p


lst=[]
def splitsum(l):
    pos = 0
    neg = 0
    for i in l:
        if i<0:
            neg+= i*i*i
        else:
            pos+= i*i
    lst.append([pos,neg])
    return lst[0]

def matrixflip(m,d):
    if d=='h':
        return [i[::-1] for i in m]
    elif d=='v':
        return m[::-1]
    else:
        return m
lust=[]
def listtype(l):
    return(type(l) == type([]))

def flatten(l):
    listtype(l)
    for i in l:
        if listtype(i)==False:
            lust.append(i)
        else:
            flatten(i)

    return lust

print(flatten([1,2,[3],[4,[5,6]]]))

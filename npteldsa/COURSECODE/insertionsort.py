def insertionsort(l):
        for i in range(len(l)):
            pos=i
            while pos>0 and l[pos]<l[pos-1]:
                (l[pos],l[pos-1])=(l[pos-1],l[pos])
                pos=pos-1
        return(l)

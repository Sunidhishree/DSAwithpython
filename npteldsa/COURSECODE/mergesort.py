def merge(a,b):
    l=[]
    i=0
    j=0
    m=len(a)
    n=len(b)
    while i+j<m+n:
        if i==m:
            l.append(b[j])
            j+=1
        elif j==n:
            l.append(a[i])
            i+=1
        elif a[i]<=b[j]:
            l.append(a[i])
            i+=1
        elif b[j]<a[i]:
            l.append(b[j])
            j+=1
    return l

def mergesort(a,l,r):
    if r-l<=1:
        return a[l:r]

    mid=(l+r)//2
    L=mergesort(a,l,mid)
    R=mergesort(a,mid,r)
    return merge(L,R)

arr=[1,3,5,7,89,4,56]
sorted_arr = mergesort(arr, 0, len(arr))
print(sorted_arr)

#time=o(n)

def bsearch(seq,k,high,low):
        mid=(high+low)/2
        if k<=high and k>mid:
            return(bsearch(seq,k,high,mid))
        elif k <mid and k >=low:
            return (bsearch(seq, k, mid, low))
        elif k==mid:
            return True
        else:
            return False

#time takes in O(n)=t(n/2log2(n))
def prime(a):
    for i in range(2, (a // 2) + 1):
        if a % i == 0:
            return False
    return True


def primepartition(b):
    for i in range(2, b):
        if prime(i) and prime(b - i):
            return True
    return False


def odd(f):
    if f % 2 == 0:
        return False
    else:
        return True


def matched(st):
    k = 0
    for i in st:
        if i == "(":
            k += 1

        elif i == ")":
            k -= 1

    if odd(k):
        return False
    return True


def rotatelist(l, n):
    if n > len(l):
        n = n % len(l)
    if n == 0:
        return l

    return l[n:] + l[:n]

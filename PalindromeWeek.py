import calendar as cl
def ispalindrome(st):
    if st[::-1] == st: return True
    return False
def isweekpalindrome(yr, m, d):
    r0, r1 = d, cl.monthrange(yr, m)[1]
    if d+7 > r1: return False, None
    wik = []
    for d0 in range(d, d+8):
        st = f"{m}{d0}{yr%100}"
        if ispalindrome(st) == False: return False, None
        wik.append(st)
    return True, wik
dic = {}
for y in range(2010, 2100):
    for m0 in range(1, 13):
        st, en = cl.monthrange(y, m0)
        for dx in  range(st, en+1):
            temp = isweekpalindrome(y, m0, dx)
            if temp[0]:
                dic[y] = temp[1]
#isweekpalindrome(2019, 9, 10)
for yr in dic:
    print(yr, dic[yr])

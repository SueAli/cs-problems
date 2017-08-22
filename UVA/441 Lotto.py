while True:
    try:
        s = list(map(int, input().split()))
        k = s[0]
        if k == 0 :
            break
        s = s[1:]
        for a in range(0,k - 5 ):
            for b in range(a+1, k-4):
                for c in range(b+1, k -3):
                    for d in range(c+1, k-2):
                        for e in range(d+1, k-1):
                            for f in range(e+1, k):
                                print (str(s[a])+" "+
                                       str(s[b]) +" "+
                                       str(s[c]) + " " +
                                       str(s[d])+" "+
                                       str(s[e])+" "+
                                       str(s[f]))

    except:
        break
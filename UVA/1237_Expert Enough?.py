def findMaker(db,p):
    maker = "UNDETERMINED"
    cnt = 0 
    for i in range(0,len(db)):
        if p >= db[i][1] and p <= db[i][2]:
            cnt += 1
            maker = db[i][0]
            if cnt > 1:
                break
    if cnt == 1:
        return maker
    
    return "UNDETERMINED"


T = int(input())
while T > 0 :
    T -= 1
    d = int(input())
    db_rec = []
    while d > 0 :
        d -= 1
        maker, l, h = input().split()
        l,h = int(l),int(h)
        db_rec.append((maker,l,h))
    q= int(input())
    queries = []
    while q > 0 :
        q -= 1
        x = int(input())
        print (findMaker(db_rec,x))
    if T:
        print("")
        


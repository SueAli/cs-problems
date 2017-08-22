while True:
    try:
        T = int(input())

        while T > 0 :
            T -= 1

            n = int(input())
            a_list = list(map(int,input().split()))
            b_sum = 0

            for i in range(n-1,0,-1):
                tmp = 0
                for j in range(i-1,-1,-1):
                  if a_list[j] <= a_list[i]:
                      tmp += 1
                b_sum += tmp
            print (b_sum)


    except:
        break
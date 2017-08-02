#   10986 - Sending email - UVA
# https://uva.onlinejudge.org/external/109/10986.pdf
import heapq
import  sys
class edge:
    def __init__(self,l,d):
        self.end = d
        self.latency = l
    def __lt__(self, other):
        if self.latency == other.latency:
            return self.end < other.end
        return self.latency < other.latency

while True :
    try:
        T = int(input())
        for tt in range(T):
            l = input()
            n,m,s,t = map(int,l.split())

            adj_list = [[] for _ in range(n)]
            all_latency = [sys.maxsize for _ in range(n)]
            heap_min = []

            for i in range(m): # Time = E
                s_d_w = input()
                src,dist,w = map(int,s_d_w.split())
                adj_list[src].append(edge(w,dist))
                adj_list[dist].append(edge(w,src))

            # Dijkstra's - Time complexity is O((E+V)* log V)
            # Greedy algorithm
            all_latency[s] = 0
            heapq.heappush(heap_min,edge(0,s))

            while heap_min:
                e = heapq.heappop(heap_min)
                for e_v in adj_list[e.end]:
                    if all_latency[e.end] + e_v.latency < all_latency[e_v.end]: # lazy deletion
                        all_latency[e_v.end] = all_latency[e.end] + e_v.latency
                        heapq.heappush(heap_min, edge(all_latency[e_v.end],e_v.end))

            if all_latency[t] == sys.maxsize:
                print("Case #"+str(tt+1)+": "+ "unreachable")
            else:
                print("Case #"+str(tt+1)+": "+ str(all_latency[t]))




    except:
        break
from heapq import heappush, heappop
import  sys
class word_prop:
    def __init__(self,sub_len,end, lang):
        self.lang = lang
        self.end_word = end
        self.chain_len = sub_len

    def __lt__(self, other):
        return self.chain_len < other.chain_len


while True:
    M = int(input())
    if M == 0:
        break
    src_lang , dst_lang = input().split()
    lang_mapping = {}
    relations = {}
    idx= 0

    for i in range(M):
        I1,I2,P = input().split()
        if I1 not in lang_mapping:
            lang_mapping[I1] = idx
            idx += 1
        if I2 not in lang_mapping:
            lang_mapping[I2] = idx
            idx += 1
        key = sorted([lang_mapping[I1], lang_mapping[I2]])
        if  key not in relations:
            relations[key] = []
        relations[key].append(P)

    lang_related = [[0 for c in range(idx)]for r in range(idx)]
    lang_diff =  [[sys.maxsize for c in range(idx)]for r in range(idx)]
    for pair in relations:
        lang_related[pair[0]][pair[1]] = 1
        lang_related[pair[1]][pair[0]] = 1

    src_lang_idx , dst_lang_idx = lang_mapping[src_lang], lang_mapping[dst_lang]

    q = []
    start = word_prop(0,None,src_lang_idx)
    lang_diff[src_lang_idx][src_lang_idx]  = 0

    heappush(q,start)

    while q:
        word = q.pop() # min queue based on chain len
        for dst in range(idx):
            if dst != word.lang  and lang_related[word.lang][dst] == 1:
                pair = sorted([word.lang,dst])
                for w in relations[pair]:
                    if word.end_word is not None and w[0] ==  word.end_word[0]:
                        continue
                    subSeq_len = word.chain_len + len(w)
                    if subSeq_len < lang_diff[word.lang][dst]:
                        lang_diff[word.lang][dst] = subSeq_len
                        heappush(q,word_prop(subSeq_len,w,dst))



        if lang_diff[src_lang_idx][dst_lang_idx] == sys.maxsize:
            print ("impossivel")
        else:
            print lang_diff[src_lang_idx][dst_lang_idx]








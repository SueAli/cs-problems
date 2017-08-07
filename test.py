#!/bin/python3

import sys
import bisect 

def solve(s, k):
    # Complete this function
    occur_dic = {}
    for i in range(len(s)):  # key = char , value = [cnt,list of idxs] 
        if s[i] in occur_dic: 
            occur_dic[s[i]][0] += 1 
            occur_dic[s[i]][1].append(i)
        else:
            occur_dic[s[i]] = [1,[i]]
    distinct_chars = sorted(occur_dic.keys(), reverse = True)
    res_sub = []
    curr_idx = -1 
    for c in distinct_chars : 
        if occur_dic[c][0] < k : 
            continue
        char_occr = occur_dic[c][1]
        tmp_idx = bisect.bisect_left(char_occr, curr_idx)
        if len(curr_idx) - tmp_idx >= k :
            for j in range(tmp_idx,len(char_occr)):
                pos = char_occr[j]
                res_sub.append(s[pos])
                curr_idx = pos

    return "".join(res_sub)


if __name__ == "__main__":
    s = input().strip()
    k = int(input().strip())
    result = solve(s, k)
    print(result)

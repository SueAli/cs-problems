# 429 - Word Transformation
from collections import deque

def calcDiff(word1,word2):
    if len(word1) == len(word2):
        diff_cnt = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff_cnt += 1
        if diff_cnt ==1 :
            return  1
    return 0


while True:
    try:
        T = int(input())
        input() # read blank line
        for tt in range(T):
            dict_words = []
            words_mapping = {}
            idx = 0
            while True:
              line = input()
              if line == "*":
                    break
              dict_words.append(line)
              words_mapping[line] = idx
              idx+= 1
            w_cnt = len(dict_words)
            adj_list = [[] for _ in range(w_cnt )]

            for i in range(len(dict_words)):
                for j in range(i+1, len(dict_words)):
                    if calcDiff(dict_words[i],dict_words[j]) == 1:
                        adj_list[i].append(j)
                        adj_list[j].append(i)

            while True:
              t_input = input()

              if  not t_input :
                break
              visited = [False for _ in range(w_cnt)]
              w1,w2 = t_input.split()
              start,end =  words_mapping[w1],  words_mapping[w2]
              q= deque()
              q.append((0,start))
              visited[start] = True
              while q :
                  steps, curr_word_id = q.popleft()
                  if curr_word_id == end:
                    print(dict_words[start]+" "+dict_words[curr_word_id]+" "+str(steps))

                    break
                  for next_w in adj_list[curr_word_id]:
                      if not visited[next_w]:
                        q.append((steps+1,next_w))
                        visited[next_w] = True
            if tt < T-1:
              print()
    except:

        break
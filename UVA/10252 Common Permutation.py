# 10252 Common Permutation

from collections import Counter
import sys
def getCommonPerm(a, b):
  res = []
  a_cnt = Counter(a)
  b_cnt = Counter(b)
  for a_chr, a_freq in a_cnt.items():
    if a_chr in b_cnt:
      occr = min(a_freq, b_cnt[a_chr])
      while occr > 0 :
        occr -= 1
        res.append(a_chr)
  res.sort()
  return "".join(res)

while True:
  try:
    # Reading should be done in another way
    a = input().strip()
    b = input().strip()
    if not a and not b :
      break

    com_perm = getCommonPerm(a,b)
    print(com_perm)
  except :
    break
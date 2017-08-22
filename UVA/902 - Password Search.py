from collections import defaultdict
while True:
  try:
    password =""
    max_ocr = 0
    p_len,txt = input().split()
    p_len = int(p_len)
    if p_len > 0:
      i = 0
      found_patterns = defaultdict(int)
      while i < len(txt):
          j = i+p_len-1

          if j < len(txt):
              curr_pat = txt[i:j+1]
              found_patterns[curr_pat] += 1
          else:
              break
          i += 1

      for k,v in found_patterns.items():
          if v > max_ocr:
              max_ocr = v
              password = k
    print (password)
  except:
    break



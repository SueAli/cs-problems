
def isCorrect(q):
    q = q.strip()
    a = ""
    b = ""
    c = ""
    op = ""
    i,j = 0,0
    while j < len(q) and q[j].isdigit():
        j += 1
    a = q[i:j]
    op = q[j]
    j += 1
    i = j
    while j < len(q) and q[j].isdigit():
        j += 1
    b= q[i:j]


    j += 1
    c = q[j:]

    res = 0
    if a == "" or b =="" or op == "":
      return 0

    if op =='+':
      res = int(a) + int(b)
    else:
      res = int(a) - int(b)
    if c=="" or c.strip() == "?" or int(c) != res :
        return 0
    else :
        return 1

correct_ans = 0
x = input()
while x :
  correct_ans += isCorrect(x)
  x = input()
print (correct_ans)

import string
class Pos:
  def __init__(self,i,j):
    self.row = i
    self.col = j

def fillKeyMat(key_txt, key_mat):
  visited= set()
  all_letters = []

  for c in key_txt:
    if c != ' ' and c != 'q' and c not in visited:
      all_letters.append(c.upper())
      visited.add(c)

  for c in string.ascii_lowercase:
    if c not in visited and c != 'q':
      all_letters.append(c.upper())
  k = 0
  for i in range(len(key_mat)):
    for j in range(len(key_mat[0])):
      key_mat[i][j] = all_letters[k]
      k += 1

def getPos(char, key_mat):
  for i in range(len(key_mat)):
    for j in range(len(key_mat[0])):
      if key_mat[i][j] == char:
         return Pos(i,j)
  return None


def mapChars(chrs, key_mat):
  enc = ""
  first = getPos(chrs[0], key_mat)
  second = getPos(chrs[1], key_mat)
  if first.row == second.row:
    enc = key_mat[first.row][(first.col+1) % 5]+ key_mat[second.row][(second.col+1) % 5]
  elif first.col == second.col:
     enc = key_mat[(first.row+1)%5][first.col]+ key_mat[(second.row+1)%5][second.col]
  else:

      enc = key_mat[first.row][second.col] + key_mat[second.row][first.col]

  return enc





n = int(input())
while n > 0:
  n -= 1
  k_txt = input()
  key_matrix = [[' ' for i in range(5)] for j in range(5)]
  orig_msg = input()
  orig_msg = orig_msg.replace(" ","")
  enc_msg = ""
  fillKeyMat(k_txt, key_matrix)

  i = 0
  while i < len(orig_msg):
    j = i+1
    two_char = ""
    if j == len(orig_msg) or orig_msg[i] == orig_msg[j]:
      two_char = orig_msg[i].upper() + 'X'
    else:
      two_char = orig_msg[i].upper() + orig_msg[j].upper()

    enc_msg += mapChars(two_char, key_matrix)
    if j < len(orig_msg) and orig_msg[i] == orig_msg[j]:
      i += 1
    else:
      i += 2
  print(enc_msg)











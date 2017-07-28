def getNext(R, C , r,c, ori, inst, arena):
  new_r , new_c , new_ori = r , c, ori
  if inst == 'D':
    if ori == 'N':
      new_ori = 'L'
    elif ori == 'L':
      new_ori = 'S'
    elif ori == 'S':
      new_ori = 'O'
    else:
      new_ori = 'N'
  elif inst == 'E':
    if ori == 'N':
      new_ori = 'O'
    elif ori == 'O':
      new_ori = 'S'
    elif ori == 'S':
      new_ori = 'L'
    else:
      new_ori= 'N'
  elif inst =='F':
    if ori == 'N':
      new_r,new_c = r-1,c
    elif ori == 'L':
      new_r, new_c = r , c+1
    elif ori == 'O':
      new_r,new_c = r, c-1
    else:
      new_r, new_c = r + 1, c
  # Validate next location
  if (new_r < 0 or
  new_c < 0 or
  new_r == R or
  new_c == C or
  arena[new_r][new_c]=='#'):
    return (r,c,ori)
  return (new_r,new_c,new_ori)


def collectStickers(rows,cols,arena,start_i, start_j, start_ori, instructions):
  #print (rows,cols,arena,start_i, start_j, start_ori, instructions)
  i = 0
  stickers_cnt = 0
  curr_r, curr_c, curr_ori = start_i, start_j, start_ori
  while i < len(instructions):
    curr_r, curr_c, curr_ori = getNext(rows, cols, curr_r, curr_c,curr_ori,  instructions[i],arena)
    if arena[curr_r][curr_c] == '*':
      stickers_cnt += 1
      arena[curr_r][curr_c] = '.'
    i += 1
  return stickers_cnt




while True:
  N,M,S = map(int,input().split())
  if N == 0 and M == 0 and S == 0 :
    break
  else:
    tmp_arena = []
    start_r, start_i , start_or = None, None, None
    for i in range(N):
      row = input()
      l = []
      for j in range(M):
        if row[j] in ('S', 'N', 'O', 'L'):
          start_i  = i
          start_j = j
          start_or = row[j]
        l.append(row[j])
      tmp_arena.append(l)
    instructions = input()
    res = collectStickers(N, M,tmp_arena, start_i,start_j, start_or, instructions)
    print(res)

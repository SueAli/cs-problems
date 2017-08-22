def mapFn(c):
    if c =="/":
        return  '0'
    else:
        return  '1'


while True:
  try:
    n = int(input())
    while n > 0 :
      n -= 1
      bin_mat = []
      # Start Reading the matrix
      msg_mat = []
      final_msg = ''
      for i in range(10):
        line = input()
        if i in [ 0, 9]:
          continue
        m = len(line)
        line = line[1:m-1]
        tmp = [ mapFn(c) for c in line]
        bin_mat.append(tmp)

      chr_cnt = len(bin_mat[0])

      for cc in range(chr_cnt):
        col_data =''
        for ii in range(7,-1,-1):
          col_data += bin_mat[ii][cc]

        ascii_val = int(col_data,base=2)

        final_msg += chr(ascii_val)

      print(final_msg)
      if n >0:
        input()


  except:
    break

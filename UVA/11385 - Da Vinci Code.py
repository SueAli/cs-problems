import string

while True:
  try:
    T = int(input())
    while T > 0 :
      T -= 1
      n = int(input())
      m = 100

      in_fib = list(map(int, input().split()))
      ciper_txt = input()

      fib_ser = [ i+1 for i in range(m)]
      decrypted_msg = ["#" for _ in range(m)]

      for i in range(2,m):
        fib_ser[i] = fib_ser[i-1] + fib_ser[i-2]

      msg_hash_t = {}
      j = 0

      max_fib = 0
      for i in range(len(ciper_txt)):
        if ciper_txt[i] in string.ascii_uppercase:
          msg_hash_t[in_fib[j]] = ciper_txt[i]
          j += 1
          if j == len(in_fib):
            break


      # build o/p msg
      for i in range(m):
        if fib_ser[i] in  msg_hash_t:
          max_fib = max(max_fib,i )
          decrypted_msg[i] = msg_hash_t[fib_ser[i]]

      final_msg = "".join(decrypted_msg[0:max_fib+1])
      print(final_msg.strip().replace("#"," "))

  except:
    break
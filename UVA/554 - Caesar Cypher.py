import string
def decMsgByK(msg, k):
  all_letters = ' '+string.ascii_uppercase
  gen_msg = ''
  for c in msg:
    old_ascii = 0 # for space char
    if c != ' ':
      old_ascii = ord(c)- ord('A') + 1
    new_ascii = (old_ascii + k ) % 27
    gen_msg += all_letters[new_ascii]
  return gen_msg
found = False
while True:
  try:
    if found:
      break
    words_dic = set()
    while True :
      word = input()
      if word == '#' :
        break
      words_dic.add(word)
    enc_msg = input()
    matched_cnt = 0
    dec_msg_list = None
    for k in range(1,27):
      curr_msg = decMsgByK(enc_msg, k)
      #print(curr_msg)
      w_list = curr_msg.split()
      found_in_dic = 0
      for w in w_list:
        if w in words_dic:
          found_in_dic += 1
      if found_in_dic > matched_cnt:
        matched_cnt = found_in_dic
        dec_msg_list = w_list
    i = 0
    tmp = ""
    while i < len(dec_msg_list):
        if tmp == "":
          tmp = dec_msg_list[i]
        elif (len(tmp) +1 + len(dec_msg_list[i])) <= 60:
          tmp = tmp + " "+ dec_msg_list[i]
        else:
          print(tmp)
          tmp = dec_msg_list[i]
        i += 1
    if tmp != "": # print last line
      print(tmp)

    found = True



  except:
    break

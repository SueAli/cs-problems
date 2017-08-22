def isTheorem(me_txt):
    front_symb = 0
    mid_symb = 0
    back_symb = 0
    i = 0
    while i < len(me_txt) and me_txt[i] != 'M':
        if me_txt[i] == '?':
            front_symb += 1
        else:
            return "no-theorem"
        i += 1

    if i == len(me_txt): # 'M' Not found
        return "no-theorem"
    else:
        i += 1 # to pass the 'M' char
        while i < len(me_txt) and me_txt[i] != 'E':
            if me_txt[i] == '?':
                mid_symb += 1
            else:
                return "no-theorem"
            i += 1
        if i == len(me_txt) : # 'E' char not found
            return "no-theorem"
        else:
            i+= 1
            while i < len(me_txt):
                if me_txt[i] == '?':
                    back_symb += 1
                else:
                    return 'no-theorem'
                i += 1
    if mid_symb >= 1 and back_symb > front_symb  and back_symb > mid_symb:
        return 'thoerem'
    return 'no-thoerem'


n = int(input())
while n > 0 :
    n -= 1
    me_txt = input()
    print (isTheorem(me_txt))



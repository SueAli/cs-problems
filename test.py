class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        
        def decodeRec(str_, curr_idx):
            res =""
         
            if curr_idx[0] >= len(str_) : # it is the end  so return -1 
                return  res 
            
            else:
                
                # if  str_[curr_idx[0]] == ']':
                #     curr_idx[0] += 1
                #     return -1, res  
                
                if str_[curr_idx[0]] in ('[',']'): # 1 means continue 
                    curr_idx[0] += 1
                    return  res  
                
                elif not str_[curr_idx[0]].isdigit(): # it is a char 
                    prev = curr_idx[0]
                    curr_idx[0] += 1
                    return str_[prev]
            
                else: # it is a digit 
                    j = curr_idx[0] 
                    repeat_cnt = '0'
                    while j < len(str_) and str_[j].isdigit():  
                        repeat_cnt += str_[j]
                        j += 1
                        curr_idx[0] = j 

                    repeat_cnt = int(repeat_cnt)
                    final_res = ''
                    print (repeat_cnt)
                    while curr_idx[0] < len(str_) and str_[curr_idx[0]] != ']':
                        res +=  decodeRec(str_, curr_idx)
                        #res += tmp_res
                    while repeat_cnt > 0: 
                        final_res+= res
                        repeat_cnt -= 1
                            
                    return final_res 
                        
        decoed_str =''
        idx = [0]
        while idx[0] < len(s):
            decoed_str +=  decodeRec(s, idx)      
        return decoed_str
                
                
                
            
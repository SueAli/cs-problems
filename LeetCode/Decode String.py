# Decode String

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        Time complexity is O(n)
        Space complexity is O(n) for recursion stack
        """
        def decodeStrRec(s,idx , s_stack):
            curr_str = ''

            while idx[0] < len(s) and s[idx[0]] != ']':

                if not s[idx[0]].isdigit():
                    if s[idx[0]] != '[':
                        curr_str+= s[idx[0]]
                    idx[0] += 1

                else: # is digit
                    repeat_cnt =''
                    while idx[0]< len(s) and s[idx[0]].isdigit():
                        repeat_cnt += s[idx[0]]
                        idx[0]+= 1
                    s_stack.append(int(repeat_cnt))

                    curr_str += decodeStrRec(s,idx,s_stack)
            if idx[0] == len(s)   :
                return curr_str


            idx[0] += 1
            cnt = s_stack.pop()
            print(cnt)
            final_res = ''
            while cnt > 0 :
                final_res += curr_str
                cnt -= 1
            return final_res


        return decodeStrRec(s,[0] ,[])





import math
# Evaluate Reverse Polish Notation
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        Time Complexity is O(n)
        Space Complexity is O(n)
        # Stack
        """
        oper_stack = []
        for s in tokens:
            #print oper_stack
            if s not  in ('+', '-','*', '/'):
                oper_stack.append(int(s))
                continue
            if len(oper_stack) >=2:
                oper1 = oper_stack.pop()
                oper2 = oper_stack.pop()
                r = 0
                if s == '+':
                    r = oper1 + oper2
                elif s == '-':
                    r = oper2 - oper1
                elif s == '*':
                    r = oper2 * oper1
                else:
                    r = math.trunc(float(oper2) / oper1)
                oper_stack.append(r)
        if oper_stack:
            return oper_stack[-1]
        return 0


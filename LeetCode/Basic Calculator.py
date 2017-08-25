from collections import deque

# Time complexity is O(n)
# Space complexity is O(n)

class Solution(object):
    def eval(self,exp, idx):
        operands = deque([0])
        operators = deque()

        while idx[0] < len(exp ) and exp[idx[0]] != ')':
            if  exp[idx[0]]  == '(' : # start new exp
                idx[0] += 1
                tmp = self.eval (exp,idx)
                operands[-1] = operands[-1]*10 + tmp
                continue

            elif exp[idx[0]]  == " ":
                idx[0] += 1
                continue

            elif exp[idx[0]].isdigit():
                operands[-1] = operands[-1] * 10 + int(exp[idx[0]])

            elif  exp[idx[0]] in ('+', '-'):
                operators.append(exp[idx[0]])
                operands.append(0) # start building new operand

            idx[0] += 1

        if idx[0] < len(exp ) and exp[idx[0]] == ')':
            idx[0] += 1

        # final res
        while len(operands) >= 2 :

            curr_op = operators.popleft()
            op1 = operands.popleft()
            if curr_op == '+':
                operands[0] += op1
            else:
                operands[0] = op1 - operands[0]
        return operands[0]


    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = self.eval(s,[0])
        return res



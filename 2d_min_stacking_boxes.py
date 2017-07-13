# n ^ 2 time
class Solution:
    def checkFit(self, inside_box, outer_box):
        if inside_box[0] < outer_box[0] and inside_box[1] < outer_box[1]:
            return True
        return False

    def stackingBoxes(self,boxes):
        stacks_count = 0
        for b in boxes:
            b.sort()
            
        boxes.sort(key = lambda x : (x[0],x[1]))
        placed = [False for _ in xrange(len(boxes))]

        idx = len(boxes) - 1
        while idx >= 0 :
            if not placed[idx]:
                stacks_count += 1
                placed[idx] = True
                curr_stack_top = boxes[idx]
                j = idx - 1
                while j >= 0 :
                    if not placed[j] and self.checkFit(boxes[j],curr_stack_top):
                        placed[j] = True
                        curr_stack_top = boxes[j]
                    j -= 1
            idx -= 1

        return stacks_count


s = Solution()

print s.stackingBoxes([[2, 4], [3, 5], [3, 6]])
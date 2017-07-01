class personNode:
    def __init__(self, h, i):
        self.left = None
        self.right = None
        self.val = 1
        self.height = h
        self.infront = i
class Solution:
    # @param heights : list of integers
	# @param infronts : list of integers
	# @return a list of integers

    def inorder(self, root, r ):
        # Time is O(n) to visit all n nodes in segment tree
        # Space Complexity is O ( log n ) for recursion stack function calls ( worest case is O(n) )
         if not root:
            return
         self.inorder(root.left,r)
         r.append(root.height)
         self.inorder(root.right,r)

    def insertPerson(self,root, person, val):
        # Time for insertion is O ( the height of tree ) ~ Avg : O(log n ) ,
        # worest is  O(n)
         if val < root.val:
            if not root.left:
                root.left = person
            else:
                self.insertPerson(root.left, person,val)
            root.val += 1
         else:
            if not root.right:
                root.right = person
            else:
                self.insertPerson(root.right,person,val-root.val)

    def order(self, heights, infronts):
        ## Total time complexity is O( n log n )
        ## Space complexity is O ( n )
        ## Where n is proportional to s which is  size of the input heights array
        #### n ~ 2 ^ ( log s + 1 )
         persons = [None] * len(heights)
         for i in range ( 0 , len(persons)):
            persons[i] = personNode(heights[i], infronts[i])
         persons.sort(key = lambda x : x.height, reverse= True) # Time is O(nlogn), space O(1)
         root = persons[0]
         for i in range(1, len(persons)): # O(n log n )
            self.insertPerson(root, persons[i], persons[i].infront)
         result =[] # O(n) extra memory
         self.inorder(root, result)
         return result







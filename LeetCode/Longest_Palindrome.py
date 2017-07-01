class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        Memory : O(n) for hash table
        Time Complexity =  n for builing Hash table + n for looping on hash items => O(2n) ~ O(n)
        """
        hash_t ={}
        for i in range(0, len(s)):
            if s[i] in hash_t:
                hash_t[s[i]] += 1
            else:
                hash_t[s[i]] = 1

        odd_ocur = 0
        long_l = 0

        for k,v in hash_t.iteritems():
            long_l += v
            if v%2 == 1:
                long_l -= 1
                odd_ocur += 1

        return  long_l + (odd_ocur >0)




# Testing
s = Solution()
print s.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth")
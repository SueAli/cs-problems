class Solution {
    public int maxArea(int[] height) {
        // Time complexity is O(n)
        // Space complexity is O(1)
        // The goal is to find the max area so we try to keep the width & height with max values
        // Using pointers
        int maxArea = -1;
        int i = 0;
        int j = height.length - 1;
        int n = height.length;
        
        while(i < n && j >= 0 && i!=j) {
            maxArea = Math.max(maxArea,
                              Math.min(height[i], height[j]) * (j - i));
            if(height[j] <= height[i]) {
                j --;
            } else {
                i ++;
            }
        }
        
        return maxArea;

    }
}

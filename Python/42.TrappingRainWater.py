class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        result = 0

        # To track highest point in traversal
        top1 = 0
        top2 = 0
        # For traversals
        arr1 = [0] * len(height)
        arr2 = [0] * len(height)
        
        # Beginning to end travelsal with i, reverse order with rev
        for i in range(len(height)):
            if height[i] > top1: 
                top1 = height[i]
            arr1[i] = top1 - height[i]
            # For reverse index
            rev = len(height)-1-i
            if height[rev] > top2:
                top2 = height[rev]
            arr2[rev] = top2 - height[rev]
        # Compare both arrays and count matching "boxes"
        for i in range(len(height)-1):
            if (arr1[i] > 0) and (arr2[i] > 0):
                result += min(arr1[i],arr2[i])
        
        return result
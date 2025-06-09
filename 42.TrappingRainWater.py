class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        n = len(height)
        result = 0

        # To track highest point in traversal
        top = 0
        # For traversals
        arr1 = [0] * n
        arr2 = [0] * n
        
        # Beginning to end travelsal
        for i in range(n):
            if height[i] > top: 
                top = height[i]
            arr1[i] = top - height[i]
        # End to beginning traversal
        top = 0
        for i in range(n-1, -1, -1):
            if height[i] > top:
                top = height[i]
            arr2[i] = top - height[i]
        # Compare both arrays and count matching "boxes"
        for i in range(n-1):
            if (arr1[i] > 0) and (arr2[i] > 0):
                result += min(arr1[i],arr2[i])
        
        return result

